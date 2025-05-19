import socket
import json
import threading
import time
from sorular import sorular
from random import sample

PROGRAM_HOST = "127.0.0.1"
PROGRAM_PORT = 4337
JOKER_HOST = "127.0.0.1"
JOKER_PORT = 4338


def joker_iste(joker_tipi, dogru_cevap):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as joker_socket:
            joker_socket.connect((JOKER_HOST, JOKER_PORT))
            istek = {
                "type": joker_tipi,
                "dogru": dogru_cevap
            }
            joker_socket.sendall(json.dumps(istek).encode())
            cevap = joker_socket.recv(1024).decode()
            return json.loads(cevap)
    except Exception as e:
        return {"hata": f"Joker sunucusuna bağlanırken hata: {str(e)}"}


def handle_client(conn, addr):
    print(f"[+] Bağlantı sağlandı: {addr}")
    kullanilan_jokerler = []
    oduller = [
        "Linç Yükleniyor",
        "Önemli olan katılmaktı",
        "İki birden büyüktür",
        "Buralara kolay gelmedik",
        "Sen bu işi biliyorsun",
        "Harikasın"
    ]

    try:
        secilecek_soru_sayisi = 5
        rastgele_sorular = sample(sorular, secilecek_soru_sayisi)

        dogru_sayisi = 0

        for index, soru in enumerate(rastgele_sorular):
            soru_gonder = soru.copy()
            soru_gonder["Soru No"] = f"Soru {index + 1}/{secilecek_soru_sayisi}"
            conn.sendall(json.dumps(soru_gonder).encode())

            while True:
                gelen_veri = conn.recv(1024).decode()
                if not gelen_veri:
                    raise Exception("İstemciden veri alınamadı. Bağlantı kesildi.")

                try:
                    mesaj = json.loads(gelen_veri)
                    if "joker" in mesaj:
                        joker_tipi = mesaj["joker"]
                        if joker_tipi in kullanilan_jokerler:
                            conn.sendall(json.dumps({
                                "hata": f"'{joker_tipi}' jokerini zaten kullandınız!"
                            }).encode())
                            continue
                        dogru_cevap = soru["Dogru Cevap"]
                        sonuc = joker_iste(joker_tipi, dogru_cevap)
                        if "hata" not in sonuc:
                            kullanilan_jokerler.append(joker_tipi)
                        conn.sendall(json.dumps(sonuc).encode())
                        continue

                except json.JSONDecodeError:
                    pass

                cevap = gelen_veri.strip().upper()
                if cevap == soru["Dogru Cevap"]:
                    dogru_sayisi += 1
                    conn.sendall(json.dumps({"durum": "dogru"}).encode())
                else:
                    conn.sendall(json.dumps({
                        "durum": "yanlis",
                        "dogru": soru["Dogru Cevap"],
                        "odul": oduller[dogru_sayisi]
                    }).encode())
                    break  # Yarışma biter
                time.sleep(0.3)
                break

        conn.sendall("Yarışma sona erdi!".encode())

    except Exception as e:
        print(f"[{addr}] Hata oluştu:", e)
        try:
            conn.sendall(json.dumps({"hata": str(e)}).encode())
        except:
            pass
    finally:
        conn.close()
        print(f"[{addr}] Bağlantı kapatıldı.")



def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((PROGRAM_HOST, PROGRAM_PORT))
        server.listen()
        print(f"[SERVER] Program Sunucusu başlatıldı. {PROGRAM_PORT} portunda dinleniyor...")

        while True:
            try:
                conn, addr = server.accept()
                threading.Thread(target=handle_client, args=(conn, addr)).start()
            except KeyboardInterrupt:
                print("\n[SERVER] Sunucu durduruluyor...")
                break


if __name__ == "__main__":
    start_server()

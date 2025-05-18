import socket
import json
from sorular import sorular
import time

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
        return {"hata": str(e)}

def handle_client(conn, addr):
    print(f"[+] Bağlantı sağlandı: {addr}")
    for soru in sorular:
        conn.sendall(json.dumps(soru).encode())

        try:
            gelen_veri = conn.recv(1024).decode()
            print(f"Gelen veri: {gelen_veri}")

            try:
                mesaj = json.loads(gelen_veri)
                if "joker" in mesaj:
                    joker_tipi = mesaj["joker"]
                    dogru_cevap = soru["Dogru Cevap"]
                    sonuc = joker_iste(joker_tipi, dogru_cevap)
                    conn.sendall(json.dumps(sonuc).encode())
                    continue
            except json.JSONDecodeError:
                pass  # JSON değilse cevap olarak kabul edilecek

            cevap = gelen_veri.strip().upper()
            print(f"Cevap: {cevap} / Doğru: {soru['Dogru Cevap']}")

            if cevap == soru["Dogru Cevap"]:
                conn.sendall(json.dumps({"durum": "dogru"}).encode())
            else:
                conn.sendall(json.dumps({
                    "durum": "yanlis",
                    "dogru": soru["Dogru Cevap"]
                }).encode())
            time.sleep(0.2)
        except Exception as e:
            print("HATA:", e)
            conn.sendall(json.dumps({"hata": str(e)}).encode())
            break

    conn.sendall("Yarışma sona erdi!".encode())
    conn.close()


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((PROGRAM_HOST, PROGRAM_PORT))
        server.listen()
        print(f"[SERVER] Program Sunucusu başlatıldı. {PROGRAM_PORT} portunda dinleniyor...")
        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)

if __name__ == "__main__":
    start_server()

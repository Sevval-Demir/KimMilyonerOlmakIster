import socket
import json
from sorular import sorular  # Sorular ayrı dosyadan geliyor

PROGRAM_HOST = "127.0.0.1"
PROGRAM_PORT = 4337  # Yarışmacı bu porta bağlanacak
JOKER_HOST = "127.0.0.1"
JOKER_PORT = 4338    # Joker sunucusuna bağlanılacak port

# 🔌 Joker sunucusuna istek gönderme fonksiyonu
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

# 👂 Yarışmacıdan gelen bağlantıları ve mesajları işle
def handle_client(conn, addr):
    print(f"[+] Bağlantı sağlandı: {addr}")
    for soru in sorular:
        conn.sendall(json.dumps(soru).encode())  # Soru gönder

        try:
            gelen_veri = conn.recv(1024).decode()
            mesaj = json.loads(gelen_veri)

            # 🎯 Eğer mesaj bir joker isteğiyse
            if "joker" in mesaj:
                joker_tipi = mesaj["joker"]
                dogru_cevap = soru["dogru"]
                sonuc = joker_iste(joker_tipi, dogru_cevap)
                conn.sendall(json.dumps(sonuc).encode())
                continue  # Bu soruda cevap beklemiyoruz, tekrar gönderiyoruz

        except json.JSONDecodeError:
            # 🤖 Normal cevapsa doğrudan kontrol edelim
            cevap = gelen_veri.strip().upper()
            print(f"Gelen cevap: {cevap}")

            if cevap == soru["dogru"]:
                conn.sendall("Doğru!".encode())
            else:
                conn.sendall(f"Yanlış! Doğru cevap: {soru['dogru']}".encode())
            continue  # Sıradaki soruya geç

    conn.sendall("Yarışma sona erdi!".encode())
    conn.close()

# 🧠 Sunucuyu başlatan ana fonksiyon
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((PROGRAM_HOST, PROGRAM_PORT))
        server.listen()
        print(f"[SERVER] Program Sunucusu başlatıldı. {PROGRAM_PORT} portunda dinleniyor...")

        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)

# 🏁 Ana fonksiyon çağrısı
if __name__ == "__main__":
    start_server()

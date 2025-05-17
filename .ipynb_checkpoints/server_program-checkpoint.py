import socket
import json
from sorular import sorular  # Soru listesi buradan geliyor

HOST = "127.0.0.1"
PORT = 4338

def handle_client(conn, addr):
    print(f"[+] Bağlantı sağlandı: {addr}")
    for soru in sorular:
        conn.sendall(json.dumps(soru).encode())

        # Cevap al
        cevap = conn.recv(1024).decode().strip().upper()
        print(f"Gelen cevap: {cevap}")

        if cevap == soru["dogru"]:
            conn.sendall("Doğru!".encode())
        else:
            conn.sendall(f"Yanlış! Doğru cevap: {soru['dogru']}".encode())

    conn.sendall("Yarışma sona erdi!".encode())
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Program Sunucusu başlatıldı. Port {PORT} dinleniyor...")

        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)

start_server()
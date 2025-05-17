import socket
import json

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1",4338))

    mesaj={
        "type":"seyirci",
        "dogru":"B"
    }

    s.sendall(json.dumps(mesaj).encode())
    cevap=s.recv(1024).decode()
    print("Gelen cevap: ",cevap)
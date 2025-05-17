import socket
import json
import random

host="127.0.0.1"
port=4338

def seyirci_joker(dogru_cevap):
    secenekler=["A","B","C","D"]
    oranlar={}

    #Dogru cevaba en yüksek % verilir
    dogru_yuzde=random.randint(40,60)
    kalan=100-dogru_yuzde
    yanlis_yuzde=[s for s in secenekler if s!=dogru_cevap]
    random.shuffle(yanlis_yuzde)

    for i,secenek in enumerate(yanlis_yuzde):
        if i<2:
            oranlar[secenek]=random.randint(0,kalan)
            kalan-=oranlar[secenek]
        else:
            oranlar[secenek]=kalan
    oranlar[dogru_cevap]=dogru_yuzde
    return oranlar

def yariyariya_joker(dogru_cevap):
    secenekler=["A","B","C","D"]
    yanlislar=[s for s in secenekler if s!=dogru_cevap]
    elenenler=random.sample(yanlislar, 2)
    kalanlar=[dogru_cevap]+[s for s in secenekler if s not in elenenler and s!=dogru_cevap]
    return kalanlar

def handle_request(data):
    try:
        joker_istek=json.loads(data)
        joker_tipi=joker_istek.get("type")
        dogru=joker_istek.get("dogru")

        if joker_tipi=="seyirci":
            return json.dumps(seyirci_joker(dogru))
        elif joker_tipi=="yariyariya":
            return json.dumps(yariyariya_joker(dogru))
        else:
            return json.dumps({"hata":"Gecersiz joker tipi"})
    except Exception as e:
        return json.dumps({"hata":str(e)})

def joker_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        print(f"[JOKER] {host}:{port} dinleniyor...")

        while True:
            conn,addr=s.accept()
            with conn:
                print(f"[JOKER] Baglanti: {addr}")
                data=conn.recv(1024).decode()
                if not data:
                    continue

                print("[JOKER] Gelen istek: ",data)
                cevap=handle_request(data)
                conn.sendall(cevap.encode())

if __name__=="__main__":
    joker_server()















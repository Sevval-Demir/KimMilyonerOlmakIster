# 🧠 Kim Milyoner Olmak İster - TCP Socket Tabanlı Yarışma Simülasyonu

- Python + TCP Socket + CustomTkinter ile yazılmış, çok modüllü bir bilgi yarışması oyunu.  
- Bilgisayar Ağları dersi için geliştirilmiştir. Ağ iletişimi, GUI tasarımı ve çoklu sunucu kontrolü bir arada ele alınmıştır.

---

## 🎯 Proje Amacı

Bu proje, TCP/IP soket programlamayı somut bir projeyle öğrenmek amacıyla geliştirilmiştir. Popüler yarışma formatı "Kim Milyoner Olmak İster" model alınarak:

- Yarışmacı (client),
- Ana program sunucusu,
- Joker sunucusu,

modülleri ayrı ayrı oluşturulmuş, grafik arayüz ile kullanıcı deneyimi sağlanmış ve Wireshark üzerinden ağ iletişimi analiz edilebilir hale getirilmiştir.

---

## 🧩 Mimaride Neler Var?

- **🎮 Yarışmacı (Client)**  
  `client_yarismaci.py`: GUI ile sunucuya bağlanır, soru alır, cevap verir, joker kullanır.

- **📡 Program Sunucusu (Server)**  
  `server_program.py`: Soruları sırayla yarışmacıya iletir, cevapları kontrol eder, joker isteklerini yönlendirir.

- **🧠 Joker Sunucusu (Bağımsız TCP Server)**  
  `server_joker.py`: Yarı yarıya, seyirci ve telefon jokerlerini işler.
---

## 🖥️ Uygulama Görselleri

### 🎮 Yarışmacı Arayüzü
![Yarışmacı Arayüzü](https://github.com/Sevval-Demir/KimMilyonerOlmakIster/blob/main/image1.jpeg)
![Yarışmacı Arayüzü](https://github.com/Sevval-Demir/KimMilyonerOlmakIster/blob/main/image4.jpeg)
### 🧠 Joker Kullanımı 
![Joker Kullanımı](https://github.com/Sevval-Demir/KimMilyonerOlmakIster/blob/main/image2.jpeg)
![Joker Kullanımı](https://github.com/Sevval-Demir/KimMilyonerOlmakIster/blob/main/image3.jpeg)
### 📶 Wireshark Trafik İzleme
![Wireshark İzleme](https://github.com/Sevval-Demir/KimMilyonerOlmakIster/blob/main/wireshark1.png)
![Wireshark İzleme](https://github.com/Sevval-Demir/KimMilyonerOlmakIster/blob/main/wireshark2.png)
![Wireshark İzleme](https://github.com/Sevval-Demir/KimMilyonerOlmakIster/blob/main/wireshark3.png)



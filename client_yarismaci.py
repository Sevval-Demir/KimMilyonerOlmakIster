import customtkinter as ctk
import socket
import json
from tkinter import messagebox

class YarismaciClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Yarışma Programı")
        self.root.geometry("800x600")
<<<<<<< HEAD
        self.root.configure(bg="#F5F3EF")  # kırık beyaz arka plan
=======
        self.root.configure(bg="#EAF9F4")  # Mint beyazı arka plan
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setup_ui()

        if not self.connect_to_server():
            self.root.destroy()
            return

        self.puan = 0
<<<<<<< HEAD
        self.dogru_sayisi = 0

        self.puan_label = ctk.CTkLabel(self.main_frame, text=f"Puan: {self.puan}", font=("Arial", 14), text_color="#3D3D3D")
=======
        self.puan_label = ctk.CTkLabel(
            self.main_frame, text=f"Puan: {self.puan}", 
            font=("Helvetica", 16, "bold"), text_color="#3A4D39"
        )
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)
        self.puan_label.pack(pady=10)

        self.get_next_question()

    def setup_ui(self):
<<<<<<< HEAD
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#F5F3EF")
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.soru_label = ctk.CTkLabel(
            self.main_frame, text="", font=("Arial", 16),
            wraplength=700, justify="left", text_color="#4C3A51"
        )
        self.soru_label.pack(pady=20)

        self.secenek_frame = ctk.CTkFrame(self.main_frame, fg_color="#F5F3EF")
=======
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#EAF9F4", corner_radius=15)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.soru_label = ctk.CTkLabel(
            self.main_frame, text="", font=("Helvetica", 18), 
            wraplength=700, justify="left", text_color="#3A4D39"
        )
        self.soru_label.pack(pady=20)

        self.secenek_frame = ctk.CTkFrame(self.main_frame, fg_color="#EAF9F4")
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)
        self.secenek_frame.pack(pady=10)

        self.secenek_buttons = []
        for i in range(4):
            btn = ctk.CTkButton(
                self.secenek_frame,
                text="",
<<<<<<< HEAD
                font=("Arial", 14),
                width=300,
                height=40,
                fg_color="#5D3FD3",
                hover_color="#7F5EE2",
                text_color="white",
                corner_radius=20,
=======
                font=("Helvetica", 15),
                width=320,
                height=45,
                fg_color="#C3EBD3",
                hover_color="#A6CF98",
                text_color="#3A4D39",
                corner_radius=12,
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)
                command=lambda idx=i: self.cevap_gonder(chr(65 + idx))
            )
            btn.pack(pady=7)
            self.secenek_buttons.append(btn)

<<<<<<< HEAD
        self.joker_frame = ctk.CTkFrame(self.main_frame, fg_color="#F5F3EF")
        self.joker_frame.pack(pady=20)

        self.seyirci_joker_btn = ctk.CTkButton(
            self.joker_frame, text="Seyirci Jokeri", font=("Arial", 12),
            fg_color="#D6CCFF", hover_color="#C4B5FD", text_color="#2F195F",
            corner_radius=15, command=lambda: self.joker_kullan("seyirci")
=======
        self.joker_frame = ctk.CTkFrame(self.main_frame, fg_color="#EAF9F4")
        self.joker_frame.pack(pady=20)

        self.seyirci_joker_btn = ctk.CTkButton(
            self.joker_frame, text="Seyirci Jokeri", font=("Helvetica", 13),
            fg_color="#C3EBD3", hover_color="#A6CF98", text_color="#3A4D39",
            corner_radius=10,
            command=lambda: self.joker_kullan("seyirci")
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)
        )
        self.seyirci_joker_btn.pack(side="left", padx=10)

        self.yariyariya_joker_btn = ctk.CTkButton(
<<<<<<< HEAD
            self.joker_frame, text="Yarı Yarıya Joker", font=("Arial", 12),
            fg_color="#D6CCFF", hover_color="#C4B5FD", text_color="#2F195F",
            corner_radius=15, command=lambda: self.joker_kullan("yariyariya")
        )
        self.yariyariya_joker_btn.pack(side="left", padx=10)

        self.bilgi_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 14), text_color="#3D3D3D")
        self.bilgi_label.pack(pady=10)

        self.seyirci_frame = ctk.CTkFrame(self.main_frame, fg_color="#F5F3EF")
        self.seyirci_labels = {}
        for i, sec in enumerate(["A", "B", "C", "D"]):
            lbl = ctk.CTkLabel(self.seyirci_frame, text=f"{sec}: %0", font=("Arial", 12), text_color="#4C3A51")
=======
            self.joker_frame, text="Yarı Yarıya Joker", font=("Helvetica", 13),
            fg_color="#C3EBD3", hover_color="#A6CF98", text_color="#3A4D39",
            corner_radius=10,
            command=lambda: self.joker_kullan("yariyariya")
        )
        self.yariyariya_joker_btn.pack(side="left", padx=10)

        self.bilgi_label = ctk.CTkLabel(self.main_frame, text="", font=("Helvetica", 15, "italic"))
        self.bilgi_label.pack(pady=10)

        self.seyirci_frame = ctk.CTkFrame(self.main_frame, fg_color="#EAF9F4")
        self.seyirci_labels = {}
        for i, sec in enumerate(["A", "B", "C", "D"]):
            lbl = ctk.CTkLabel(self.seyirci_frame, text=f"{sec}: %0", font=("Helvetica", 12), text_color="#3A4D39")
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)
            lbl.grid(row=0, column=i, padx=10)
            self.seyirci_labels[sec] = lbl

    def connect_to_server(self):
        try:
            self.socket.connect(("127.0.0.1", 4337))
            return True
        except Exception as e:
            messagebox.showerror("Hata", f"Sunucuya bağlanılamadı: {str(e)}")
            return False

    def get_next_question(self):
        try:
            data = self.socket.recv(1024).decode()
            if not data:
                return

            if "Yarışma sona erdi" in data:
                self.show_final_screen()
                return

            self.current_question = json.loads(data)
            self.show_question()
        except Exception as e:
            messagebox.showerror("Hata", f"Soru alınırken hata oluştu: {str(e)}")
            self.root.destroy()

<<<<<<< HEAD
    def fade_out_and_in(self):
        self.soru_label.configure(text="")
        for btn in self.secenek_buttons:
            btn.configure(text="", state="disabled")
        self.root.after(400, self.show_question)

=======
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)
    def show_question(self):
        soru_no = self.current_question.get("Soru No", "")
        soru_metni = self.current_question["Soru"]
        self.soru_label.configure(text=f"{soru_no}\n\n{soru_metni}")

        for i, sec in enumerate(["A", "B", "C", "D"]):
            self.secenek_buttons[i].configure(
                text=f"{sec}: {self.current_question[sec]}", state="normal"
            )

        self.seyirci_joker_btn.configure(state="normal")
        self.yariyariya_joker_btn.configure(state="normal")
        self.bilgi_label.configure(text="", text_color="#3A4D39")
        self.seyirci_frame.pack_forget()

    def cevap_gonder(self, cevap):
        try:
            self.socket.sendall(cevap.encode())

            for btn in self.secenek_buttons:
                btn.configure(state="disabled")
            self.seyirci_joker_btn.configure(state="disabled")
            self.yariyariya_joker_btn.configure(state="disabled")

            response = self.socket.recv(1024).decode()
            json_blocks = response.split("}{")
            if len(json_blocks) > 1:
                json_blocks = [json_blocks[0] + "}", "{" + json_blocks[1]]
            else:
                json_blocks = [response]

            data = json.loads(json_blocks[0])

            if data.get("durum") == "dogru":
<<<<<<< HEAD
                self.dogru_sayisi += 1
                self.bilgi_label.configure(text="Doğru Cevap!", text_color="#4CAF50")
                self.puan += 100
                self.puan_label.configure(text=f"Puan: {self.puan}")
                self.root.after(2000, self.get_next_question)
=======
                self.bilgi_label.configure(text="Doğru Cevap!", text_color="#3BB273")
                self.puan += 100
            elif data.get("durum") == "yanlis":
                self.bilgi_label.configure(text=f"Yanlış Cevap! Doğru: {data['dogru']}", text_color="#FF9E9E")
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)

            elif data.get("durum") == "yanlis":
                dogru = data["dogru"]
                odul = data.get("odul", "Hiçbir şey 😢")
                self.bilgi_label.configure(
                    text=f"Yanlış Cevap! Doğru: {dogru}\nKazandığınız: {odul}",
                    text_color="#E53935"
                )
                self.puan_label.configure(text=f"Puan: {self.puan}")
                self.root.after(3000, self.show_final_screen)

        except Exception as e:
            messagebox.showerror("Hata", f"Cevap gönderilirken hata oluştu: {str(e)}")

    def joker_kullan(self, joker_tipi):
        try:
            istek = {"joker": joker_tipi}
            self.socket.sendall(json.dumps(istek).encode())
            self.seyirci_joker_btn.configure(state="disabled")
            self.yariyariya_joker_btn.configure(state="disabled")

            response = self.socket.recv(1024).decode()
            joker_sonuc = json.loads(response)

            if "hata" in joker_sonuc:
                messagebox.showerror("Hata", joker_sonuc["hata"])
                return

            if joker_tipi == "seyirci":
                self.show_seyirci_joker(joker_sonuc)
            elif joker_tipi == "yariyariya":
                self.show_yariyariya_joker(joker_sonuc)

        except Exception as e:
            messagebox.showerror("Hata", f"Joker kullanılırken hata oluştu: {str(e)}")

    def show_seyirci_joker(self, oranlar):
        self.bilgi_label.configure(text="Seyirci Jokeri Sonuçları:", text_color="#3A4D39")
        for sec in ["A", "B", "C", "D"]:
            if sec in oranlar:
                self.seyirci_labels[sec].configure(text=f"{sec}: %{oranlar[sec]}")
        self.seyirci_frame.pack(pady=10)

    def show_yariyariya_joker(self, kalanlar):
        self.bilgi_label.configure(
            text=f"Yarı Yarıya Joker: {', '.join(kalanlar)} seçenekleri kaldı", text_color="#3A4D39"
        )
        for i, btn in enumerate(self.secenek_buttons):
            secenek = chr(65 + i)
            if secenek not in kalanlar:
                btn.configure(state="disabled")

    def show_final_screen(self):
        final_window = ctk.CTkToplevel(self.root)
        final_window.title("Yarışma Bitti")
        final_window.geometry("400x350")
        final_window.grab_set()
<<<<<<< HEAD
        final_window.configure(bg="#F5F3EF")

        ctk.CTkLabel(final_window, text="Yarışma Tamamlandı!", font=("Arial", 18)).pack(pady=20)
        ctk.CTkLabel(final_window, text=f"Toplam Puanınız: {self.puan}", font=("Arial", 16)).pack(pady=10)
        ctk.CTkLabel(final_window, text=f"Doğru Sayısı: {self.dogru_sayisi}", font=("Arial", 14)).pack(pady=5)

        oduller = [
            "Linç Yükleniyor",
            "Önemli olan katılmaktı",
            "İki birden büyüktür",
            "Buralara kolay gelmedik",
            "Sen bu işi biliyorsun",
            "Harikasın"
        ]
        kazanilan_odul = oduller[self.dogru_sayisi]
        ctk.CTkLabel(final_window, text=f"Kazandığınız: {kazanilan_odul}", font=("Arial", 14), wraplength=300).pack(pady=5)
=======
        final_window.configure(fg_color="#EAF9F4")

        ctk.CTkLabel(final_window, text="Yarışma Tamamlandı!", font=("Helvetica", 18), text_color="#3A4D39").pack(pady=20)
        ctk.CTkLabel(final_window, text=f"Toplam Puanınız: {self.puan}", font=("Helvetica", 16), text_color="#3A4D39").pack(pady=10)
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)

        if self.puan >= 500:
            mesaj = "Mükemmel! Gerçek bir bilgi ustasısınız! 🧠"
        elif self.puan >= 300:
            mesaj = "Harika! Çok iyi gidiyorsun! ⭐"
        elif self.puan >= 100:
            mesaj = "Fena değil, biraz daha çalışmayla mükemmel olur! 💪"
        else:
            mesaj = "Başlamak da bir başarı! Devam et! 🚀"

        ctk.CTkLabel(final_window, text=mesaj, font=("Helvetica", 14), wraplength=300, justify="center", text_color="#3A4D39").pack(pady=10)
        ctk.CTkButton(final_window, text="Kapat", command=self.root.destroy,
                      fg_color="#E2EBC3", hover_color="#A6CF98", text_color="#3A4D39", corner_radius=10).pack(pady=20)

# ...existing code...
if __name__ == "__main__":
<<<<<<< HEAD
    ctk.set_appearance_mode("light")
=======
    ctk.set_appearance_mode("light")  # Mint temaya uygun olarak açık tema
    ctk.set_default_color_theme("green")  # Light + yeşil uyumlu tema
>>>>>>> fd0b9ba (yarışmacı butonlarına animasyon eklendi, mint tema devam)
    root = ctk.CTk()
    app = YarismaciClient(root)
    root.mainloop()
# ...existing code...
import customtkinter as ctk
import socket
import json
from tkinter import messagebox



def connect_to_server(self):
    try:
        self.socket.connect(("127.0.0.1", 4337))
        messagebox.showinfo("Bağlantı", "Sunucuya bağlanıldı!")  # <-- Bu satırı ekleyin
    except Exception as e:
        messagebox.showerror("Hata", f"Sunucuya bağlanılamadı: {str(e)}")
        self.root.destroy()



class YarismaciClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Yarışma Programı")
        self.root.geometry("800x600")
        
        # Socket bağlantısı
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # GUI elemanları
        self.setup_ui()
        
        # Sunucuya bağlan
        self.connect_to_server()
        
        # İlk soruyu al
        self.get_next_question()
    
    def setup_ui(self):
        # Ana frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Soru alanı
        self.soru_label = ctk.CTkLabel(
            self.main_frame, 
            text="", 
            font=("Arial", 16),
            wraplength=700,
            justify="left"
        )
        self.soru_label.pack(pady=20)
        
        # Şıklar için frame
        self.secenek_frame = ctk.CTkFrame(self.main_frame)
        self.secenek_frame.pack(pady=10)
        
        self.secenek_buttons = []
        for i in range(4):
            btn = ctk.CTkButton(
                self.secenek_frame,
                text="",
                font=("Arial", 14),
                width=300,
                height=40,
                command=lambda idx=i: self.cevap_gonder(chr(65 + idx))
            )
            btn.pack(pady=5)
            self.secenek_buttons.append(btn)
        
        # Joker butonları
        self.joker_frame = ctk.CTkFrame(self.main_frame)
        self.joker_frame.pack(pady=20)
        
        self.seyirci_joker_btn = ctk.CTkButton(
            self.joker_frame,
            text="Seyirci Jokeri",
            font=("Arial", 12),
            command=lambda: self.joker_kullan("seyirci")
        )
        self.seyirci_joker_btn.pack(side="left", padx=10)
        
        self.yariyariya_joker_btn = ctk.CTkButton(
            self.joker_frame,
            text="Yarı Yarıya Joker",
            font=("Arial", 12),
            command=lambda: self.joker_kullan("yariyariya")
        )
        self.yariyariya_joker_btn.pack(side="left", padx=10)
        
        # Bilgi alanı
        self.bilgi_label = ctk.CTkLabel(
            self.main_frame,
            text="",
            font=("Arial", 14),
            text_color="yellow"
        )
        self.bilgi_label.pack(pady=10)
        
        # Seyirci joker sonuçları için frame
        self.seyirci_frame = ctk.CTkFrame(self.main_frame)
        self.seyirci_labels = {}
        for i, sec in enumerate(["A", "B", "C", "D"]):
            lbl = ctk.CTkLabel(self.seyirci_frame, text=f"{sec}: %0", font=("Arial", 12))
            lbl.grid(row=0, column=i, padx=10)
            self.seyirci_labels[sec] = lbl
    
    def connect_to_server(self):
        try:
            self.socket.connect(("127.0.0.1", 4337))
        except Exception as e:
            messagebox.showerror("Hata", f"Sunucuya bağlanılamadı: {str(e)}")
            self.root.destroy()
    
    def get_next_question(self):
        try:
            data = self.socket.recv(1024).decode()
            if not data:
                return
            
            if "Yarışma sona erdi" in data:
                messagebox.showinfo("Bilgi", "Yarışma sona erdi!")
                self.root.destroy()
                return
            
            self.current_question = json.loads(data)
            self.show_question()
        except Exception as e:
            messagebox.showerror("Hata", f"Soru alınırken hata oluştu: {str(e)}")
            self.root.destroy()
    
    def show_question(self):
        self.soru_label.configure(text=self.current_question["Soru"])
        
        for i, sec in enumerate(["A", "B", "C", "D"]):
            self.secenek_buttons[i].configure(
                text=f"{sec}: {self.current_question[sec]}",
                state="normal"
            )
        
        # Joker butonlarını aktif et
        self.seyirci_joker_btn.configure(state="normal")
        self.yariyariya_joker_btn.configure(state="normal")
        
        # Bilgi ve seyirci frame'ini temizle
        self.bilgi_label.configure(text="")
        self.seyirci_frame.pack_forget()
    
    def cevap_gonder(self, cevap):
        try:
            self.socket.sendall(cevap.encode())
            
            # Cevap gönderdikten sonra butonları devre dışı bırak
            for btn in self.secenek_buttons:
                btn.configure(state="disabled")
            
            # Joker butonlarını devre dışı bırak
            self.seyirci_joker_btn.configure(state="disabled")
            self.yariyariya_joker_btn.configure(state="disabled")
            
            # Sunucudan cevabı al
            response = self.socket.recv(1024).decode()
            
            if "Doğru" in response:
                self.bilgi_label.configure(text=response, text_color="green")
            else:
                self.bilgi_label.configure(text=response, text_color="red")
            
            # Sonraki soruya geç
            self.root.after(2000, self.get_next_question)
        except Exception as e:
            messagebox.showerror("Hata", f"Cevap gönderilirken hata oluştu: {str(e)}")
    
    def joker_kullan(self, joker_tipi):
        try:
            # Joker isteği gönder
            istek = {"joker": joker_tipi}
            self.socket.sendall(json.dumps(istek).encode())
            
            # Joker butonlarını devre dışı bırak
            self.seyirci_joker_btn.configure(state="disabled")
            self.yariyariya_joker_btn.configure(state="disabled")
            
            # Sunucudan joker cevabını al
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
        self.bilgi_label.configure(text="Seyirci Jokeri Sonuçları:", text_color="blue")
        
        for sec in ["A", "B", "C", "D"]:
            if sec in oranlar:
                self.seyirci_labels[sec].configure(text=f"{sec}: %{oranlar[sec]}")
        
        self.seyirci_frame.pack(pady=10)
    
    def show_yariyariya_joker(self, kalanlar):
        self.bilgi_label.configure(text=f"Yarı Yarıya Joker: {', '.join(kalanlar)} seçenekleri kaldı", text_color="blue")
        
        # Kalan seçenekler dışındaki butonları devre dışı bırak
        for i, btn in enumerate(self.secenek_buttons):
            secenek = chr(65 + i)
            if secenek not in kalanlar:
                btn.configure(state="disabled")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    app = YarismaciClient(root)
    root.mainloop()
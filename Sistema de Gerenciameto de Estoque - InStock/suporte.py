import customtkinter as ctk
import tkinter as tk
import os
import subprocess

class SupportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Suporte - InStock")
        self.root.geometry("600x400")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Obter o diretório atual
        self.diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Container principal
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=15, width=1000, height=700, fg_color="#2b2b2b")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Botão Voltar
        self.back_button = ctk.CTkButton(self.root, text="Voltar", width=100, height=30, command=self.voltar_home)
        self.back_button.place(relx=0.9, rely=0.05, anchor="center")

        # Título
        self.title_label = ctk.CTkLabel(self.main_frame, text="Suporte", font=("Arial", 24, "bold"), text_color="#ffffff")
        self.title_label.pack(pady=20)

        # Texto de descrição
        self.description_label = ctk.CTkLabel(self.main_frame, text="Para abrir um chamado ou entrar em contato conosco, utilize as opções abaixo:", font=("Arial", 14), text_color="#ffffff", wraplength=500)
        self.description_label.pack(pady=(10, 20))

        # Link para formulário de abertura de chamados
        self.form_label = ctk.CTkLabel(self.main_frame, text="Formulário para abertura de chamados:", font=("Arial", 14, "underline"), text_color="#1e90ff", cursor="hand2")
        self.form_label.pack(pady=5)
        self.form_label.bind("<Button-1>", lambda e: self.abrir_link("https://docs.google.com/forms/d/e/1FAIpQLSdWi83xT5Web7uDR8zf0XJjg-1N1aujPIpUVtNlPLHFFB26qw/viewform?usp=sf_link"))

        # E-mail de contato
        self.email_label = ctk.CTkLabel(self.main_frame, text="E-mail para contato: sup.instock@gmail.com", font=("Arial", 14), text_color="#ffffff")
        self.email_label.pack(pady=5)

        # Agendar a maximização da janela após a inicialização
        self.root.after(0, self.maximize_window)

    def voltar_home(self):
        self.root.destroy()
        subprocess.run(["python", os.path.join(self.diretorio_atual, "home.py")])

    def abrir_link(self, url):
        import webbrowser
        webbrowser.open_new(url)

    def maximize_window(self):
        self.root.state('zoomed')

if __name__ == "__main__":
    root = ctk.CTk()
    app = SupportApp(root)
    root.mainloop()

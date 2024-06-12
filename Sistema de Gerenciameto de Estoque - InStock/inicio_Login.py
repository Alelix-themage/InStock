import tkinter as tk
import customtkinter
from subprocess import call
from registrar_Usuario import TelaRegistro  # Importe a classe TelaRegistro
import verificacao
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def abrir_tela_registro():
    tela_registro = TelaRegistro(root)  # Crie uma instância da classe TelaRegistro
    root.withdraw()

def on_closing():
    root.destroy()

def maximize_window():
    root.state('zoomed')

def abrir_tela_home():
    print("Abrindo a tela home...")
    root.withdraw()
    # Obtém o diretório do script atual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Constrói o caminho absoluto para o script home.py
    home_script = os.path.join(current_dir, "home.py")
    print(f"Executando o script: {home_script}")  # Mensagem de depuração para verificar o caminho do script
    call(["python", home_script])
    root.destroy()

def login():
    # Passa pela verificação de senha para permitir o login
    usuario = user_entry.get()
    senha = senha_entry.get()
    if verificacao.validar(usuario, senha):
        abrir_tela_home()
    else:
        print("Senha Incorreta. Tente Novamente!")

root = customtkinter.CTk()
root.geometry("1280x720")
root.protocol("WM_DELETE_WINDOW", on_closing)

# Agendar a maximização da janela após a inicialização
root.after(0, maximize_window)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=50, padx=50, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="MultiShine", font=("Roboto", 50))
label.pack(padx=1, pady=20)

user_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Usuário", width=300, height=35)
user_entry.pack(padx=50, pady=5)

senha_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Senha", width=300, height=35, show="*")
senha_entry.pack(padx=50, pady=5)

entrar_button = customtkinter.CTkButton(master=frame, text="Entrar", command=login, width=300, height=35)
entrar_button.pack(padx=50, pady=5)

registro_button = customtkinter.CTkButton(master=frame, text="Registrar-se", command=abrir_tela_registro, width=300, height=35, fg_color="green")
registro_button.pack(padx=50, pady=5)

root.mainloop()

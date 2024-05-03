import tkinter as tk
import customtkinter
from registrar_Usuario import TelaRegistro

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def button_event():
    print("Entrou!")

def abrir_tela_registro():
    root.withdraw()  # Esconde a tela de login
    tela_registro = TelaRegistro(root)  # Cria a instância da tela de registro

def on_closing():
    root.destroy()  # Encerra a aplicação quando a janela de login é fechada

def mask_password_entry(event):
    senha_content = senha.get()
    senha.delete(0, tk.END)
    senha.insert(0, "*" * len(senha_content))

root = customtkinter.CTk()
root.geometry("1280x720")
root.protocol("WM_DELETE_WINDOW", on_closing)  # Define a função a ser chamada quando a janela é fechada

# Criando o frame principal
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=50, padx=50, fill="both", expand=True)

# Adicionando o conteúdo dentro do frame principal
label = customtkinter.CTkLabel(master=frame, text="MultiShine", font=("Roboto", 50))
label.pack(padx=1, pady=20)

user = customtkinter.CTkEntry(master=frame, placeholder_text="Usuário", width=300, height=35)
user.pack(padx=50, pady=5)

senha = customtkinter.CTkEntry(master=frame, placeholder_text="Senha", width=300, height=35)
senha.pack(padx=50, pady=5)
senha.bind("<Key>", mask_password_entry)  # Atualiza a máscara toda vez que uma tecla é pressionada

entrar = customtkinter.CTkButton(master=frame, text="Entrar", command=button_event, width=300, height=35)
entrar.pack(padx=50, pady=5)

registro = customtkinter.CTkButton(master=frame, text="Registrar-se", command=abrir_tela_registro, width=300, height=35, fg_color="green")
registro.pack(padx=50, pady=5)

root.mainloop()

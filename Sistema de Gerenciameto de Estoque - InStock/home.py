import os
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import subprocess

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1280x720")
root.title("InStock - Home")

# Obter o diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Função para maximizar a janela após a inicialização
def maximize_window():
    root.state('zoomed')

# Função para abrir a tela de consulta de estoque
def abrir_consulta_estoque():
    novo_arquivo = os.path.join(diretorio_atual, "consulta_estoque.py")
    print(f"Abrindo o arquivo: {novo_arquivo}")  # Mensagem de depuração para verificar o caminho do arquivo
    root.withdraw()
    subprocess.run(["python", novo_arquivo])
    root.destroy()  # Fechar a tela de home após a tela de consulta ser fechada

# Função para abrir a tela de cadastro de itens
def abrir_cadastro_itens():
    novo_arquivo = os.path.join(diretorio_atual, "cadastrar_itens.py")
    print(f"Abrindo o arquivo: {novo_arquivo}")
    root.withdraw()
    subprocess.run(["python", novo_arquivo])
    root.destroy()  # Fechar a tela de home após a tela de cadastro ser fechada

# Função para abrir a tela de suporte
def abrir_suporte():
    novo_arquivo = os.path.join(diretorio_atual, "suporte.py")
    print(f"Abrindo o arquivo: {novo_arquivo}")
    root.withdraw()
    subprocess.run(["python", novo_arquivo])
    root.destroy()  # Fechar a tela de home após a tela de suporte ser fechada

# Configurar o título e a fonte do rótulo principal
title_label = customtkinter.CTkLabel(master=root, text="InStock", font=("Roboto", 50, "bold"))
title_label.pack(padx=20, pady=(30, 10))

# Subtítulo
subtitle_label = customtkinter.CTkLabel(master=root, text="Bem-vindo ao InStock - O seu gerenciador de estoque", font=("Roboto", 20))
subtitle_label.pack(padx=20, pady=(0, 30))

# Configurar os botões com bordas e ícones
button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame.pack(pady=(0, 50))

# Função para carregar ícones
def load_icon(path, size):
    image = Image.open(path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

icon_size = (30, 30)
estoque_icon = load_icon(os.path.join(diretorio_atual, "images", "estoque_icon.png"), icon_size)
cadastro_icon = load_icon(os.path.join(diretorio_atual, "images", "cadastro_icon.png"), icon_size)
sup_icon = load_icon(os.path.join(diretorio_atual, "images", "sup_icon.png"), icon_size)

# Função para criar botões com efeito de hover
def create_button(master, text, command, description, image):
    button = customtkinter.CTkButton(
        master=master, 
        text=text, 
        command=command, 
        width=300, 
        height=50, 
        fg_color="#688EE8", 
        hover_color="#5077C7",
        border_width=2, 
        corner_radius=10,
        image=image, 
        compound="left"
    )
    button.bind("<Enter>", lambda event: show_description(description))
    button.bind("<Leave>", lambda event: hide_description())
    return button

# Criar os botões com descrição
estoque_button = create_button(button_frame, "Gerenciador de Estoque", abrir_consulta_estoque, "Abra o Gerenciador de Estoque", estoque_icon)
estoque_button.grid(row=0, column=0, padx=20, pady=10)

cadastro_button = create_button(button_frame, "Cadastrar Produto", abrir_cadastro_itens, "Cadastrar novo produto no sistema", cadastro_icon)
cadastro_button.grid(row=0, column=1, padx=20, pady=10)

sup_button = create_button(button_frame, "Suporte", abrir_suporte, "Entre em contato com o Suporte", sup_icon)
sup_button.grid(row=0, column=2, padx=20, pady=10)

# Criar um frame para conter o conteúdo principal e definir um fundo
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Adicionar um texto descritivo ou informativo no frame principal
info_label = customtkinter.CTkLabel(master=frame, text="Selecione uma das opções acima para começar a gerenciar seu estoque.", font=("Roboto", 16))
info_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Funções para mostrar e esconder as descrições
def show_description(description):
    info_label.configure(text=description)

def hide_description():
    info_label.configure(text="Selecione uma das opções acima para começar a gerenciar seu estoque.")

# Agendar a maximização da janela após a inicialização
root.after(0, maximize_window)

# Iniciar o loop principal da interface
root.mainloop()

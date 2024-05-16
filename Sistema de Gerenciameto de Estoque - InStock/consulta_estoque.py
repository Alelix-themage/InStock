import tkinter as tk
import customtkinter
import sqlite3 as sq
from tkinter import messagebox
import pandas as pd
from pandastable import Table

# Configuração do tema do customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Conexão com o banco de dados 'Estoque.db'
banco_de_dados = sq.connect("Estoque.db")
cursor = banco_de_dados.cursor()

# Função para criar o banco de dados com produtos cadastrados (caso necessário)
def criar_banco(nome_item):
    cursor.execute("INSERT INTO Estoque (Item, Quantidade, Preço) VALUES (?, ?, ?)", (nome_item, 0, 0.0))
    banco_de_dados.commit()

# Função para consultar produtos no banco de dados com base no critério de pesquisa
def consultar_produtos():
    # Obtém o texto de pesquisa do campo de entrada
    texto_pesquisa = adicionar_item.get()

    # Consulta SQL com cláusula LIKE para buscar produtos com base no nome
    consulta_sql = "SELECT Cod, Item, Quantidade, Preço FROM Estoque WHERE Item LIKE ?;"

    # Executa a consulta com o texto de pesquisa (usando '%' para procurar parte do nome)
    cursor.execute(consulta_sql, ('%' + texto_pesquisa + '%',))
    resultados = cursor.fetchall()

    # Exibe os resultados na área de texto
    if resultados:
        # Cria um DataFrame Pandas com os resultados
        df = pd.DataFrame(resultados, columns=["Cod, Item", "Quantidade", "Preço"])
        
        # Cria um widget de tabela usando PandasTable
        table = Table(frame, dataframe=df)
        table.show()
    else:
        messagebox.showinfo("Nenhum Resultado", "Nenhum resultado encontrado.")

# Criando a janela principal
janela = customtkinter.CTk()
janela.title("Consulta de Estoque - Multishine")
janela.geometry("800x600+400+200")

# Definindo cor de fundo e fonte
cor_fundo = "#0a0a0a"  # Cor escura de fundo
fonte_titulo = ("Roboto", 20, "bold")
fonte = ("Roboto", 12)

# Título da janela
titulo = customtkinter.CTkLabel(janela, text="Consulta de Estoque", font=fonte_titulo)
titulo.pack(pady=(30, 20))

# Frame para conter os widgets
frame = tk.Frame(janela, bg=cor_fundo)
frame.pack(padx=50, pady=20)

# Widget para texto de instrução
texto_item = customtkinter.CTkLabel(frame, text="Digite o nome do item:", font=fonte)
texto_item.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Campo de entrada para adicionar ou pesquisar produtos
adicionar_item = customtkinter.CTkEntry(frame, placeholder_text="Item", width=50)
adicionar_item.grid(row=0, column=1, padx=10, pady=10)

# Botão para consultar produtos
button_consultar = customtkinter.CTkButton(frame, text="Consultar", command=consultar_produtos, width=20)
button_consultar.grid(row=0, column=2, padx=10, pady=10)

# Configura a cor de fundo da janela
janela.configure(bg=cor_fundo)

# Inicia o loop principal da aplicação
janela.mainloop()
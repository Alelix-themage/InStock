
import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import messagebox  # Importa a classe messagebox para exibir caixas de mensagem
from PIL import ImageTk, Image  # Importa a biblioteca PIL para manipulação de imagens
import sqlite3 as sq  # Importa a biblioteca sqlite3 para trabalhar com banco de dados
import customtkinter # Importa a bliblioteca customTkinder para desing

# Conecta-se ao banco de dados 'Estoque.db'
banco_de_dados = sq.connect("Estoque.db")
cursor = banco_de_dados.cursor()

# Função para criar o banco de dados com produtos cadastrados (caso necessário)
def criar_banco(nome_item):
    cursor.execute("INSERT INTO Estoque (Item, quantidade, preco) VALUES (?, ?, ?)", (nome_item, 0, 0.0))
    banco_de_dados.commit()
    
# Função para consultar produtos no banco de dados com base no critério de pesquisa
def consultar_produtos():
    # Obtenha o texto de pesquisa do campo de entrada
    texto_pesquisa = adicionar_item.get()
    
    # Consulta SQL com cláusula LIKE para buscar produtos com base no nome
    consulta_sql = "SELECT Cod, Item, Quantidade, Preço FROM Estoque WHERE Item LIKE ?;"
    
    # Executa a consulta com o texto de pesquisa (usando '%' para procurar parte do nome)
    cursor.execute(consulta_sql, ('%' + texto_pesquisa + '%',))
    resultados = cursor.fetchall()
    resultado_texto.config(state='normal')

    # Limpa o conteúdo anterior na área de texto de resultados
    resultado_texto.delete(1.0, tk.END)
    
    # Exibe os resultados na área de texto
    for produto in resultados:
        linha = f"Cod: {produto[0]}, Item: {produto[1]}, Quantidade: {produto[2]}, Preço: R${produto[3]:.2f}\n"
        resultado_texto.insert(tk.END, linha)

        resultado_texto.config(state='disabled')

# Função chamada quando a janela é redimensionada
def redimensionar(event):
    largura_janela = event.width
    altura_janela = event.height

# Criando a janela principal
janela = tk.Tk()
janela.title("Consulta de Estoque - Multishine")
janela.geometry("700x360+400+400")

# Definindo cor de fundo e fonte
cor_fundo = "royal blue"
cor_texto = "black"
fonte = ("Helvetica", 12, "bold")
customtkinter.set_appearance_mode("dark")

# Widget para texto de instrução
texto_item = tk.Label(janela, text="DIGITE O SEU ITEM:", bg=cor_fundo, font=fonte)
texto_item.place(relx=0.5, rely=0.1, anchor="center")

# Campo de entrada para adicionar ou pesquisar produtos
adicionar_item = tk.Entry(janela, bg="light gray", width=40, font=fonte)
adicionar_item.place(relx=0.5, rely=0.2, anchor="center")

# Botão para consultar produtos
button_consultar = tk.Button(janela, text="CONSULTAR", font=fonte, command=consultar_produtos)
button_consultar.place(relx=0.5, rely=0.3, anchor="center")

# Área de texto para exibir os resultados da consulta
resultado_texto = tk.Text(janela, bg="light gray", width=50, height=10, font=fonte)
resultado_texto.place(relx=0.5, rely=0.6, anchor="center")
resultado_texto.config(state='disabled')

# Configura a cor de fundo da janela
janela.configure(bg=cor_fundo)

# Inicia o loop principal da aplicação
janela.mainloop()
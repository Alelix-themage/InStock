import os
import tkinter as tk
import customtkinter
import sqlite3 as sq
from tkinter import messagebox, filedialog
import pandas as pd
from pandastable import Table, TableModel
import subprocess

# Configuração do tema do customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Conexão com o banco de dados 'Estoque.db'
banco_de_dados = sq.connect("Estoque.db")
cursor = banco_de_dados.cursor()

# Função para criar o banco de dados com produtos cadastrados (caso necessário)
def criar_banco(nome_item):
    cursor.execute("INSERT INTO Estoque (Cod, Item, Quantidade, Preço) VALUES (?, ?, ?, ?)", (None, nome_item, 0, 0.0))
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
        df = pd.DataFrame(resultados, columns=["Cod", "Item", "Quantidade", "Preço"])

        # Cria um modelo de tabela PandasTable
        model = TableModel(dataframe=df)

        # Limpa o frame antes de exibir uma nova tabela
        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # Cria um widget de tabela usando PandasTable
        table = Table(frame_tabela, model=model, editable=True)
        table.show()

        # Função para capturar as alterações na tabela
        def on_edit_cell(row, col, value):
            cod = df.iloc[row]["Cod"]
            column_name = df.columns[col]
            # Atualiza o DataFrame
            df.at[row, column_name] = value
            # Atualiza o banco de dados
            cursor.execute(f"UPDATE Estoque SET {column_name} = ? WHERE Cod = ?", (value, cod))
            banco_de_dados.commit()

        # Bind the edit cell function
        table.bind('celledited', lambda event, row, col, value: on_edit_cell(row, col, value))
        table.redraw()  # Força a atualização da tabela

        # Mostra o botão Nova Consulta
        button_nova_consulta.grid(row=0, column=2, padx=10, pady=10)
        # Mostra o botão Exportar Excel
        button_exportar_excel.grid(row=0, column=3, padx=10, pady=10)

    else:
        messagebox.showinfo("Nenhum Resultado", "Nenhum resultado encontrado.")
        # Esconde o botão Nova Consulta se não houver resultados
        button_nova_consulta.grid_forget()
        # Esconde o botão Exportar Excel se não houver resultados
        button_exportar_excel.grid_forget()

# Função para realizar uma nova consulta
def nova_consulta():
    adicionar_item.delete(0, tk.END)
    for widget in frame_tabela.winfo_children():
        widget.destroy()
    # Esconde o botão Nova Consulta após limpar os resultados
    button_nova_consulta.grid_forget()
    # Mostra o botão Exportar Excel
    button_exportar_excel.grid(row=0, column=3, padx=10, pady=10)

# Função para deletar o item do banco de dados
def deletar_item():
    texto_item = adicionar_item.get()
    consulta_sql = "DELETE FROM Estoque WHERE Item LIKE ?;"
    cursor.execute(consulta_sql, ('%' + texto_item + '%',))
    banco_de_dados.commit()
    messagebox.showinfo("Item Deletado", "O item foi deletado com sucesso.")
    # Atualiza a consulta para refletir as alterações
    consultar_produtos()

# Função para exportar resultados para Excel
def exportar_excel():
    consulta_sql = "SELECT Cod, Item, Quantidade, Preço FROM Estoque WHERE Item LIKE ?;"
    texto_pesquisa = adicionar_item.get()
    cursor.execute(consulta_sql, ('%' + texto_pesquisa + '%',))
    resultados = cursor.fetchall()

    if resultados:
        df = pd.DataFrame(resultados, columns=["Cod", "Item", "Quantidade", "Preço"])
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])

        if file_path:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Exportação Concluída", "Os resultados foram exportados com sucesso!")
    else:
        messagebox.showinfo("Exportação Falhou", "Nenhum dado disponível para exportar.")

# Função para voltar à tela inicial
def voltar_home():
    janela.destroy()
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "home.py")
    subprocess.run(["python", script_path])

# Função para encerrar o programa quando a janela for fechada
def fechar_janela():
    janela.quit()

# Criando a janela principal
janela = customtkinter.CTk()
janela.title("Consulta de Estoque - Multishine")

# Definindo cor de fundo e fonte
cor_fundo = "#0a0a0a"  # Cor escura de fundo
fonte_titulo = ("Roboto", 24, "bold")
fonte = ("Roboto", 14)

# Função para maximizar a janela após a inicialização
def maximize_window():
    janela.state('zoomed')

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
adicionar_item = customtkinter.CTkEntry(frame, placeholder_text="Item", width=400)
adicionar_item.grid(row=0, column=1, padx=10, pady=10)

# Botão para consultar produtos
button_consultar = customtkinter.CTkButton(frame, text="Consultar", command=consultar_produtos)
button_consultar.grid(row=0, column=2, padx=10, pady=10)

# Botão para exportar resultados para Excel
button_exportar_excel = customtkinter.CTkButton(frame, text="Exportar Excel", command=exportar_excel)
button_exportar_excel.grid(row=0, column=3, padx=10, pady=10)

# Botão para deletar o item do banco
button_delete = customtkinter.CTkButton(frame, text="Deletar", command=deletar_item)
button_delete.grid(row=0, column=4, padx=10, pady=10)

# Frame para exibir a tabela de resultados
frame_tabela = tk.Frame(janela, bg=cor_fundo)
frame_tabela.pack(fill='both', expand=True, padx=50, pady=(20, 50))

# Configura a cor de fundo da janela
janela.configure(bg=cor_fundo)

# Configura a ação de fechamento da janela
janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Agendar a maximização da janela após a inicialização
janela.after(0, maximize_window)

# Função para posicionar o botão "Voltar" no canto superior direito da janela
def position_button_voltar(event=None):
    x = janela.winfo_width() - 20
    button_voltar.place(x=x, y=20, anchor='ne')

# Criando o botão "Voltar"
button_voltar = customtkinter.CTkButton(janela, text="Voltar", command=voltar_home)
button_voltar.bind('<Configure>', position_button_voltar)
button_voltar.pack()

# Criando o botão "Nova Consulta" (inicialmente escondido)
button_nova_consulta = customtkinter.CTkButton(frame, text="Nova Consulta", command=nova_consulta)

# Inicia o loop principal da aplicação
janela.mainloop()
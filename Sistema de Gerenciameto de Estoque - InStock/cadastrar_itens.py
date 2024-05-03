import tkinter as tk
from tkinter import messagebox
import banco_estoque

janela = tk.Tk()
janela.title("Cadastro de Estoque")
janela.geometry("700x320")

input_item = tk.Label(janela, text="Item:")
input_item.pack()

input_item = tk.Entry(janela)
input_item.pack()

input_quantidade = tk.Label(janela, text="Quantidade:")
input_quantidade.pack()

input_quantidade = tk.Entry(janela)
input_quantidade.pack()

input_preco = tk.Label(janela, text="Preço:")
input_preco.pack()

input_preco = tk.Entry(janela)
input_preco.pack()

def registra_item():
    item = input_item.get()
    quantidade = input_quantidade.get()
    preco = input_preco.get()
    banco_estoque.cursor.execute("""
        INSERT INTO estoque(Item, Quantidade, Preço) VALUES(?, ?, ?)                            
     """,(item, quantidade, preco))
    banco_estoque.conn.commit()
    messagebox.showinfo(title="Alerta de Cadastro", message="Cadastro do item realizado com Sucesso!")

cadastrar_button = tk.Button(janela, text="Cadastrar", command=registra_item)
cadastrar_button.pack()

janela.mainloop()

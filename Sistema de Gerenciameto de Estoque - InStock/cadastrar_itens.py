import customtkinter as ctk
from tkinter import messagebox
import sqlite3 as sq
import os
import subprocess

class ItemRegisterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Itens")
        self.root.geometry("600x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Obter o diretório atual
        self.diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Container principal
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=15, width=550, height=600, fg_color="#2b2b2b")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Botão Voltar
        self.back_button = ctk.CTkButton(self.root, text="Voltar", width=100, height=30, command=self.voltar_home)
        self.back_button.place(relx=0.9, rely=0.05, anchor="center")

        # Título
        self.title_label = ctk.CTkLabel(self.main_frame, text="Cadastro de Itens", font=("Arial", 24, "bold"), text_color="#ffffff")
        self.title_label.pack(pady=20)

        # Nome do Item
        self.name_label = ctk.CTkLabel(self.main_frame, text="Nome do Item *", font=("Arial", 14), text_color="#ffffff")
        self.name_label.pack(anchor="w", pady=(10, 5), padx=20)
        self.name_entry = ctk.CTkEntry(self.main_frame, width=400, height=30, font=("Arial", 12), placeholder_text="Digite o nome do item")
        self.name_entry.pack(anchor="w", padx=20)

        # Quantidade em Estoque
        self.stock_label = ctk.CTkLabel(self.main_frame, text="Quantidade em Estoque *", font=("Arial", 14), text_color="#ffffff")
        self.stock_label.pack(anchor="w", pady=(10, 5), padx=20)
        self.stock_entry = ctk.CTkEntry(self.main_frame, width=400, height=30, font=("Arial", 12), placeholder_text="Digite a quantidade em estoque")
        self.stock_entry.pack(anchor="w", padx=20)

        # Preço
        self.price_label = ctk.CTkLabel(self.main_frame, text="Preço *", font=("Arial", 14), text_color="#ffffff")
        self.price_label.pack(anchor="w", pady=(10, 5), padx=20)
        self.price_entry = ctk.CTkEntry(self.main_frame, width=400, height=30, font=("Arial", 12), placeholder_text="Digite o preço do item")
        self.price_entry.pack(anchor="w", padx=20)

        # Botões
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(pady=30)

        self.register_button = ctk.CTkButton(self.button_frame, text="Cadastrar", width=150, height=40, command=self.register_item, fg_color="#4caf50", hover_color="#45a049")
        self.register_button.pack(side="left", padx=20)

        self.clear_button = ctk.CTkButton(self.button_frame, text="Limpar", width=150, height=40, command=self.confirm_clear_form, fg_color="#f44336", hover_color="#e53935")
        self.clear_button.pack(side="right", padx=20)

        # Barra de Status
        self.status_bar = ctk.CTkLabel(self.root, text="", font=("Arial", 12), text_color="#ffffff")
        self.status_bar.pack(side="bottom", fill="x")

        # Melhorias na interação
        self.name_entry.focus_set()
        self.name_entry.bind("<Return>", lambda event: self.stock_entry.focus_set())
        self.stock_entry.bind("<Return>", lambda event: self.price_entry.focus_set())
        self.price_entry.bind("<Return>", lambda event: self.register_item())

        # Agendar a maximização da janela após a inicialização
        self.root.after(0, self.maximize_window)

    def maximize_window(self):
        self.root.state('zoomed')

    def validate_fields(self):
        name = self.name_entry.get().strip()
        price = self.price_entry.get().strip()
        stock = self.stock_entry.get().strip()

        if not name:
            self.status_bar.configure(text="Nome do item é obrigatório.", text_color="red")
            return False
        if not stock.isdigit():
            self.status_bar.configure(text="Quantidade em estoque deve ser um número inteiro.", text_color="red")
            return False
        if not self.is_float(price):
            self.status_bar.configure(text="Preço deve ser um número válido.", text_color="red")
            return False
        return True

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def register_item(self):
        if not self.validate_fields():
            return

        name = self.name_entry.get().strip()
        price = float(self.price_entry.get().strip())
        stock = int(self.stock_entry.get().strip())

        try:
            conn = sq.connect("Estoque.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO estoque (Item, Quantidade, Preço) VALUES (?, ?, ?)", (name, stock, price))
            conn.commit()
            conn.close()
            self.status_bar.configure(text="Item cadastrado com sucesso!", text_color="green")
            self.clear_form(after_registration=True)
        except Exception as e:
            self.status_bar.configure(text=f"Erro ao cadastrar item: {e}", text_color="red")

    def confirm_clear_form(self):
        result = messagebox.askyesno("Confirmar", "Tem certeza que deseja limpar o formulário?")
        if result:
            self.clear_form()

    def clear_form(self, after_registration=False):
        self.name_entry.delete(0, "end")
        self.price_entry.delete(0, "end")
        self.stock_entry.delete(0, "end")
        if not after_registration:
            self.status_bar.configure(text="Formulário limpo", text_color="blue")

    def voltar_home(self):
        self.root.destroy()
        subprocess.run(["python", os.path.join(self.diretorio_atual, "home.py")])

if __name__ == "__main__":
    root = ctk.CTk()
    app = ItemRegisterApp(root)
    root.mainloop()

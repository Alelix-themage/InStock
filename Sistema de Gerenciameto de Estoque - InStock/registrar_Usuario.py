import tkinter as tk
import customtkinter
from tkinter import messagebox
import databaseUser
import bcrypt

class TelaRegistro(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registro")
        self.geometry("1280x720")
        self.master = master
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Maximize a janela ao ser criada
        self.state('zoomed')
        
        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=0, padx=0, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Registro", font=("Roboto", 50))
        label.pack(padx=0, pady=20)

        self.user = customtkinter.CTkEntry(master=frame, placeholder_text="Nome", width=300, height=35)
        self.user.place(relx=0.5, rely=0.240, anchor=tk.CENTER)

        self.email = customtkinter.CTkEntry(master=frame, placeholder_text="Email", width=300, height=35)
        self.email.place(relx=0.5, rely=0.320, anchor=tk.CENTER)

        self.cpf = customtkinter.CTkEntry(master=frame, placeholder_text="CPF", width=300, height=35)
        self.cpf.place(relx=0.5, rely=0.400, anchor=tk.CENTER)

        self.senha = customtkinter.CTkEntry(master=frame, placeholder_text="Senha", width=300, height=35, show="*")
        self.senha.place(relx=0.5, rely=0.480, anchor=tk.CENTER)
        
        registro = customtkinter.CTkButton(master=frame, text="Registrar conta", command=self.button_event, width=300, height=35, fg_color="green")
        registro.place(relx=0.5, rely=0.560, anchor=tk.CENTER)

        voltar = customtkinter.CTkButton(master=frame, text="Voltar", command=self.voltar_para_login, width=300, height=35)
        voltar.place(relx=0.5, rely=0.640, anchor=tk.CENTER)

    def cript(self):
        senha = self.senha.get().encode("utf-8")
        self.hash = bcrypt.hashpw(senha, bcrypt.gensalt()).decode('utf-8')
        print(f"Senha criptografada: {self.hash}")
    
    def button_event(self):
        self.cript()
        self.cadastraUserTable()

    def cadastraUserTable(self):
        nome = self.user.get()
        email = self.email.get()
        cpf = self.cpf.get()
        senha_criptografada = self.hash
        
        databaseUser.cursor.execute("""
            INSERT INTO Users(Nome, Email, CPF, Senha) VALUES(?, ?, ?, ?)                            
        """, (nome, email, cpf, senha_criptografada))
        databaseUser.conn.commit()
        messagebox.showinfo(title="Alerta de Cadastro", message="Usuário registrado com sucesso!")

    def voltar_para_login(self):
        self.destroy()
        self.master.deiconify()
        self.master.state('zoomed')  # Maximize a tela de login

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaRegistro(root)
    root.mainloop()

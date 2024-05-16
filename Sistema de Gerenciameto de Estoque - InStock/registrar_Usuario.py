import tkinter as tk
import customtkinter
from tkinter import messagebox
import databaseUser
from hashlib import md5

class TelaRegistro(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Registro")
        self.geometry("1280x720")
        self.master = master
        
        # Aplicar o tema personalizado após a criação da janela
        customtkinter.set_appearance_mode("dark")  
        customtkinter.set_default_color_theme("blue")
        
        # Conteúdo da janela de registro
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

        self.senha = customtkinter.CTkEntry(master=frame, placeholder_text="Senha", width=300, height=35)
        self.senha.place(relx=0.5, rely=0.480, anchor=tk.CENTER)
        
        
        registro = customtkinter.CTkButton(master=frame, text="Registrar conta", command=self.button_event, width=300, height=35, fg_color="green")
        registro.place(relx=0.5, rely=0.560, anchor=tk.CENTER)

        # Botão de voltar
        voltar = customtkinter.CTkButton(master=frame, text="Voltar", command=self.voltar_para_login, width=300, height=35)
        voltar.place(relx=0.5, rely=0.640, anchor=tk.CENTER)

    
    def cript(self):
        """Função que criptografa a senha do sqlite"""
        senha = self.senha.get()
        texto_cripto = senha.encode("utf-8")
        self.hash = md5(texto_cripto).hexdigest()  # Convertendo a hash para uma string hexadecimal
    
    def button_event(self):
        self.cript()  # Chama o método para calcular a hash da senha
        self.cadastraUserTable()

    def cadastraUserTable(self):
        nome = self.user.get()
        email = self.email.get()
        cpf = self.cpf.get()
        #criptografia de senha
        senha_criptografada = self.hash
        
        databaseUser.cursor.execute("""
            INSERT INTO Users(Nome, Email, CPF, Senha) VALUES(?, ?, ?, ?)                            
        """,(nome, email, cpf, senha_criptografada))
        databaseUser.conn.commit()
        messagebox.showinfo(title="Alerta de Cadastro", message="Usuário realizado com Sucesso!")

    def voltar_para_login(self):
        self.destroy()  # Fecha a janela de registro
        self.master.deiconify()  # Exibe a tela de login novamente
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TelaRegistro(root)
    root.mainloop()

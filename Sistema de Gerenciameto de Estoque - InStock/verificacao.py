import sqlite3
import bcrypt

def verificaLogin(usuario, senha):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    query = "SELECT Senha FROM Users WHERE Nome = ?"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        senha_hash_armazenada = resultado[0]
        senha_fornecida = senha.encode('utf-8')
        
        print(f"Senha fornecida: {senha_fornecida}")
        print(f"Senha armazenada: {senha_hash_armazenada}")
        
        return bcrypt.checkpw(senha_fornecida, senha_hash_armazenada.encode('utf-8'))
    return False

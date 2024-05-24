import sqlite3
from hashlib import md5

def verificaLogin(usuario, senha):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    query = "SELECT Senha FROM Users WHERE Nome = ?"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        senha_hash_armazenada = resultado[0]
        senha_hash_fornecida = md5(senha.encode("utf-8")).hexdigest()
        
        print("Senha fornecida:", senha_hash_fornecida)
        print("Senha armazenada:", senha_hash_armazenada)
        
        return senha_hash_fornecida == senha_hash_armazenada
    return False

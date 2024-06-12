import sqlite3
from hashlib import md5

def buscar_usuario(usuario):
    '''buscar usuário no banco, para puxar a senha'''
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT senha FROM Users WHERE Nome = ?
    ''', (usuario,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def codificar(usuario, senha):
    '''codificação da senha, criando um hash'''
    texto = senha.encode('utf-8')
    hash = md5(texto).hexdigest()
    print("Senha codificada: " + hash)

def validar(usuario, senha):
    ''' Validação da senha '''
    hash_correto = buscar_usuario(usuario)
    if not hash_correto:
        print("Usuário não encontrado!")
        return False
    texto = senha.encode('utf-8')
    hash = md5(texto).hexdigest()
    if hash == hash_correto:
        print("Senha Válida")
        print("Senha codificada: " + hash)
        return True
    else:
        print("Senha Inválida!")
        return False

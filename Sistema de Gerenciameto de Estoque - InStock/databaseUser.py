import sqlite3 as sq

conn = sq.connect("user.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Email TEXT NOT NULL,
        CPF INTEGER NOT NULL,
        Senha TEXT NOT NULL 
    );
""")

print("Banco de dados do usuário conectado!")

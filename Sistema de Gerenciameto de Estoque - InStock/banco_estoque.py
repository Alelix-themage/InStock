import sqlite3 as sq

conn = sq.connect("Estoque.db")

cursor  = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque(
        Cod INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
        Item TEXT NOT NULL,
        Quantidade INTEGER NOT NULL,
        Preço FLOAT NOT NULL
    );
""")

print("Banco de dados conectado!")

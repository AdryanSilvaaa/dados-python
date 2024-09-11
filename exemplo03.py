import sqlite3
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM produtos"

cursor.execute(selecionar_produtos)
  
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
    
conn.close()
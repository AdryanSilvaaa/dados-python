#Inserindo dados a tabela (exemplo.db)

import sqlite3
#conectando o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#dados do novo produto
novo_produto = ("camisa", 100.50, 50)
#comando SQL para inserir o novo produto na tabela
inserir_produto = "INSERT INTO produtos (nome, preco, estoque) VALUES(?,?,?)"
#Executando o comando SQL para inserção 
cursor.execute(inserir_produto , novo_produto)
#confirmando as alterações 
conn.commit()
#fechando a conexão
conn.close()

""" 
selecionar_produtos = "SELECT * FROM produtos"

cursor.execute(selecionar_produtos)
  
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
    
conn.close() """
"""

Ao inserirmos ' OR 1=1 -- no campo username, aquery 
do código deixará de ser:

SELECT * FROM tb_user WHERE ds_email = '' AND ps_pass = ''

para se tornar:

SELECT * FROM tb_user WHERE ds_email = '' OR 1=1 -- AND ps_pass = ''

pois

1. ' fecha a string do campo ds_email
2. OR 1=1 é uma condição sempre verdadeira
3. -- comenta o restante da query (inclusive a verificação da senha)

Com isso, todos os usuários da tabela por trás da consulta SQL 
associado ao código de login do software serão exibidos, sem ao menos
precisar digitar a senha. Isso porque o banco ignora a verificação
de senha, uma vez que foi comentado na query, e simplesmente retorna
todos os registros da tabela, uma vez que, porém, OR 1=1 satisfaz
tal condição.

Para mitigar esse problema e outros, utilize queries parametrizadas.

Na linha 45, substitua por:

query = "SELECT * FROM tb_user WHERE ds_email = ? AND ps_pass = ?"

Na linha 47, acrescente:

cursor.execute(query, (username, password))

"""

import connection
import forms

localDatabase = connection.database
cursor = localDatabase.cursor()

connection.cursorTable()

def login(username, password):
    query = f"SELECT * FROM tb_user WHERE ds_email = '{username}' AND ps_pass = '{password}'"
    print("Executing query commando:", query)
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        print("You logged in!")
        for row in result:
            print(row)
    else:
        print("Failed to login")
        forms.form()
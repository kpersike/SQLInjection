import sqlite3

database = sqlite3.connect("db_empresa.db")

users = [
    {'id': 1, 'nm_username': 'Kaik', 'ds_email': 'kaik@email.com', 'ps_pass': 'kaik123'},
    {'id': 2, 'nm_username': 'Diego', 'ds_email': 'diego@email.com', 'ps_pass': 'diego321'},
    {'id': 3, 'nm_username': 'Matheus', 'ds_email': 'matheus@email.com', 'ps_pass': 'matheus123'},
    {'id': 4, 'nm_username': 'Johnathan', 'ds_email': 'johnathan@email.com', 'ps_pass': 'johnathan321'}
    ]

def cursorTable():
    
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS tb_user (" \
        "id_user," \
        "nm_username," \
        "ds_email," \
        "ps_pass)"
    )

    for i in range(0, len(users)):
        cursor.execute("INSERT INTO tb_user VALUES ('"+str(users[i]['id'])+"', '"+users[i]['nm_username']+"', '"+users[i]['ds_email']+"', '"+users[i]['ps_pass']+"')")

    database.commit()
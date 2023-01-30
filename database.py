import sqlite3

def databaseConnect(tipo, data, valor, cpf, cartao, hora, dono, nomeloja):
    column = tipo, data, valor, cpf, cartao, hora, dono, nomeloja
    con = sqlite3.connect('database.sqlite3')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS informacoes
                (tipo text, data text, valor text, cpf text, cartao text, hora text, dono text, nomeloja text)''')
    cur.execute("INSERT INTO informacoes (tipo, data, valor, cpf, cartao, hora, dono, nomeloja) VALUES (?,?,?,?,?,?,?,?)", column)
    con.commit()
    con.close()

def databaseFatch():
    con = sqlite3.connect('database.sqlite3')
    cur = con.cursor()
    result = cur.execute('SELECT * FROM informacoes').fetchall()
    cur.execute("DROP TABLE informacoes")
    con.close()
    return result

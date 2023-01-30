from datetime import date, datetime
from database import databaseConnect

def read():
    with open("CNAB.txt", encoding="UTF-8") as file:
        for line in file:
            print("Tipo: ", line[0])
            x = line[1:9]
            date = datetime.strptime(x, '%Y%m%d')
            print("Data: ", date.strftime('%Y-%m-%d'))
            # dateres = date.strftime('%Y-%m-%d')
            print("Valor: ", int(line[10:19]) / 100)
            valorRes = int(line[10:19]) / 100
            print("CPF: ", line[19:30])
            print("Cartão: ", line[30:42])
            y = line[42:48]
            time = datetime.strptime(y, '%H%M%S')
            print("Hora: ", time.strftime('%H:%M:%S'))
            # timeRes = time.strftime('%H:%M:%S')
            print("Dono da Loja: ", line[48:62])
            print("Nome da Loja: ", line[62:81])
            databaseConnect(line[0], date.strftime('%Y-%m-%d'), str(valorRes), line[19:30], line[30:42], time.strftime('%H:%M:%S'), line[48:62], line[62:81])
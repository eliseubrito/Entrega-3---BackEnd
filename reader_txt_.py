from datetime import date, datetime
from database import databaseConnect
from textwrap import wrap

def read(infos):
        temp = wrap(infos, 80)
        print(temp)
        print(len(temp))
        x = len(temp)
        for x in temp:
            # print(x)
            # print(x[0])
            # print("")
            print("Tipo: ", x[0])
            xdate = x[1:9]
            date = datetime.strptime(xdate, '%Y%m%d')
            print("Data: ", date.strftime('%Y-%m-%d'))
            # dateres = date.strftime('%Y-%m-%d')
            print("Valor: ", int(x[10:19]) / 100)
            valorRes = int(x[10:19]) / 100
            print("CPF: ", x[19:30])
            print("Cartão: ", x[30:42])
            y = x[42:48]
            time = datetime.strptime(y, '%H%M%S')
            print("Hora: ", time.strftime('%H:%M:%S'))
            # timeRes = time.strftime('%H:%M:%S')
            print("Dono da Loja: ", x[48:62])
            print("Nome da Loja: ", x[62:81])
            databaseConnect(x[0], date.strftime('%Y-%m-%d'), str(valorRes), x[19:30], x[30:42], time.strftime('%H:%M:%S'), x[48:62], x[62:81])
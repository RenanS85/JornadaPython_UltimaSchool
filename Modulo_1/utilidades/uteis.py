import sqlite3

def interface(txt):
    print('-'*90)
    print (txt.upper().center(90))
    print('-'*90)

def cabecalho (msg):
    print('~'*90)
    interface(msg.upper().center(90))
    print('~' *90)


def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (TypeError, ValueError):
            print('ERRO - Resposta inválida')
            continue
        else:
            return n

def leiaFloat (valor):
    while True:
        try:
            val = float(input(valor))
        except (ValueError,TypeError):
            print ('ERRO = DIGITE UM NUMERO INTEIRO')
            continue
        else:
            return val


def continua(txt):
    while True:
        con = str(input(txt)).strip().upper()
        if con not in 'SsNn' or con in '':
            print ('ERRO - Resposta inválida')
            continue
        elif con in 'SsNn':
            break
    return con

def connection(name):
    connection = sqlite3.connect(name)
    return connection

















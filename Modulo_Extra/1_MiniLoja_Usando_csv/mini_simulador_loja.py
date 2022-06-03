from uteis_loja.uteis_loja import *
import csv
from time import sleep

estoque = []
with open ('estoque.csv', 'r') as file:
    data = csv.DictReader(file)
    for d in data:
        if d['price']:
            d['price'] = float(d['price'])
        if d['amount']:
            d['amount'] = float(d['amount'])
        estoque.append(d)

while True:
    cabecalho('DRUMFUN: FABRICA DE DRUM KITS')
    menu = interface('1 - Vender produto\n2 - Tabela de descontos\n3 - Ver estoque\n4 - Sair')
    resposta = leiaInt('DIGITE SUA OPÇÂO: ')
    sleep(1.2)
    if resposta==1:
        print (' ')
        print('PRODUTOS DISPONIVEIS'.center(90))
        print ('=-'*45)
        c=0
        for dic in estoque:
            print (f'CÓDIGO {c} --> {dic}')
            c+=1
        print('=-' * 45)
        vender_prod(estoque)
    elif resposta==2:
        tabela_desc()
        continua('DIGITE "S" PARA VOLTAR AO MENU: ')
    elif resposta==3:
        c = 0
        for dic in estoque:
            print(f'CÓDIGO {c} --> {dic}')
            c += 1
        print('=-' * 45)
        continua('DIGITE "S" PARA VOLTAR AO MENU: ')
    elif resposta==4:
        print ('SAINDO, VOLTE SEMPRE')
        sleep(1.4)
        break

with open('estoque.csv', 'w', newline='') as file:
    w = csv.DictWriter(file, fieldnames=estoque[0].keys())
    w.writeheader()
    w.writerows(estoque)















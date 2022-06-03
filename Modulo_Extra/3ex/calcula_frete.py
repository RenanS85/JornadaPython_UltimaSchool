import csv
from Modulo_Extra.utilidades.uteis import *
from time import sleep
list = []
siglas = []
with open('rotas.csv','r') as file:
    rota = csv.DictReader(file)
    for r in rota:
        list.append(r)
        siglas.append(r['Rota'])

cabecalho('vamos calcular o valor seu pacote')
a = leiaFloat('Altura do pacote (cm): ')
c = leiaFloat('Comprimento do pacote (cm): ')
l = leiaFloat('Largura do pacote (cm): ')
p = leiaFloat('Peso do pacote (Kg): ')
volume = c*a*c
print('CALCULANDO DIMENSÕES')
sleep(2)
if 0.1 <= p < 1:
    peso = p * 1.5
elif 1 <= p < 10:
    peso = p * 1.5
elif p <= 30:
    peso = p * 2
elif p > 30:
    print ('Peso excede o limite')
    exit()
if volume < 1000:
    dimensoes = 10
elif 1000 <= volume < 10000:
    dimensoes = 20
elif 10000 <= volume < 30000:
    dimensoes = 30
elif volume >= 100000:
    print ('OPS - as dimensões ultrapassam o limite')
    exit()
print (peso)
print (dimensoes)
interface('rotas')
print('RS – De Rio de Janeiro até São Paulo\n'
      'SR – De São Paulo até Rio de Janeiro\n'
      'BS – De Brasília até São Paulo\n'	 
      'SB – De São Paulo até Brasília\n'	 
      'BR – De Brasília até Rio de Janeiro\n'
      'RB – Rio de Janeiro até Brasília')
print('')
while True:
    rota = input('Digite sua rota [SIGLA]: ').upper().strip()
    if rota not in siglas:
        print ('ERRO - DIGITE UMA ROTA VÁLIDA')
        continue
    else:
        break
for r in list:
    if r['Rota'] == rota:
        fator = int(r['Multiplicador'])

total = dimensoes*peso*fator
print (f'O valor todal é R$ {total}')



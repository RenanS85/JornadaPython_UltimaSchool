'''
OBS: Leia o enunciado!
A aplicação a sehuir foi criada para receber valores, portanto se vocÊ utilizar os valores da tabela
do enunciado, vocÊ encontrará o valor total papra o Sr. João
'''

from Modulo_1.utilidades.uteis import leiaInt

print('Olá, Sr. João, irei te ajudar a calcular sua quantia total de dinheiro!')
print('Vamos lá!')

print('')

pgt1 = (str(input('você possui moedas de 1 centavo? DIGITE: sim ou não --> ')))
if pgt1 == 'sim':
    moeda1cent = leiaInt('quantas moedas de 1 centavo você possui? DIGITE o número --> ')
else:
    moeda1cent = 0

print('')

pgt2 = (str(input('você possui moedas de 5 centavos? DIGITE: sim ou não --> ')))
if pgt2 == 'sim':
    moeda5cent = leiaInt('quantas moedas de 5 centavos você possui? DIGITE o número --> ')
else:
    moeda5cent = 0

print('')

pgt3 = (str(input('você possui moedas de 10 centavos? DIGITE: sim ou não --> ')))
if pgt3 == 'sim':
    moeda10cent = leiaInt('quantas moedas de 10 centavos você possui? DIGITE o número --> ')
else:
    moeda10cent = 0

print('')

pgt4 = (str(input('você possui moedas de 25 centavos? DIGITE: sim ou não --> ')))
if pgt4 == 'sim':
    moeda25cent = leiaInt('quantas moedas de 25 centavos você possui? DIGITE o número --> ')
else:
    moeda25cent = 0

print('')

pgt5 = (str(input('você possui moedas de 50 centavos? DIGITE: sim ou não --> ')))
if pgt5 == 'sim':
    moeda50cent = leiaInt('quantas moedas de 50 centavos você possui? DIGITE o número --> ')
else:
    moeda50cent = 0

print('')

pgt6 = (str(input('você possui moedas de 1 real? DIGITE: sim ou não --> ')))
if pgt6 == 'sim':
    moeda1real = leiaInt('quantas moedas de 1 real você possui? DIGITE o número --> ')
else:
    moeda1real = 0

print('')

print(f'Você possui {moeda1cent} moedas de 1 centavo')
print(f'Você possui {moeda5cent} moedas de 5 centavos')
print(f'Você possui {moeda10cent} moedas de 10 centavos')
print(f'Você possui {moeda25cent} moedas de 25 centavos')
print(f'Você possui {moeda50cent} moedas de 50 centavos')
print(f'Você possui {moeda1real} moedas de 1 real')

print('')

moeda01 = moeda1cent * 0.01
moeda05 = moeda5cent * 0.05
moeda10 = moeda10cent * 0.10
moeda25 = moeda25cent * 0.25
moeda50 = moeda50cent * 0.50
moeda1 = moeda1real * 1

total = moeda01 + moeda05 + moeda10 + moeda25 + moeda50 + moeda1

print('Total de R$ {:.2f}'.format(total))

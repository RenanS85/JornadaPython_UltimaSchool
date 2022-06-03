'''
Criei um programa que possua as variáveis A, B e C. Imprima o resultado de A + B caso
ele seja menor do que C, caso contrário imprima que o valor é menor.
'''
from Modulo_1.utilidades.uteis import leiaFloat

a = leiaFloat('DIGITE UM VALOR PARA A: ')
b = leiaFloat('DIGITE UM VALOR PARA B: ')
c = leiaFloat('DIGITE UM VALOR PARA C: ')

if (a + b) < c:
    print('O valor de A+B é', a + b)
else:
    print(f'Infellizmente o valor {c} é menor do que A+B = {a+b}')


'''
Crie um programa que calcule o peso ideal de uma pessoa. Para isso utilize as fórmulas:

Para Homens: (72.7 * altura) – 58
Para Mulheres: (62.1 * altura) – 44.7

Sua aplicação deve identificar se a pessoa é Homem ou Mulher e então fazer o cálculo apropriado.
Deve ser impresso se a pessoa é homem ou mulher, juntamente com o peso ideal calculado.
'''

from Modulo_1.utilidades.uteis import leiaFloat

print('Olá, vamos calcular seu peso ideal, de acordo com seu sexo.')
print('')
altura = leiaFloat('Qual a sua altura em metros?: ')
sexo = input('Digite seu sexo, masculino (M) ou feminino (F): ').upper().strip()
ideal_homem = (altura * 72.7) - 58
ideal_mulher = (altura * 62.1) - 44.7

if sexo == 'M':
    print('Para o sexo masculino, seu peso ideal é {:.2f}'.format(ideal_homem))
if sexo == 'F':
    print('Para o sexo feminino, seu peso ideal é {:.2f}'.format(ideal_mulher))

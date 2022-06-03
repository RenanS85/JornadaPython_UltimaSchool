'''
Um nutricionista está precisando de uma ajuda para calcular o IMC de seus pacientes.
Para calcular o IMC ele passou a seguinte fórmula:

IMC = peso / ( altura )².

Crie um programa que faça o cálculo do IMC de uma pessoa (ele deve ser impresso na tela)
e classifique o IMC dessa pessoa de acordo com a tabela (também deverá ser impresso):

Valor do IMC            Classificação
Abaixo de 18,5          Pessoa abaixo do peso
Entre 18,5 e 25         Pessoa com peso normal
Entre 25 e 30           Pessoa acima do peso
Acima de 30             Pessoa obesa
'''

from Modulo_1.utilidades.uteis import leiaFloat

peso = leiaFloat('Qual seu peso em kg?: ')
altura = leiaFloat('Qual a sua altura em metros?: ')
imc = (peso / (pow(altura, 2)))

print('seu imc é {:.2f}'.format(imc))

if imc < 18:
    print('você está abaixo do peso')

elif imc > 18.5:
    print('peso normal')

elif imc < 25:
    print('peso normal')

elif imc > 25:
    print('acima do peso')

elif imc < 30:
    print('acima do peso')

elif imc > 30:
    print('risco de obesidade')

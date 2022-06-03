'''
Um freelancer está com dificuldade para calcular qual o valor cobrar por um projeto que está estimado
em 80 horas. Após pensar e revisitar o preço de alguns projetos que cobrou no passado ele montou a
seguinte fórmula: valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado.
Sua tarefa é criar um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre
será 1000,00 R$ e o valor da hora cobrada é de 20,45 R$. A aplicação deve imprimir o valor calculado pelo
projeto considerando duas casas decimais na formatação do valor.
'''
from Modulo_1.utilidades.uteis import leiaInt

print('Olá, freelancer, vamos calcular o valor do seu serviço!')
hora_estimada = leiaInt('Horas estimadas: somente valor inteiro: ')
valor_inicial = 1000
valor_hora = 20.45
valor_adicional = 0.15

calculo = valor_inicial + (hora_estimada * valor_hora)
adicional = 0.15 * calculo
total = calculo + adicional

print('Olá, freelancer, vamos calcular o valor do seu serviço!')
print('')
print(f'Segundo os parâmetros de calculo, o trabalho custará {total:.2f}')

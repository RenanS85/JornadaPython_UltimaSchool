'''
5- Faça um programa com uma função que necessite de um argumento.
A função deve retornar o valor de caractere ‘P’, se seu argumento
for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''

def num (a):
    if a > 0:
        return 'P'
    if a < 0:
        return 'N'

#programa principal:
n1 = num(10)
n2 = num(-10)

print (n1)
print (n2)

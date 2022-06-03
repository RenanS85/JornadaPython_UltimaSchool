'''
6- Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.
'''

def contaLetra (letra):
    c=p.count(l)
    print (f'A letra {l} aparece {c} vezes na palavra {p}')


#programa principal:
p = input(str('Digite uma palavra ou frase: '))
l = str(input ('Digite uma letra para contar: '))
contaLetra(p)

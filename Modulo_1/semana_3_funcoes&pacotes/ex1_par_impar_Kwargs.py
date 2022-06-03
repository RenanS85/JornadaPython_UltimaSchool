'''
1- Crie uma função que, ao receber um número inteiro, retorna se um número
é par ou ímpar (utilizando **kwargs).
'''

def par_impar(**kwargs):
    for k,v in kwargs.items():
        if v%2 == 0:
            print (f'{k} é {v} e é par')
        else:
            print(f'{k} é {v} e é impar')


par_impar(n1=23, n2=1, n3 = 12, n4 =100)


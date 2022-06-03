'''
Crie de forma recursiva uma função que printe do número recebido até o zero.
'''

def regressiva (num):
    from time import sleep
    n=int(input(num))
    for c in range (n,0-1,-1):
        if c != 0:
            print (c,end='->')
        else:
            print(c)
        sleep(0.3)

#programa principal
n = regressiva('Digite um numero para ver sua contagem regressiva: ')

'''
7- Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom,
considerando 10% do valor da conta.
'''

def gorjeta (v):
    val=input(v)
    if val.isnumeric():
        val = int(val)
    taxag=0.1
    global g
    g = val*taxag
    return g

#programa principal
g =  gorjeta('Digite o valor da conta: R$ ')
print (f'O valor da gorjeta é de R$ {g:.2f}')

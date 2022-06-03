'''
3- Crie uma função de somatório que some todos os números que a mesma receber (usando *args ).
'''

def soma (*n,show_math=False):
    s=0
    for c in n:
        s+=c
    if show_math:
        c=0
        for num in n:
            if c != len(n) - 1:
                print (f'{num}+', end='')
                c+=1
            else:
                print(f'{num} = {s}')
    else:
        return s


s1 = soma (100,200,300,show_math=True)


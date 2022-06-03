'''
8-Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja um prefixo da segunda.
Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ não é prefixo de ’uf’.
'''

def prefixo(p1,p2):
    if p1 in p2 [0:]:
        print (f'{p1} é prefixo de {p2}')
    else:
        print(f'{p1} não é prefixo de {p2}')

prefixo('heli', 'helicoptero')
prefixo('helicoptero','heli')
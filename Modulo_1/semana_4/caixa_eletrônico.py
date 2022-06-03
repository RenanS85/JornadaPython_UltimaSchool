def decoracao(txt):
    deco = '*'
    print(f'\033[43m{deco * 46}\033[m')
    print(f'\033[1;40m====( {txt} )==== \033[m')
    print(f'\033[43m{deco * 46}\033[m')


dic = {}
dic['notas de 100'] = 0
dic['notas de 50'] = 0
dic['notas de 20'] = 0
dic['notas de 10'] = 0
decoracao('SEJA BEM VINDO AO BANCO DO PYTHON')
print (f'Disponiveis:')
for k in dic.keys():
    print(k)
saque = int(input('DIGITE O VALOR QUE DESEJA SACAR: '))
total = saque

while True:
    if total>=100:
        total -= 100
        dic['notas de 100'] += 1
    elif total>=50:
        total -= 50
        dic['notas de 50'] += 1
    elif total>=20:
        total -= 20
        dic['notas de 20'] += 1
    elif total>=10:
        total -= 10
        dic['notas de 10'] += 1
    if total == 0:
        break

for k,v in dic.items():
    if v !=0:
        print (f'{v} {k}')
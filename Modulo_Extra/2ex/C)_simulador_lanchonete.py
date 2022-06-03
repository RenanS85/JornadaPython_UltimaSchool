from Modulo_Extra.utilidades.uteis import *


conexao = 'lanchonete.db'
total = 0
while True:
    cabecalho("Bem vindo a lanchonete")
    print('')
    print('PRODUTOS:')
    print('')
    conn = connection(conexao)
    cur = conn.cursor()
    select = cur.execute('''select * from produtos; ''')
    show = select.fetchall()
    print(f'{"Código":^10} {"Descrição":^30} {"valor":^10}')
    print('')
    for p in show:
        print (f'{p[0]:^10} {p[1]:^30} R${p[2]:^10} ')
    print('')
    cod = int(input('Código do produto: '))
    amount = int(input('Quantidade: '))
    select = cur.execute(f'''select valor*{amount} from produtos where codigo = {cod}''')
    show = select.fetchone()
    for valor in show:
        total+=valor
    again = input('Vender mais produtos? [S/N]: ').strip().upper()
    if again == 'N':
        break

print(f'VALOR DO PEDIDO: R$ {total:.2f}')








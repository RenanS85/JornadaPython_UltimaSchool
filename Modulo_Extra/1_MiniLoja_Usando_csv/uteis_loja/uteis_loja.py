def interface(txt):
    print('-'*90)
    print (txt)
    print('-'*90)

def cabecalho (msg):
    print('~'*90)
    interface(msg.center(90))
    print('~' *90)


def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (TypeError, ValueError):
            print('ERRO - Resposta inválida')
            continue
        else:
            return n

def vender_prod(est):
    from time import sleep
    print ('Digite o código do produto para a venda')
    sale_code = leiaInt('CÓDIGO: ')
    if est[sale_code]['amount'] <= 0:
        print ('Produto indisponível')
        print ('Retornando ao menu')
        sleep(2)
    else:
        print (f'Você selecionou {est[sale_code]["name"]}')
        print (f'preço R$ {est[sale_code]["price"]:.2f}')
        unidades = leiaInt('Nº DE UNIDADES: ')
        prec_total = est[sale_code]['price'] * unidades
        if 10 < unidades <= 99:#5%
            desc1 = prec_total*0.05
            pre_desc1 = prec_total - desc1
            print (f'Valor total: R$ {pre_desc1:.2f}\n'
                   f'Desconto de 10%\n'
                   f'Economia de R% {desc1:.2f}')
        elif 100 <= unidades <= 999:
            desc2 = prec_total * 0.1
            pre_desc2 = prec_total - desc2
            print(f'Valor total: R$ {pre_desc2:.2f}\n'
                  f'Desconto de 10%\n'
                  f'Economia de R$ {desc2:.2f}')
        elif 1000 <= unidades:
            desc3 = prec_total * 0.15
            pre_desc3 = prec_total - desc3
            print(f'Valor total: R$ {pre_desc3:.2f}\n'
                  f'Desconto de 15%\n'
                  f'Economia de R$ {desc3:.2f}')
        else:
            print(f'Valor total: R$ {prec_total:2f}')
        resposta = continua('DESEJA CONCLUIR A VENDA? [S/N]: ')
        if resposta in 'Ss':
            retirada = est[sale_code]['amount'] - unidades
            est[sale_code]['amount'] = retirada
            estoque = est[:]
            print('Venda Concluida com sucesso!')
            return estoque
        else:
            print ('VENDA CANCELADA')

def tabela_desc ():
    cabecalho('TABELA DE DESCONTOS')
    print ('Unidades : acima de 10 à 99 unidades --> desconto de 5%')
    print ('Unidades : de 100 à 999 unidades --> desconto de 10%')
    print('Unidades : de 1000 em diante --> desconto de 15%')



def continua(txt):
    while True:
        con = str(input(txt)).strip().upper()
        if con not in 'SsNn' or con in '':
            print ('ERRO - Resposta inválida')
            continue
        elif con in 'SsNn':
            break
    return con
















from Modulo_2.Simulação_Fornecimeto_Loja.uteis.uteis_m2s3 import *

from Modulo_2.Simulação_Fornecimeto_Loja.uteis.utilidadesSQLITE3 import *

while True:
    file = 'sqlitesemana3B'
    conect(file)
    interface_1('MENU')
    menu('1 - Cadastrar fornecedor\n2 - Consultar cadastros\n3 - Alterar cadastros\n4 - Sair')
    resposta = input('DIGITE SUA OPÇÂO: ')
    while resposta not in '12345':
        resposta = input('ERRO - DIGITE SUA OPÇÂO VÁlIDA: ')
    if resposta == '1':
        supplier_registration(file)
    if resposta == '2':
        show_table(file)
        back_menu = input('Voltar ao MENU? [S/N]: ').upper().strip()
        while back_menu not in 'SsNn':
            back_menu = input('Voltar ao MENU? [S/N]: ').upper().strip()
            if back_menu == 'S':
                break
    if resposta == '3':
        alteration_menu(file)
    if resposta == '4':
        break









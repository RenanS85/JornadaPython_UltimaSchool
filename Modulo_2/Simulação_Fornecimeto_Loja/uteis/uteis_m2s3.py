import sqlite3
from sqlite3 import Error

def conect(arq):
    try:
        conn = sqlite3.connect(arq)
    except Error as er:
        print (er)
    else:
        print ('Conexão estabelecida')
        return conn

def interface_1 (msg):
    print('--' * 30)
    print(msg.center(60))
    print('--' * 30)

def menu (opções):
    print(opções)
    print ('--'*30)
    print ('--'*30)

def supplier_registration(connect):
    while True:
        conn=sqlite3.connect(connect)
        cur=conn.cursor()
        interface_1('CADASTRO DE FORNECEDOR ')
        name = input('NOME: ').title().strip()
        address = input('ENDEREÇO (RUA, NÚMERO) ').title().strip()
        product = input('PRODUTO: ')
        interface_1('SALVAR ALTERAÇÕES NA TABELA?')
        salvar = str(input('DIGITE S PARA SALVAR E N PARA DESCARTAR: ')).upper()
        while salvar not in 'SsNn':
            salvar = str(input('ERRO - DIGITE S PARA SALVAR E N PARA DESCARTAR: ')).upper()
        if salvar == 'S':
            cur.execute(f'''
            insert into fornecedor values
            (null,'{name}','{address}','{product}');''')
            conn.commit()
            conn.close()
        else:
            conn.close()
        continua = str(input('CADASTRAR NOVO FORNECEDOR [S/N]?: ')).upper()
        if continua == 'S':
            continue
        else:
            from time import sleep
            print ('Carregando menu')
            sleep(1.2)
            break

def alteration_menu(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    while True:
        interface_1('MENU DE ALTERAÇÃO ')
        print ('FILTRO DE BUSCA'.center(60))
        menu('1 - Mostrar tabela inteira\n2 - Buscar por id\n3 - Buscar por nome\n4 - Buscar por endereço\n5 - Menu principal')
        resposta = input('DIGITE SUA OPÇÂO: ')
        while resposta not in '12345':
            resposta = input('ERRO - DIGITE SUA OPÇÂO VÁLIDA: ')
        if resposta == '1':
            search = show_table(connect)
            if search:
                foward = input('Continuar para alteração [S/N]: ').upper().strip()
                while foward not in 'SsNn':
                    foward = input('ERRO - DIGITE SUA OPÇÂO VÁLIDA: ').upper().strip()
                type_alteration_menu()
                resposta = input('DIGITE SUA OPÇÂO: ')
                while resposta not in '1234':
                    resposta = input('ERRO - DIGITE SUA OPÇÂO VÁlIDA: ')
                if foward == 'S' and resposta == '1':
                    id_alteration(connect)
                elif foward == 'S' and resposta == '2':
                    name_alteration(connect)
                elif foward == 'S' and resposta == '3':
                    address_alteration(connect)
                elif foward == 'S' and resposta == '4':
                    product_alteration(connect)
                elif foward == 'N':
                    break
        elif resposta == '2':
            search = seach_by_id(connect)
            if search:
                foward = input('Continuar para alteração [S/N]: ').upper().strip()
                while foward not in 'SsNn':
                    foward = input('ERRO - DIGITE SUA OPÇÂO VÁLIDA: ').upper().strip()
                type_alteration_menu()
                resposta = input('DIGITE SUA OPÇÂO: ')
                while resposta not in '1234':
                    resposta = input('ERRO - DIGITE SUA OPÇÂO VÁlIDA: ')
                if foward == 'S' and resposta == '1':
                    id_alteration(connect)
                elif foward == 'S' and resposta == '2':
                    name_alteration(connect)
                elif foward == 'S' and resposta == '3':
                    address_alteration(connect)
                elif foward == 'S' and resposta == '4':
                    product_alteration(connect)
                elif foward == 'N':
                    break
        elif resposta == '3':
            search = seach_by_name(connect)
            if search:
                foward = input('Continuar para alteração [S/N]: ').upper().strip()
                while foward not in 'SsNn':
                    foward = input('ERRO - DIGITE SUA OPÇÂO VÁLIDA: ').upper().strip()
                type_alteration_menu()
                resposta = input('DIGITE SUA OPÇÂO: ')
                while resposta not in '1234':
                    resposta = input('ERRO - DIGITE SUA OPÇÂO VÁlIDA: ')
                if foward == 'S' and resposta == '1':
                    id_alteration(connect)
                elif foward == 'S' and resposta == '2':
                    name_alteration(connect)
                elif foward == 'S' and resposta == '3':
                    address_alteration(connect)
                elif foward == 'S' and resposta == '4':
                    product_alteration(connect)
                elif foward == 'N':
                    break
        elif resposta == '4':
            search = seach_by_address(connect)
            if search:
                foward = input('Continuar para alteração [S/N]: ').upper().strip()
                while foward not in 'SsNn':
                    foward = input('ERRO - DIGITE SUA OPÇÂO VÁLIDA: ').upper().strip()
                type_alteration_menu()
                resposta = input('DIGITE SUA OPÇÂO: ')
                while resposta not in '1234':
                    resposta = input('ERRO - DIGITE SUA OPÇÂO VÁlIDA: ')
                if foward == 'S' and resposta == '1':
                    id_alteration(connect)
                elif foward == 'S' and resposta == '2':
                    name_alteration(connect)
                elif foward == 'S' and resposta == '3':
                    address_alteration(connect)
                elif foward == 'S' and resposta == '4':
                    product_alteration(connect)
                elif foward == 'N':
                    break
        elif resposta == '5':
            break

def type_alteration_menu():
    print('--'*30)
    menu('1 - Alterar ID\n2 - Alterar nome\n3 - Alterar endereço\n4 - alterar produto')

def show_table(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    sql = '''select * from fornecedor;'''
    cur.execute(sql)
    result = cur.fetchall()
    if result != []:
        for r in result:
            print(f'id: {r[0]:^3} | nome: {r[1]:^30} | endereço {r[2]:^30} | produto {r[3]:^10}')
        return True
    else:
        print('Ainda não há uma tabela cadastrada')

def seach_by_id(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    while True:
        try:
            id = int(input(('Digite o ID da busca: ')))
        except (TypeError,ValueError):
            print ('Erro - Digite um número inteiro')
            continue
        else:
            sql = f'''select * from fornecedor where id = {id};'''
            cur.execute(sql)
            result = cur.fetchall()
            break
    if result !=[]:
        for r in result:
            print(f'id: {r[0]:^3} | nome: {r[1]:^30} | endereço {r[2]:^30} | produto {r[3]:^10}')
            return True
    else:
        print ('Id não encontrado')

def seach_by_name(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    nome = input(('Digite o nome: '))
    sql = f'''select * from fornecedor where nome like '{nome}%';'''
    cur.execute(sql)
    result = cur.fetchall()
    if result !=[]:
        for r in result:
            print(f'id: {r[0]:^3} | nome: {r[1]:^30} | endereço {r[2]:^30} | produto {r[3]:^10}')
        return True
    else:
        print ('Nome não localizado')

def seach_by_address(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    address = input(('Digite o endereço: '))
    sql = f'''select * from fornecedor where endereço = '%{address}%';'''
    cur.execute(sql)
    result = cur.fetchall()
    if result !=[]:
        for r in result:
            print(f'id: {r[0]:^3} | nome: {r[1]:^30} | endereço {r[2]:^30} | produto {r[3]:^10}')
        return True
    else:
        print ('Endereço não localizado')

def search_by_product(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    product = input(('Digite o produto: '))
    sql = f'''select * from fornecedor where endereço = '{product}%';'''
    cur.execute(sql)
    result = cur.fetchall()
    if result != []:
        for r in result:
            print(f'id: {r[0]:^3} | nome: {r[1]:^30} | endereço {r[2]:^30} | produto {r[3]:^10}')
            return True
    else:
        print('produto não localizado')

def id_alteration(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    while True:
        try:
            target_id = int(input('Qual ID deseja alterar: '))
        except (TypeError,ValueError):
            print('Erro - Digite um número inteiro: ')
            continue
        else:
            sql = f'''select * from fornecedor where id = {target_id}'''
            cur.execute(sql)
            result = cur.fetchall()
            print (f'Você irá alterar o ID de:\n{result}')
            certain = input('Deseja continuar? [S/N]: ').upper()
            while certain not in 'SsNn':
                certain = input('ERRO - Concluir Alteração? [S/N]: ').upper().strip()
            if certain == 'N':
                break
            if certain == 'S':
                new_id = int(input(f'Digite o novo ID para {result[0][1]}: '))
                new_id_confirm = input('Salvar alterações? [S/N]: ').upper().strip()
                while new_id_confirm not in 'SsNn':
                    new_id_confirm = input('ERRO - Salvar alterações? [S/N]: ').upper().strip()
                if new_id_confirm =='N':
                    break
                if new_id_confirm == 'S':
                    try:
                        cur.execute(f'''update fornecedor set id = {new_id} where id = {target_id}''')
                    except Error as er:
                        print (er, '--> O ID já existe')
                        cur.execute(f'''select nome from fornecedor where id = {new_id}''')
                        resul3 = cur.fetchall()
                        print(f'Tente outro ID, ou altere o id de {resul3}')
                    else:
                        print('ALTEREÇÕES REALIZADAS')
                        cur.execute(f'''select* from fornecedor where id = {new_id}''')
                        result2 = cur.fetchall()
                        print(f'ALTERAÇÂO:\n{result2}')
                        conn.commit()
                        break

def name_alteration(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    while True:
        try:
            target_id = int(input('Digite o ID do cadastro que deseja alterar: '))
        except (TypeError,ValueError):
            print('Erro - Digite um número inteiro: ')
            continue
        else:
            sql = f'''select * from fornecedor where id = {target_id}'''
            cur.execute(sql)
            result = cur.fetchall()
            print (f'Você irá alterar o nome de:\n{result}')
            certain = input('Deseja continuar? [S/N]: ').upper()
            while certain not in 'SsNn':
                certain = input('ERRO - Concluir Alteração? [S/N]: ').upper().strip()
            if certain == 'N':
                break
            if certain == 'S':
                new_name = input(f'Digite o novo nome para {result[0][1]}: ')
                new_confirm = input('Salvar alterações? [S/N]: ').upper().strip()
                while new_confirm not in 'SsNn':
                    new_confirm = input('ERRO - Salvar alterações? [S/N]: ').upper().strip()
                if new_confirm =='N':
                    break
                if new_confirm == 'S':
                    try:
                        cur.execute(f'''update fornecedor set nome = '{new_name}' where id = {target_id};''')
                    except Error as er:
                        print (er)
                        print ('OPS, houve algum erro, tente novamente ou contate seu DESENVOLVEDOR')
                    else:
                        print('ALTEREÇÕES REALIZADAS')
                        cur.execute(f'''select * from fornecedor where id = {target_id};''')
                        result2 = cur.fetchall()
                        print(f'ALTERAÇÂO:\n{result2}')
                        conn.commit()
                        break

def address_alteration(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    while True:
        try:
            target_id = int(input('Digite o ID do cadastro que deseja alterar: '))
        except (TypeError,ValueError):
            print('Erro - Digite um número inteiro: ')
            continue
        else:
            sql = f'''select * from fornecedor where id = {target_id}'''
            cur.execute(sql)
            result = cur.fetchall()
            print (f'Você irá alterar o endereço de:\n{result}')
            certain = input('Deseja continuar? [S/N]: ').upper()
            while certain not in 'SsNn':
                certain = input('ERRO - Concluir Alteração? [S/N]: ').upper().strip()
            if certain == 'N':
                break
            if certain == 'S':
                new_address = input(f'Digite o novo endereço para {result[0][1]}: ')
                new_confirm = input('Salvar alterações? [S/N]: ').upper().strip()
                while new_confirm not in 'SsNn':
                    new_confirm = input('ERRO - Salvar alterações? [S/N]: ').upper().strip()
                if new_confirm =='N':
                    break
                if new_confirm == 'S':
                    try:
                        cur.execute(f'''update fornecedor set endereço = '{new_address}' where id = {target_id}''')
                    except Error as er:
                        print ('OPS, houve algum erro, tente novamente ou contate seu DESENVOLVEDOR')
                    else:
                        print('ALTEREÇÕES REALIZADAS')
                        cur.execute(f'''select * from fornecedor where id = {target_id}''')
                        result2 = cur.fetchall()
                        print(f'ALTERAÇÂO:\n{result2}')
                        conn.commit()
                        break

def product_alteration(connect):
    conn = sqlite3.connect(connect)
    cur = conn.cursor()
    while True:
        try:
            target_id = int(input('Digite o ID do cadastro que deseja alterar: '))
        except (TypeError, ValueError):
            print('Erro - Digite um número inteiro: ')
            continue
        else:
            sql = f'''select * from fornecedor where id = {target_id}'''
            cur.execute(sql)
            result = cur.fetchall()
            print(f'Você irá alterar o produto de:\n{result}')
            certain = input('Deseja continuar? [S/N]: ').upper()
            while certain not in 'SsNn':
                certain = input('ERRO - Concluir Alteração? [S/N]: ').upper().strip()
            if certain == 'N':
                break
            if certain == 'S':
                new_product = input(f'Digite o novo produto para {result[0][1]}: ')
                new_confirm = input('Salvar alterações? [S/N]: ').upper().strip()
                while new_confirm not in 'SsNn':
                    new_confirm = input('ERRO - Salvar alterações? [S/N]: ').upper().strip()
                if new_confirm == 'N':
                    break
                if new_confirm == 'S':
                    try:
                        cur.execute(f'''update fornecedor set produto = '{new_product}' where id = {target_id}''')
                    except Error as er:
                        print('OPS, houve algum erro, tente novamente ou contate seu DESENVOLVEDOR')
                    else:
                        print('ALTEREÇÕES REALIZADAS')
                        cur.execute(f'''select * from fornecedor where id = {target_id}''')
                        result2 = cur.fetchall()
                        print(f'ALTERAÇÂO:\n{result2}')
                        conn.commit()
                        break






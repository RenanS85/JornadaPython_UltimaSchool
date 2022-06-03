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

def cadastro_pessoa(connect):
    while True:
        conn=sqlite3.connect(connect)
        cur=conn.cursor()
        interface_1('CADASTRO DE PESSOA')
        nome = str(input('Digite seu nome: ')).title().strip()
        cpf = str(input('Digite seu cpf: ')).strip().replace('.', '').replace('-', '')
        idade = int(input('Digite sua idade: '))
        sexo = str(input('Digite seu sexo: ')).upper()
        telefone = str(input('Telefone com DDD: '))
        interface_1('SALVAR ALTERAÇÕES NA TABELA?')
        salvar = str(input('DIGITE S PARA SALVAR E N PARA DESCARTAR: ')).upper()
        if salvar == 'S':
            cur.execute(f'''
            insert into pessoas values
            (null,'{nome}','{cpf}','{idade}','{sexo}','{telefone}');''')
            conn.commit()
            conn.close()
        else:
            conn.close()
        continua = str(input('CADASTRAR NOVA PESSOA [S/N]?: ')).upper()
        if continua == 'S':
            continue
        else:
            from time import sleep
            print ('Carregando menu')
            sleep(1.2)
            break

def consult_connection (connect):
    from time import sleep
    while True:
        try:
            conn = sqlite3.connect(connect)
        except Error as er:
            print(er)
        else:
            print('--'*30)
            menu('1 - Consultar todos os cadastros\n2 - Aplicar filtros\n3 - Menu principal')
            resposta = int(input('DIGITE SUA OPÇÂO: '))
            cur = conn.cursor()
            if resposta==1:
                sql='''select * from pessoas'''
                consulta = cur.execute(sql)
                resultado = cur.fetchall()
                if resultado == []:
                    print ('Ainda não há cadastros na tabela, cadastre alguem para consultar')
                    sleep(1.2)
                    break
                else:
                    for r in resultado:
                        print(f'ID: {r[0]} | Nome: {r[1]} | CPF: {r[2]} | Idade: {r[3]} | Sexo: {r[4]} | Telefone {r[5]}')
            if resposta ==2:
                menu('1 - Filtrar por nome\n2 - Filtrar por CPF\n3 - Filtrar por idade\n'
                     '4 - Filtrar por sexo\n5 - Filtrar por telefone')
                resposta1 = int(input('DIGITE SUA OPÇÂO: '))
                if resposta1 == 1:
                    busca_nome=str(input('Digite o nome, ou parte dele: '))
                    sql1 = f'''select * from pessoas where nome like '%{busca_nome}%';'''
                    consulta = cur.execute(sql1)
                    resultado1 = cur.fetchall()
                    if resultado1==[]:
                        print ('Não há resultados na busca')
                    else:
                        for r1 in resultado1:
                            print (f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                if resposta1 == 2:
                    busca_CPF = str(input('Digite o cpf, ou parte dele: '))
                    sql1 = f'''select * from pessoas where cpf like '%{busca_CPF}%';'''
                    consulta = cur.execute(sql1)
                    resultado2 = cur.fetchall()
                    if resultado2 == []:
                        print ('Não há resultados na busca')
                    else:
                        for r1 in resultado2:
                            print(f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                if resposta1 == 3:
                    busca_idade = str(input('Digite a idade: '))
                    sql1 = f'''select * from pessoas where idade like '{busca_idade}';'''
                    consulta = cur.execute(sql1)
                    resultado3 = cur.fetchall()
                    if resultado3 == []:
                        print('Não há resultados na busca')
                    else:
                        for r1 in resultado3:
                            print(
                                f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                if resposta1 == 4:
                    busca_sexo = str(input('Digite o sexo [M/F]: ')).upper()
                    sql1 = f'''select * from pessoas where sexo like '{busca_sexo}';'''
                    consulta = cur.execute(sql1)
                    resultado4 = cur.fetchall()
                    if resultado4 == []:
                        print('Não há resultados na busca')
                    else:
                        for r1 in resultado4:
                            print(f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                if resposta1 == 5:
                    busca_telefone = str(input('Digite o telefone ou parte dele: '))
                    sql1 = f'''select * from pessoas where telefone like '%{busca_telefone}%';'''
                    consulta = cur.execute(sql1)
                    resultado5 = cur.fetchall()
                    if resultado5 == []:
                        print('Não há resultados na busca')
                    else:
                        for r1 in resultado5:
                            print(f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
            if resposta == 3:
                break
        filtrar_mais = str(input('Consultar novamente? [S/N]: ')).upper()
        if filtrar_mais == 'S':
            continue
        else:
            print('Carregando menu')
            sleep(1.2)
            break

def deleta_cadastro (connect):
    from time import sleep
    while True:
        try:
            conn = sqlite3.connect(connect)
        except Error as er:
            print(er)
        else:
            print('--' * 30)
            interface_1('MENU DE DELEÇÂO')
            menu('1 - Deletar todos os registros\n2 - Deletar todos os homens\n3 - Deletar todas as mulheres\n4 - Deletar Personalizado'
                 '\n5 - Menu Principal')
            resposta = int(input('DIGITE SUA OPÇÂO: '))
            cur = conn.cursor()
            if resposta == 1:
                cur.execute('''select * from pessoas''')
                a=cur.fetchall()
                if a ==[]:
                    print ('A tabela se encontra vazia, cadastre pessoas')
                    sleep(1.2)
                    break
                else:
                    sql = '''delete from pessoas;'''
                    cur.execute(sql)
                    conn.commit()
                    print ('TODOS OS REGISTROS FORAM DELETADOS')
            if resposta == 2:
                cur.execute(''' select * from pessoas where sexo = 'M';''')
                a = cur.fetchall()
                if a == []:
                    print('Não há homens cadastrados')
                else:
                    sql = '''delete from pessoas where sexo='M';'''
                    cur.execute(sql)
                    conn.commit()
                    print('TODOS OS HOMENS FORAM DELETADOS')
            if resposta == 3:
                cur.execute(''' select * from pessoas where sexo = 'f';''')
                a = cur.fetchall()
                if a == []:
                    print('Não há mulheres cadastradas')
                else:
                    sql = '''delete from pessoas where sexo='M';'''
                    cur.execute(sql)
                    conn.commit()
                    print('TODOS AS MULEHRES FORAM DELETADAS')
            if resposta == 4:
                interface_1('FILTRO DE DELEÇÂO')
                menu('1 - Filtrar por nome\n2 - Filtrar por CPF\n3 - Filtrar por idade\n'
                     '4 - Filtrar por sexo\n5 - Filtrar por telefone')
                resposta1 = int(input('DIGITE SUA OPÇÂO: '))
                if resposta1 == 1:
                    busca_nome = str(input('Digite o nome, ou parte dele: '))
                    sql1 = f'''select * from pessoas where nome like '%{busca_nome}%';'''
                    consulta = cur.execute(sql1)
                    resultado1 = cur.fetchall()
                    if resultado1 == []:
                        print ('Não há registros na busca')
                    else:
                        for r1 in resultado1:
                            print(f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                        selecione = int(input('DIGITE O ID DO REGISTRO PARA DELETAR: '))
                        show_delete = f'''select * from pessoas where id={selecione};'''
                        show = cur.execute(show_delete)
                        resul = cur.fetchall()
                        for re in resul:
                            print('VOCÊ IRÀ DELETAR:')
                            print(f'ID: {re[0]} | Nome: {re[1]} | CPF: {re[2]} | Idade: {re[3]} | Sexo: {re[4]} | Telefone {re[5]}')
                            confirma = str(input('DELETAR CADASTRO? [S/N]: ')).upper()
                            if confirma == 'S':
                                cur.execute(f'''delete from pessoas where id={selecione};''')
                                conn.commit()
                                print ('DELETADO COM SUCESSO')
                if resposta1 == 2:
                    busca_CPF = str(input('Digite o cpf, ou parte dele: '))
                    sql1 = f'''select * from pessoas where cpf like '%{busca_CPF}%';'''
                    consulta = cur.execute(sql1)
                    resultado2 = cur.fetchall()
                    if resultado2 == []:
                        print ('Não há resultados na busca')
                    else:
                        for r1 in resultado2:
                            print(
                                f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                        selecione = int(input('DIGITE O ID DO REGISTRO PARA DELETAR: '))
                        show_delete = f'''select * from pessoas where id={selecione};'''
                        show = cur.execute(show_delete)
                        resul = cur.fetchall()
                        for re in resul:
                            print('VOCÊ IRÀ DELETAR:')
                            print(
                                f'ID: {re[0]} | Nome: {re[1]} | CPF: {re[2]} | Idade: {re[3]} | Sexo: {re[4]} | Telefone {re[5]}')
                            confirma = str(input('DELETAR CADASTRO? [S/N]: ')).upper()
                            if confirma == 'S':
                                cur.execute(f'''delete from pessoas where id={selecione};''')
                                conn.commit()
                                print('DELETADO COM SUCESSO')
                if resposta1 == 3:
                    busca_idade = str(input('Digite a idade: '))
                    sql1 = f'''select * from pessoas where idade like '{busca_idade}';'''
                    consulta = cur.execute(sql1)
                    resultado3 = cur.fetchall()
                    if resultado3 == []:
                        print ('não há resultados na busca')
                    else:
                        for r1 in resultado3:
                            print(
                                f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                        selecione = int(input('DIGITE O ID DO REGISTRO PARA DELETAR: '))
                        show_delete = f'''select * from pessoas where id={selecione};'''
                        show = cur.execute(show_delete)
                        resul = cur.fetchall()
                        for re in resul:
                            print('VOCÊ IRÀ DELETAR:')
                            print(
                                f'ID: {re[0]} | Nome: {re[1]} | CPF: {re[2]} | Idade: {re[3]} | Sexo: {re[4]} | Telefone {re[5]}')
                            confirma = str(input('DELETAR CADASTRO? [S/N]: ')).upper()
                            if confirma == 'S':
                                cur.execute(f'''delete from pessoas where id={selecione};''')
                                conn.commit()
                                print('DELETADO COM SUCESSO')
                if resposta1 == 4:
                    busca_sexo = str(input('Digite o sexo [M/F]: ')).upper()
                    sql1 = f'''select * from pessoas where sexo like '{busca_sexo}';'''
                    consulta = cur.execute(sql1)
                    resultado4 = cur.fetchall()
                    if resultado4 == []:
                        print('Não há resultados na busca')
                    else:
                        for r1 in resultado4:
                            print(
                                f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                        selecione = int(input('DIGITE O ID DO REGISTRO PARA DELETAR: '))
                        show_delete = f'''select * from pessoas where id={selecione};'''
                        show = cur.execute(show_delete)
                        resul = cur.fetchall()
                        for re in resul:
                            print('VOCÊ IRÀ DELETAR:')
                            print(
                                f'ID: {re[0]} | Nome: {re[1]} | CPF: {re[2]} | Idade: {re[3]} | Sexo: {re[4]} | Telefone {re[5]}')
                            confirma = str(input('DELETAR CADASTRO? [S/N]: ')).upper()
                            if confirma == 'S':
                                cur.execute(f'''delete from pessoas where id={selecione};''')
                                conn.commit()
                                print('DELETADO COM SUCESSO')
                if resposta1 == 5:
                    busca_telefone = str(input('Digite o telefone ou parte dele: '))
                    sql1 = f'''select * from pessoas where telefone like '%{busca_telefone}%';'''
                    consulta = cur.execute(sql1)
                    resultado5 = cur.fetchall()
                    if resultado5 == []:
                        print('Não há resultados na busca')
                    else:
                        for r1 in resultado5:
                            print(
                                f'ID: {r1[0]} | Nome: {r1[1]} | CPF: {r1[2]} | Idade: {r1[3]} | Sexo: {r1[4]} | Telefone {r1[5]}')
                        selecione = int(input('DIGITE O ID DO REGISTRO PARA DELETAR: '))
                        show_delete = f'''select * from pessoas where id={selecione};'''
                        show = cur.execute(show_delete)
                        resul = cur.fetchall()
                        for re in resul:
                            print('VOCÊ IRÀ DELETAR:')
                            print(
                                f'ID: {re[0]} | Nome: {re[1]} | CPF: {re[2]} | Idade: {re[3]} | Sexo: {re[4]} | Telefone {re[5]}')
                            confirma = str(input('DELETAR CADASTRO? [S/N]: ')).upper()
                            if confirma == 'S':
                                cur.execute(f'''delete from pessoas where id={selecione};''')
                                conn.commit()
                                print('DELETADO COM SUCESSO')
            if resposta == 5:
                break
            if resposta == 1 or resposta ==2 or resposta ==3:
                deletar_mais = str(input('Deletar mais registros? [S/N]: ')).upper()
                if deletar_mais == 'S':
                    continue
                else:
                    break
            if resposta == 4:
                deletar_mais = str(input('Deletar mais registros? [S/N]: ')).upper()
                if deletar_mais == 'S':
                    continue
                else:
                    print ('Retornando ao menu de DELEÇÂO')
                    sleep(1.2)


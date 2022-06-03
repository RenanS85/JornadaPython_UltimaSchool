from Modulo_Extra.utilidades.uteis import *

class Peca:
    def __init__(self,id,nome,fabricante):
        self.id = id
        self.nome = nome
        self.fabricante = fabricante
id = 1
estoque = []
while True:
    cabecalho('bicicletaria show de roda')
    print ('1 - Cadastrar produto\n2 - Consultar produtos\n3 - Apagar peça\n4 - Sair')
    while True:
        resp = leiaInt('Digite a opção: ')
        if 1 > resp > 4:
            continue
        else:
            break
    if resp == 1:
        while True:
            nome = input('Nome da peça: ').strip().title()
            fabricante = input('Nome do fabricante: ').strip().title()
            peca = Peca(id,nome,fabricante)
            id+=1
            estoque.append(peca.__dict__)
            add_more = input('Adicionar mais peças: ').strip().upper()
            if add_more == 'N':
                break
    elif resp == 2:
        if estoque == []:
            print ('OPS - SEM PRODUTS CADASTRADOS')
        else:
            print('1 - Todos\n2 - Filtrar por id\n3 - Filtrar por nome\n4 - Filtrar por fabricante\n5 - Voltar')
            while True:
                resp = leiaInt('Digite a opção: ')
                if 1 > resp > 5:
                    continue
                else:
                    break
            if resp == 1:
                print (f'{"id":^10} {"nome":^20} {"fabricante":^20}')
                for p in estoque:
                    print (f'{p["id"]:^10} {p["nome"]:^20} {p["fabricante"]:^20}')
            elif resp == 2:
                    id_busca = leiaInt('ID: ')
                    for peca in estoque:
                        if id_busca == peca['id']:
                            p = peca
                    if p == peca:
                        print(f'{"id":^10} {"nome":^20} {"fabricante":^20}')
                        print(f'{p["id"]:^10} {p["nome"]:^20} {p["fabricante"]:^20}')
                    else:
                        print ('ID NAO ENCONTRADO')
            elif resp == 3:
                nome = input('NOME DA PEÇA: ').title().strip()
                nomes_buscados = []
                for peca in estoque:
                    if nome == peca['nome']:
                        nomes_buscados.append(peca)
                if nomes_buscados != []:
                    print(f'{"id":^10} {"nome":^20} {"fabricante":^20}')
                    for p in nomes_buscados:
                        print(f'{p["id"]:^10} {p["nome"]:^20} {p["fabricante"]:^20}')
                else:
                    print('NOME NAO ENCONTRADO')
            elif resp == 4:
                fabricante = input('NOME DO FABRICANTE: ').title().strip()
                fabr_buscados = []
                for peca in estoque:
                    if fabricante == peca['fabricante']:
                        fabr_buscados.append(peca)
                if fabr_buscados != []:
                    print(f'{"id":^10} {"nome":^20} {"fabricante":^20}')
                    for p in fabr_buscados:
                        print(f'{p["id"]:^10} {p["nome"]:^20} {p["fabricante"]:^20}')
                else:
                    print('FABRICANTE NAO ENCONTRADO')
    elif resp ==3:
        if estoque == []:
            print ('OPS - SEM PRODUTS CADASTRADOS')
        else:
            print('A peça será apagada pelo seu id, vá em consultar peças primeiro')
            print('Se não sabe o idd, digite 999 para retornar ao menu')
            deleta = leiaInt('ID da peça que deseja apagar: ')
            if deleta == 999:
                continue
            for peca in estoque:
                if peca['id'] == deleta:
                    estoque.remove(peca)
                    print('Peça removida com sucesso!')
    elif resp == 4:
        exit()













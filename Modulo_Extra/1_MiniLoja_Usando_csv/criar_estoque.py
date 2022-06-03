import csv
from os.path import isfile

class Produto:
    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

def dic_obj(obj):
    return obj.__dict__

exist_file = isfile("../../pacotes/Modulo_Extra_UltimaSchool/modulo extra/01_mini_loja_com_csv/estoque.csv")
columns = ['nome','preco','quantidade']
estoque = []
while True:
    print('CADASTRO DE PRODUTO')
    name = input('NOME: ').strip().title()
    price = input('PREÇO: ')
    amount = input('QUANTIDADE')
    produto = Produto(name,price,amount)
    dictionary = dic_obj(produto)
    estoque.append(dictionary)
    again = input("CADASTRAR MAIS PRODUTOS? [S/N]").upper().strip()
    if again == 'N':
        break
if not exist_file:
    with open('estoque.csv', 'w', newline='') as file:
        w = csv.DictWriter(file, fieldnames=dictionary.keys())
        w.writeheader()
        w.writerows(estoque)
if exist_file:
    with open('estoque.csv', '+a', newline='') as file:
        w = csv.DictWriter(file, fieldnames=dictionary.keys())
        w.writerows(estoque)





















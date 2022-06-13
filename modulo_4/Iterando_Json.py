import requests

r = requests.get("https://parallelum.com.br/fipe/api/v2/cars/brands", headers={'user-agent': 'my-app'})
j_file = r.json()


for brands in j_file:
    print (f'Brand: {brands["name"]:^20} | Code: {brands["code"]:^5}')
print('')
brand = input('Escolha o código da marca: ')


r = requests.get(f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{brand}/modelos", headers={'user-agent': 'my-app'})
j_file = r.json()
print(j_file)
print('')
for v in j_file.values():
    for dic in v:
        print(f'Modelo: {dic["nome"]:^20} | Codigo: {dic["codigo"]:^5}')
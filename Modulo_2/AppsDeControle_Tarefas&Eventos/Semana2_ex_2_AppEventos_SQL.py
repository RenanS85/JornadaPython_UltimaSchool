from funcoes_sql.funcoes_sqlite import SqlManager

def show_organizadores():
    cat = manger.show_all('organizadores', conn_status=True)
    print(f'{"id":^10} {"nome":^20} {"cpf":^20} {"email":^20}')
    for c in cat:
        print(f'{c[0]:^10} {c[1]:^20} {c[2]:^20} {c[3]:^20}')

manger = SqlManager('controle_eventos')

"""
manger.edit_db('''create table organizadores(
id integer not null primary key autoincrement,
nome varchar (120),
cpf text(11) not null unique,
email varchar(250));''')

manger.edit_db('''create table eventos(
id integer not null primary key autoincrement,
id_organizador integer,
titulo varchar (120) not null unique,
data varchar (20),
local varchar (300),
foreign key (id_organizador) references organizadores (id));''')
"""

while True:
    while True:
        menu = input('1 - add organizador\n2 - add evento\n3 - sair\n'
                     'RESPOSTA: ')

        if menu == '1':
            while True:
                nome = input('Nome: ')
                cpf = input('CPF: ')
                email = input('Email: ')
                manger.edit_db(f''' insert into organizadores values (
                null, "{nome}", "{cpf}", "{email}"); ''')
                again = input('add mais organizadores? [S/N]: ').upper().strip()
                if again == 'S':
                    continue
                else:
                    break

        if menu == '2':
            while True:
                show_organizadores()
                id_organizador = input('ID Organizador: ')
                titulo = input('Titulo do evento: ')
                data = input('data do evento (AAAA-MM_DD): ')
                local = input('Endereço do evento: : ')
                manger.edit_db(f''' insert into eventos values (
                null, {id_organizador}, "{titulo}", "{data}", "{local}"); ''')
                again = input('add mais eventos? [S/N]: ').upper().strip()
                if again == 'S':
                    continue
                else:
                    break
        if menu == '3':
            exit()




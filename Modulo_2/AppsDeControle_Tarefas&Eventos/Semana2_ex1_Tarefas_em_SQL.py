from funcoes_sql.funcoes_sqlite import SqlManager

def show_categories():
    cat = manager.show_all('categorias', conn_status=True)
    print(f'{"id":^10} {"nome":^20}')
    for c in cat:
        print(f'{c[0]:^10} {c[1]:^10}')

def filter(ForeignKey, OriginForeignKey, TableColumn=None, Filter=None):
    connection = manager.create_connection(show_status=True)
    cur = connection.cursor()
    if Filter:
        select = cur.execute(f''' 
                SELECT t.id , t.tarefa, c.nome as categoria , t.concluido
                from tarefas t , categorias c 
                where {ForeignKey}= {OriginForeignKey} and {TableColumn} like "{Filter}%";''')
    elif not Filter:
        select = cur.execute(f''' 
                SELECT t.id , t.tarefa, c.nome as categoria , t.concluido  
                from tarefas t , categorias c 
                where {ForeignKey} = {OriginForeignKey};''')
    show = select.fetchall()
    print(f'{"id":^10} {"tarefa":^20} {"categoria":^20} {"concluido":^20}')
    for t in show:
        print(f'{t[0]:^10} {t[1]:^20} {t[2]:^20} {t[3]:^20}')

def set_concluded(target_id):
    connection = manager.create_connection(show_status=True)
    cur = connection.cursor()
    select = cur.execute(f'''
            update tarefas set concluido = "sim" where id = {target_id}''')
    connection.commit()
    connection.close()

manager = SqlManager('controle_tarefas')

"""manager.edit_db('''CREATE table categorias(
id integer not null primary key autoincrement,
nome varchar(95));''',conn_status=True)"""

"""manager.edit_db('''CREATE table tarefas(
id integer not null primary key autoincrement,
tarefa varchar(100),
id_categoria integer not null,
data varchar(20),
concluido varchar(3),
foreign key (id_categoria) references categorias(id));
''',conn_status=True)"""

while True:
    menu = input('1 - add categoria\n2 - add tarefas\n3 - marcar tareda concluida\n4 - SAir\n'
                 'RESPOSTA: ')
    if menu == '1':
        while True:
            nome = input('nome da categoria').strip().title()
            manager.edit_db(f'''insert into categorias values (
            null,"{nome}");''')
            again = input('add mais categorias? [S/N]: ').upper()
            if again == 'S':
                continue
            else:
                break
    if menu == '2':
        while True:
            nome = input('nome da tarefa').strip().title()
            data = input('data - AAAA-MM-DD').strip().title()
            concluida = input('Concluida: [S/N]').strip().title()
            show_categories()
            categoria = int(input('ID da categoria: '))
            manager.edit_db(f'''insert into tarefas values (
            null, "{nome}",{categoria} ,"{data}", "{concluida}" );''')
            again = input('add mais tarefas? [S/N]: ').upper().strip()
            if again == 'S':
                continue
            else:
                break
    if menu == '3':
        submenu = input('1 - ver todas\n2 - filtrar por id\n3 - filtrar por categoria\n'
                        '4filtrar por nome\n5 - filtrar por data\n6 - Voltar\n'
                     'RESPOSTA: ')
        if submenu == '1':
            filter('t.id_categoria', 'c.id')
            id_for_change = int(input('ID da tarefa que deseja concluir: '))
            set_concluded(id_for_change)
        if submenu == '2':
            target_id = int(input('ID da tarefa: '))
            filter('t.id_categoria','c.id', 't.id', Filter=target_id)
            id_for_change = int(input('ID da tarefa que deseja concluir: '))
            set_concluded(id_for_change)
        if submenu == '3':
            category_name = input('Nome da categoria: ')
            filter('t.id_categoria', 'c.id', TableColumn='c.nome', Filter= category_name)
            id_for_change = int(input('ID da tarefa que deseja concluir: '))
            set_concluded(id_for_change)
        if submenu == '4':
            name = input('Nome da tarefa: ')
            filter('t.id_categoria', 'c.id', TableColumn='t.tarefa', Filter= name)
            id_for_change = int(input('ID da tarefa que deseja concluir: '))
            set_concluded(id_for_change)
        if submenu == '5':
            data = input('data da tarefa: ')
            filter('t.id_categoria', 'c.id', TableColumn='t.data', Filter= data)
            id_for_change = int(input('ID da tarefa que deseja concluir: '))
            set_concluded(id_for_change)

















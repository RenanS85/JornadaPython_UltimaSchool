import sqlite3
from os.path import isfile

class SqlManager:
    def __init__(self,conn_name):
        if '.db' not in conn_name:
            self.conn_name = f'{conn_name}.db'
        else:
            self.conn_name = conn_name

    def create_connection(self,show_status=False):
        if show_status:
            if isfile(self.conn_name):
                print(f'Conectando-se a conexão "{self.conn_name}" existente...')
            else:
                print(f'Criando nova conexão "{self.conn_name}" com db...')
        connection = sqlite3.connect(self.conn_name)
        return connection

    def edit_db(self,sql_txt,conn_status=False):
        connection = self.create_connection(show_status=conn_status)
        self.connected = True
        cur = connection.cursor()
        cur.execute(sql_txt)
        connection.commit()
        connection.close()

    def select_db(self,table,column,data,conn_status=False):
        connection = self.create_connection(show_status=conn_status)
        self.connected = True
        cur = connection.cursor()
        result = cur.execute(f'''
        
        select * from "{table}" where "{column}" like "{data}%";''')
        show = result.fetchall()
        return show

    def show_all(self,table,conn_status=False):
        connection = self.create_connection(show_status=conn_status)
        cur = connection.cursor()
        result = cur.execute(f'''select * from "{table}";''')
        show = result.fetchall()
        return show


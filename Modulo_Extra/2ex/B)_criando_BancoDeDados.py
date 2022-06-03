import sqlite3

connection = sqlite3.connect('lanchonete.db')
cur = connection.cursor()

cur.execute('''
create table produtos (
codigo integer not null primary key,
descricao varchar(70),
valor real);''')

cur.execute('''
insert into produtos values
(100,"Cachorro-Quente",9.00),
(101,"Cachorro-Quente Duplo",11.00),
(102, "X-Egg", 12.00),
(103, "X-Salada", 13.00),
(104,"X-Bacon", 14.00),
(105, "X-Tudo", 17.00),
(200, "Refrigerante Lata", 5.00),
(201, "Chá Gelado",4.00);
''')
connection.commit()
connection.close()


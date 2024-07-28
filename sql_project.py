from typing import List
# import pandas as pd
# import sqlalchemy as sa
# class Sql:
#     def __init__(self,server,database,user_name,password):
#         self.connection=f'mssql+pyodbc://{user_name}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
#     def show(self,comment):
#         engine=sa.create_engine(self.connection)
#         dataframe=pd.read_sql(comment,engine)
#         print(dataframe)
# def menu():
#     print('create your own SQL Database ')
#     print('press 1 to connect your sql server and database')
#     print('press 2 to exit')
#
# while True:
#     print(menu())
#     choice=int(input('enter your choice'))
#     if choice==1:
#         server=input('enter your name of your Sql sever EX://KEERTHANA\MSSQLSERVER01')
#         database=input('select your database')
#         user_name=input('enter your user_name')
#         password=input('enter your SQl sever password')
#         comment=input('enter your comment')
#         sachin = Sql(server,database,user_name,password)
#         sachin.show(comment)
#     if choice==2:
#         print('invalid data')
#         break
#
#
# import pandas as pd
# import sqlalchemy as sa
# class Sql:
#     def __init__(self,server,database):
#         self.connection=f'mssql+pyodbc:{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
#     def show(self,comment):
#         engine=sa.create_engine(self.connection)
#         dataframe=pd.read_sql(comment,engine)
#         print(dataframe)
# def menu():
#     print('create your own SQL Database ')
#     print('press 1 to connect your sql server and database')
#     print('press 2 to exit')
#
# while True:
#     print(menu())
#     choice=int(input('enter your choice'))
#     if choice==1:
#         server=input('enter your name of your Sql sever EX://KEERTHANA\MSSQLSERVER01')
#         database=input('select your database')
#         comment=input('enter your comment')
#         sachin = Sql(server,database)
#         sachin.show(comment)
#     if choice==2:
#         print('invalid data')
#         break
from typing import List
import pandas as pd
import pyodbc
class Sql:
    def __init__(self, server, database, user_name, password):
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                         f'SERVER={server};'
                                         f'DATABASE={database};'
                                         f'UID={user_name};'
                                         f'PWD={password}')

    def show(self, comment):
        cursor = self.connection.cursor()
        cursor.execute(comment)
        dataframe = cursor.fetchall()
        for data in dataframe:
            df = (list(data))
            print(df)


def menu1():
    print('create your own SQL Database ')
    print('press 1 to connect your sql server and database')
    print('press 2 to exit')


def menu2():
    print('to insert your data in table press 1')
    print('to select a table press 2')
    print('to update a your name or any press 3')
    print('to delete any data or cell press 4')


while True:
    print(menu1())
    choice = int(input('enter your choice'))
    if choice == 1:
        server = input('enter your name of your SQL sever EX://- KEERTHANA\MSSQLSERVER01')
        database = input('select your database - sachin')
        user_name = input('enter your user_name - sa')
        password = input('enter your SQl server password - Sachin$00')
        sachin = Sql(server, database, user_name, password)
        print('sever connected')
        while True:
            print(menu2())
            choice = int(input('enter your choice'))
            if choice == 1:
                name = input('enter a name')
                age = int(input('enter your age'))
                mail = input('enter your mailid')
                cursor = sachin.connection.cursor()
                # cursor.execute(f'insert into studentdata (id,name,age,mail) values ({name},{age},{mail})')
                cursor.execute('INSERT INTO studentdata (name, age, mail) VALUES (?, ?, ?)', (name, age, mail))
                sachin.connection.commit()
                print('data inserted in database')
                break
    elif choice == 2:
        print('Exited')
        break
    else:
        print('make a correct input')
        break









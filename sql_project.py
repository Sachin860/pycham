import pandas as pd
import sqlalchemy as sa
class Sql:
    def __init__(self,server,database):
        self.connection=f'mssql+pyodbc:{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
    def show(self,comment):
        engine=sa.create_engine(self.connection)
        dataframe=pd.read_sql(comment,engine)
        print(dataframe)
def menu():
    print('create your own SQL Database ')
    print('press 1 to connect your sql server and database')
    print('press 2 to exit')

while True:
    print(menu())
    choice=int(input('enter your choice'))
    if choice==1:
        server=input('enter your name of your Sql sever EX://KEERTHANA\MSSQLSERVER01')
        database=input('select your database')
        comment=input('enter your comment')
        sachin = Sql(server,database)
        sachin.show(comment)
    if choice==2:
        print('invalid data')
        break












# Instalar o pacote: pip install mysql-connector-python
# GRANT ALL PRIVILEGES ON * . * TO 'root'@'localhost';

from getpass import getpass
from multiprocessing import connection
from mysql.connector import connect, Error


def criar_exibir_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: ')
        ) as connection:
            #print(connection) # Mensagem de retorno da conexão
            # Criar BD a partir do VS
            query= "create database online_movie_rating" 
            with connection.cursor() as cursor:
                cursor.execute(query)

            # Consultar as bases de dados existente
            sql="show databases"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)

def criar_table_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating', # Conexão com um banco de dados específico
        ) as connection:
            # Comando para criar a table de filme
            sql_filme=""" 
            create table filme ( 
                id int auto_increment primary key,
                titulo varchar(100),
                ano_lancamento year,
                genero varchar(100),
                arrecadacao_em_mil int
            )"""
            # Comando para criar a table de revisor
            sql_revisor=""" 
            create table revisor ( 
                id int auto_increment primary key,
                primeiro_nome varchar(100),
                segundo_nome varchar(100)  
            )    
            """
            # Comando para criar a table de ranking
            sql_ranking=""" 
            create table ranking ( 
                id_filme int,
                id_revisor int,
                rate decimal(5,2),
                FOREIGN KEY(id_filme) references filme(id),
                FOREIGN KEY(id_revisor) references revisor(id),
                primary key(id_filme,id_revisor)
            ) """
            with connection.cursor() as cursor:
                cursor.execute(sql_filme)
                cursor.execute(sql_revisor)
                cursor.execute(sql_ranking)
                connection.commit()

    except Error as e:
        print(e)

def alterar_table_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            sql="alter table filme modify column arrecadacao_em_mil decimal(4,1)"
            with connection.cursor() as cursor:
                cursor.execute(sql)
    except Error as e:
        print(e)

def drop_table_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            sql="drop table filme"
            with connection.cursor() as cursor:
                cursor.execute(sql)
    except Error as e:
        print(e)

def inserir_dados_table_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            insert_filme="""insert into filme (titulo,ano_lancamento, genero, arrecadacao_em_mil) values 
            ('Forrest Gump', 1994, 'Drama', 330.2),
            ('3 Idiots', 2009, 'Drama', 2.4),
            ('Eternal Sunshine of the Spotless Mind', 2004, 'Drama', 34.5),
            ('Good Will Hunting', 1997, 'Drama', 138.1),
            ('Skyfall', 2012, 'Action', 304.6),
            ('Gladiator', 2000, 'Action', 188.7),
            ('Black', 2005, 'Drama', 3.0),
            ('Titanic', 1997, 'Romance', 659.2),
            ('The Shawshank Redemption', 1994, 'Drama',28.4),
            ('Udaan', 2010, 'Drama', 1.5),
            ('Home Alone', 1990, 'Comedy', 286.9),
            ('Casablanca', 1942, 'Romance', 1.0),
            ('Avengers: Endgame', 2019, 'Action', 858.8),
            ('Night of the Living Dead', 1968, 'Horror', 2.5),
            ('The Godfather', 1972, 'Crime', 135.6),
            ('Haider', 2014, 'Action', 4.2),
            ('Inception', 2010, 'Adventure', 293.7),
            ('Evil', 2003, 'Horror', 1.3),
            ('Toy Story 4', 2019, 'Animation', 434.9),
            ('Air Force One', 1997, 'Drama', 138.1),
            ('The Dark Knight', 2008, 'Action',535.4),
            ('Bhaag Milkha Bhaag', 2013, 'Sport', 4.1),
            ('The Lion King', 1994, 'Animation', 423.6),
            ('Pulp Fiction', 1994, 'Crime', 108.8),
            ('Kai Po Che', 2013, 'Sport', 6.0),
            ('Beasts of No Nation', 2015, 'War', 1.4),
            ('Andadhun', 2018, 'Thriller', 2.9),
            ('The Silence of the Lambs', 1991, 'Crime', 68.2),
            ('Deadpool', 2016, 'Action', 363.6),
            ('Drishyam', 2015, 'Mystery', 3.0)"""

            insert_revisor="""
            insert into revisor (primeiro_nome, segundo_nome) values
            ('Chaitanya','Baweja'),
            ('Mary','Cooper'),
            ('John','Wayne'),
            ('Thomas','Stoneman'),
            ('Penny','Hofstadter'),
            ('Mitchell','Marsh'),
            ('Wyatt','Skaggs'),
            ('Andre','Veiga'),
            ('Sheldon','Cooper'),
            ('Kimbra','Masters'),
            ('Kat','Dennings'),
            ('Bruce','Wayne'),
            ('Domingo','Cortes'),
            ('Rajesh','Koothrappali'),
            ('Ben','Glocker'),
            ('Mahinder','Dhoni'),
            ('Akbar','Khan'),
            ('Howard','Wolowitz'),
            ('Pinkie','Petit'),
            ('Gurkaran','Singh'),
            ('Amy','Farah Fowler'),
            ('Marlon','Crafford')"""

            with connection.cursor() as cursor:
                cursor.execute(insert_filme)
                cursor.execute(insert_revisor)
                connection.commit()
    except Error as e:
        print(e)
def inserir_dados_table_bd_2 ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            insert_ranking=""" insert into ranking (rate,id_filme,id_revisor) values
            (6.4, 17, 5), (5.6, 19, 1), 
            (6.3, 22, 14), (5.1, 21, 17),
            (5.0, 5, 5), (6.5, 21, 5), 
            (8.5, 30, 13), (9.7, 6, 4),
            (8.5, 24, 12), (9.9, 14, 9), 
            (8.7, 26, 14), (9.9, 6, 10),
            (5.1, 30, 6), (5.4, 18, 16), 
            (6.2, 6, 20), (7.3, 21, 19),
            (8.1, 17, 18), (5.0, 7, 2), 
            (9.8, 23, 3), (8.0, 22, 9),
            (8.5, 11, 13), (5.0, 5, 11), 
            (5.7, 8, 2), (7.6, 25, 19),
            (5.2, 18, 15), (9.7, 13, 3), 
            (5.8, 18, 8), (5.8, 30, 15),
            (8.4, 21, 18), (6.2, 23, 16), 
            (7.0, 10, 18), (9.5, 30, 20),
            (8.9, 3, 19), (6.4, 12, 2), 
            (7.8, 12, 22), (9.9, 15, 13),
            (7.5, 20, 17), (9.0, 25, 6), 
            (8.5, 23, 2), (5.3, 30, 17),
            (6.4, 5, 10), (8.1, 5, 21), 
            (5.7, 22, 1), (6.3, 28, 4),
            (9.8, 13, 1)
            """

            with connection.cursor() as cursor:
                cursor.execute(insert_ranking)
                connection.commit()
    except Error as e:
        print(e)

def select_todas_colunas_table_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            sql = "select * from filme limit 2,5" # Inicia no terceiro registro e lista cinco linhas

            with connection.cursor() as cursor:
                cursor.execute(sql)
                resultado=cursor.fetchall()
                for linha in resultado:
                    print(linha)
    except Error as e:
        print(e)

def select_algumas_colunas_table_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            sql = "select titulo, ano_lancamento from filme limit 5"

            with connection.cursor() as cursor:
                cursor.execute(sql)
                for linha in cursor.fetchall():
                    print(linha)
    except Error as e:
        print(e)

def select_where_table_bd ():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            sql = """select titulo, arrecadacao_em_mil 
            from filme
            where arrecadacao_em_mil> 300
            order by arrecadacao_em_mil desc"""

            with connection.cursor() as cursor:
                cursor.execute(sql)
                for linha in cursor.fetchall():
                    print(linha)
    except Error as e:
        print(e)

def select_limit_colunas_table_bd ():        
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating',
        ) as connection:
            sql = """
            select concat(titulo, "(", ano_lancamento, ")" ), arrecadacao_em_mil 
            from filme
            order by arrecadacao_em_mil desc
            limit 5
            """

            with connection.cursor() as cursor:
                cursor.execute(sql)
                for linha in cursor.fetchall(): # retorna todos os itens da tabela em um lista
                    print(linha)
    except Error as e:
        print(e)

def select_limitar_colunas_table_bd():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating'
        ) as connection:
            sql="""
            select concat(titulo, '(', ano_lancamento, ')'), arrecadacao_em_mil
            from filme
            order by arrecadacao_em_mil desc
            """
            with connection.cursor() as cursor:
                cursor.execute(sql)
                for filme in cursor.fetchmany(size=5): # Retorna uma lista com um número limitado de itens, neste caso 5
                    print(filme)
                cursor.fetchall()
                # É necessário limpar todos os resultados não lidos antes de executar qualquer outra instrução na mesma conexão.
                # Caso contrário, uma InternalError: Unread result foundexceção será gerada
    except Error as e:
        print(e)

def select_join_table_bd():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating'
        ) as connection:
            sql="""
            select titulo, avg(rate) as media_rate
            from ranking
            inner join filme 
                on filme.id=ranking.id_filme
            group by id_filme
            order by media_rate desc
            limit 5
            """
            with connection.cursor() as cursor:
                cursor.execute(sql)
                for filme in cursor.fetchall():
                    print(filme)
    except Error as e:
        print(e)

def update_table_db():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating'
        ) as connection:
            sql="""
            update revisor
            set segundo_nome='Cooper'
            where primeiro_nome='Amy'
            """
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
    except Error as e:
        print(e)

def delete_table_db():
    try:
        with connect(
            host='localhost',
            user=input('Entre com o usuário: '),
            password=getpass('Digite a senha: '),
            database='online_movie_rating'
        ) as connection:
            sql="""
            delete
            from ranking
            where id_revisor='2'
            """
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
    except Error as e:
        print(e)


#CHAMANDO AS FUNÇÕES
#criar_exibir_bd()
#criar_table_bd()
#inserir_dados_table_bd()
#inserir_dados_table_bd_2()
#select_todas_colunas_table_bd()
#select_algumas_colunas_table_bd()
#select_where_table_bd()
#select_limit_colunas_table_bd()
#select_join_table_bd()
#update_table_db()
#delete_table_db()
import psycopg2
from config import HOST, DATABASE, USER, PASSWORD
from pprint import pprint
import json

connection = psycopg2.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
connection.autocommit = True

def apts_collecting():
    with open ('apts_list.json', 'r') as file:
        apts_list = json.load(file)
        return apts_list

def db_start():
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
            DROP TABLE IF EXISTS flats;
            CREATE TABLE IF NOT EXISTS flats(
            pk_flat_id int PRIMARY KEY,
            flat_id int NOT NULL,
            price float NOT NULL,
            address text NOT NULL,
            fl_type text NOT NULL,
            link text NOT NULL)            
            ''')
        print('[INFO-SQL-STARTER] Table successfully started')
    except Exception as e:
        print(f'[SQL-ERROR] Something went wrong... look: *{e}*')
    finally:
        connection.close()
        print('[SQL] Connection successfully closed')

def db_filling_from_json(list):
    try:
        i = 1
        with connection.cursor() as cursor:
            for key, value in list.items():
                cursor.execute('''
                            INSERT INTO flats(pk_flat_id, flat_id, price, address, fl_type, link)
                            VALUES (%s, %s, %s, %s, %s, %s)''',(i, key, value['Цена'], value['Локация'], value['Тип'], value['Ссылка'])
                            )
                i += 1

    except Exception as e:
        print(f'[SQL-ERROR] Something went wrong... look: *{e}*')
    finally:
        connection.close()
        print('[SQL] Connection successfully closed')

def checking():
    try:
        with connection.cursor() as cursor:
            cursor.execute('''
            SELECT *
            FROM flats''')
            pprint(cursor.fetchall())
    except Exception as e:
        print(f'[SQL-CHECKING-ERROR] Something went wrong... look: *{e}*')
    finally:
        connection.close()
        print('[SQL] Connection successfully closed')

def collecting_from_db():
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT flat_id
        FROM flats
        ''')
        id_list = [row[0] for row in cursor.fetchall()]
    return id_list



if __name__ == '__main__':
#    db_start()
#    checking()
#    db_filling_from_json(apts_collecting())
#    collecting_from_db()
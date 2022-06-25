from venv import create
from django.db import connection
import psycopg2
from config import config
from psycopg2 import Error
def add_row_db(arr):
    conn = None
    try:
        params = config() #get parameter for connection
        
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)#connect to Postgre server

        add_row = '''INSERT INTO review(url,store_name,review1,review2,review3,review4,review5) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        cur = conn.cursor()
        cur.execute(add_row, (arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6]))
        conn.commit()
        
        conn.close()#close communication with Postgre server
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def create_table():
    conn = None
    try:
        params = config() #get parameter for connection
        
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)#connect to Postgre server

        create_table_query = '''CREATE TABLE review
        (url TEXT NOT NULL,
        store_name TEXT NOT NULL,
        review1 TEXT NOT NULL,
        review2 TEXT NOT NULL,
        review3 TEXT NOT NULL,
        review4 TEXT NOT NULL,
        review5 TEXT NOT NULL);'''
        cur = conn.cursor()
        cur.execute(create_table_query)
        conn.commit()
        
        conn.close()#close communication with Postgre server
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
create_table()
import psycopg2
from config import config

def connect():
    conn = None
    try:
        params = config() #get parameter for connection
        
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)#connect to Postgre server

        cur = conn.cursor()#create a cursor
        
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')#execute a statement for printing version

        db_version = cur.fetchone()# display the PostgreSQL database server version
        print(db_version)
       
        cur.close()#close communication with Postgre server
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
connect()
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    user = 'postgres',
    password = '232323',
)

cur=conn.cursor()
conn.autocommit=True

cur.execute('DROP DATABASE if exists restaurant_mm;')
cur.execute('CREATE DATABASE restaurant_mm;')

cur.close()
conn.close()

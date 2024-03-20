import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    user = 'postgres',
    password = '232323',
    dbname = 'restaurant_mm'
)

cur=conn.cursor()
conn.autocommit=True


cur.execute('DROP TABLE if exists menu_items')
create_table ="""
    CREATE TABLE menu_items(
    item_id serial primary key,
    item_name varchar(30) not null,
    item_price smallint default 0
    )
"""
cur.execute(create_table)

cur.close()
conn.close()
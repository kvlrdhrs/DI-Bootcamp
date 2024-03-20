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


class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        cur.execute("""SELECT * FROM menu_items WHERE item_name = %s""", (name,))
        result = cur.fetchone()
        return result if result else None

    @classmethod
    def all_items(cls):
        cur.execute("""SELECT * FROM menu_items""")
        return cur.fetchall()


# item2 = MenuManager.get_by_name('Beef Stew')
# items = MenuManager.all_items()
# print(item2)
# print(items)
cur.close()
conn.close()
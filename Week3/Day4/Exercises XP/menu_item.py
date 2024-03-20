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



class MenuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def save(self):
        cur.execute("""INSERT INTO menu_items (item_name, item_price) values(%s, %s);""", (self.name, self.price))

    def delete (self):
        cur.execute("""DELETE FROM menu_items WHERE item_name = %s and item_price = %s""", (self.name, self.price))


    def update(self, new_name, new_price):
        cur.execute("""UPDATE menu_items SET item_name = %s, item_price = %s where item_name = %s""", (new_name, new_price, self.name))
        self.name = new_name
        self.price = new_price


# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)

cur.close()
conn.close()
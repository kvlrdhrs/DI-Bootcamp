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


    def update(self, id):
        cur.execute("""UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_id = %s""", (self.name, self.price, id))


# item = Menu_Item('Burger', 35)

# item = MenuItem('Burger', 35)
# item.save()
# item2= MenuItem('her', 10)
# item2.delete()
item3 = MenuItem('kkk', 1)
item3.update(2)

cur.close()
conn.close()
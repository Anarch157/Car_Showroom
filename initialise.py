import sqlite3

connection = sqlite3.connect('cars.db')
c = connection.cursor()
c.execute("""CREATE TABLE inventory (
        car_name text,
        cost_price integer,
        selling_price integer,
        customer_name text,
        salesman_name text
        )""")
connection.commit()
connection.close()

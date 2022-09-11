import sqlite3 

con = sqlite3.connect('example.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXIST tshirts
                    (sku text, name text, size text , price real)''')

cur.execute('''''')


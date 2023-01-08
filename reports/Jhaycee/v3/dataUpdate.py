import configparser
import csv
import sqlite3

config = configparser.ConfigParser()
config.read('config.ini')

import_csv = config['IMPORT_CSV']['path']

def make_db():

    conn = sqlite3.connect("personal_info")
    cur = conn.cursor()

    cur.execute(
                """CREATE TABLE personal_table
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone STRING,
                name STRING,
                postal STRING,
                address1 STRING,
                address2 STRING,
                address3 STRING
                ) 
                """)
    conn.commit()
    cur.close()
    conn.close()

def update_db():
    conn = sqlite3.connect("personal_info")
    cur = conn.cursor()

    with open(import_csv, encoding="CP932") as file:
        reader = csv.reader(file)
        for i in reader:
            try:
                cur.execute("INSERT INTO personal_table(phone,name,postal,address1,address2,address3) VALUES(?,?,?,?,?,?)",                        
                            (i[67],i[1],i[7],i[8],i[9],i[10]))
            except IndexError:
                continue
        conn.commit()

    cur.close()
    conn.close()

def clear_db():
    conn = sqlite3.connect('personal_info')
    cur = conn.cursor()
    cur.execute('DELETE FROM personal_table')
    conn.commit()

    cur.close()
    conn.close()

def select_item(searches):
    conn = sqlite3.connect('personal_info')
    cur = conn.cursor()

    cur.execute('SELECT * FROM personal_table WHERE phone = ?', (searches,))
    #cur.execute('SELECT * FROM personal_table WHERE phone LIKE ?', (searches,))
    temp = cur.fetchone()

    cur.close()
    conn.close()

    
    return temp



if __name__ == "__main__":
    l = select_item("E07041701660")
    print(type(l))

# name = input("name: ")
# postal = input("postal: ")
# address1 = input("address1: ")
# address2 = input("address2: ")
# address3 = input("address3: ")

# cur.execute("INSERT INTO personal_table(name, postal, address1, address2, address3) VALUES(?,?,?,?,?)",(name,postal,address1,address2,address3))
# conn.commit()


# cur.execute('SELECT * FROM personal_table')
# print(cur.fetchone())






"""SQLITE COMMANDS
sqlite3 my_db : Entering SQL command prompt
.databases : Show Databases
.tables : Show Tables
.open personal_table : Entering table
SELECT * FROM personal_table
"""
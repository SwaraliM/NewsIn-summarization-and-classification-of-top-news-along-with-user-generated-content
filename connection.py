import mysql.connector

def create_db():
    try:
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inshort_bharat"
        )
        print("Connection Success")
    except Exception as e:
        print(e)

    cursor=con.cursor()
    
    cursor.execute("CREATE TABLE users (  id INT PRIMARY KEY,  name VARCHAR(255),  email VARCHAR(255),  password VARCHAR(255),  type VARCHAR(255),  image_url VARCHAR(255));")
    con.commit()

    # cursor.execute("CREATE TABLE IF NOT EXISTS SUPPLIER(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contact TEXT, desc TEXT)")
    # con.commit()

    # cursor.execute("CREATE TABLE IF NOT EXISTS CATEGORY(cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    # con.commit()

    # cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCT(pid INTEGER PRIMARY KEY  AUTOINCREMENT, category TEXT, supplier TEXT, name TEXT, imprices TEXT, price TEXT, qty TEXT, status TEXT)")
    # con.commit()

    # cursor.execute("CREATE TABLE IF NOT EXISTS RECORD(category TEXT,supplier TEXT, name TEXT, price TEXT, qty TEXT, tprice TEXT,Pdate date)")
    # con.commit()

create_db()
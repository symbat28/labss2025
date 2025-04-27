# insert_console.py
import psycopg2
from config import config

def insert_from_console():
    name = input("name：")
    phone = input("phone：")
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("succses！")
        cur.close()
        conn.close()
    except Exception as error:
        print("error ：", error)

if __name__ == '__main__':
    insert_from_console()

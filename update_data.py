# update_data.py
import psycopg2
from config import config

def update_data():
    name = input("input change name：")
    phone = input("input new phone：")
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
        conn.commit()
        print("sucsessfull changes！")
        cur.close()
        conn.close()
    except Exception as error:
        print("error：", error)

if __name__ == '__main__':
    update_data()

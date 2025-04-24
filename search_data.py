# search_data.py
import psycopg2
from config import config

def search_data():
    name = input("name ：")
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + name + '%',))
        rows = cur.fetchall()
        for row in rows:
            print(f"👤 {row[1]} - {row[2]}")
        cur.close()
        conn.close()
    except Exception as error:
        print("error：", error)

if __name__ == '__main__':
    search_data()

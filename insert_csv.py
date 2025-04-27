# insert_csv.py
import psycopg2
import csv
from config import config

def insert_from_csv(filename):
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                            (row['name'], row['phone']))
        conn.commit()
        print("sucsess")
        cur.close()
        conn.close()
    except Exception as error:
        print("error ：", error)

if __name__ == '__main__':
    insert_from_csv('contact.csv')

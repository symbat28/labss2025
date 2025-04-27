# create_table.py
import psycopg2
from config import config

def create_table():
    command = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
    """
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        conn.commit()
        cur.close()
        conn.close()
        print("table phonebook created succsesfull！")
    except Exception as error:
        print("error：", error)

if __name__ == '__main__':
    create_table()


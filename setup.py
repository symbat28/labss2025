import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="S9281030124")
cur = conn.cursor()

with open("snake_user.sql", "r") as f:
    sql = f.read()
    cur.execute(sql)
    conn.commit()

cur.close()
conn.close()

print("sucsessful created！")

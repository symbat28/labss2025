import psycopg2

conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="S9281030124",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())
cur.close()
conn.close()

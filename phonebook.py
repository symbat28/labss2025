import csv
import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="phonebook1",  # 请替换成你自己的数据库名
        user="postgres",  # 数据库用户名
        password="S9281030124",  # 请替换成你自己的密码
        host="localhost",  # 本地连接
        port="5432"  # PostgreSQL 默认端口
    )

def create_table():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
        """)

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Кесте құрылды немесе бар кесте тексерілді.")
    except Exception as e:
        print(f"Ошибка: {e}")

def insert_from_csv(csv_file):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # 跳过CSV的标题行（如果有的话）
            for row in csv_reader:
                name, phone = row
                cursor.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES (%s, %s);
                """, (name, phone))

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ CSV файлынан деректер енгізілді.")
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")

def display_all():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM phonebook;")
        rows = cursor.fetchall()
        
        if rows:
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]}")
        else:
            print("❌ Кестеде ешқандай мәлімет жоқ.")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Ошибка: {e}")

def menu():
    while True:
        print("====================")
        print("📱 PHONEBOOK МӘЗІР:")
        print("1 - Консоль арқылы енгізу")
        print("2 - CSV файлынан енгізу")
        print("3 - Барлығын шығару")
        print("4 - Жаңарту (Update)")
        print("5 - Жою (Delete)")
        print("6 - 9/5 басталатын телефондарды көру")
        print("0 - Шығу")
        print("====================")

        choice = input("Команданы таңда: ")

        if choice == '1':
            name = input("Аты-жөніңізді енгізіңіз: ")
            phone = input("Телефон нөмірін енгізіңіз: ")
            try:
                conn = connect_db()
                cursor = conn.cursor()

                cursor.execute("""
                INSERT INTO phonebook (name, phone)
                VALUES (%s, %s);
                """, (name, phone))

                conn.commit()
                cursor.close()
                conn.close()
                print("✅ Жаңа жазба енгізілді.")
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == '2':
            csv_path = input("CSV файлының жолын енгіз: ")
            insert_from_csv(csv_path)
        
        elif choice == '3':
            display_all()

        elif choice == '0':
            print("Шығу...")
            break

        else:
            print("❌ Дұрыс команданы таңдаңыз!")

if __name__ == "__main__":
    create_table()  # 创建表格
    menu()
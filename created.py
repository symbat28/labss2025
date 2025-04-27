import sqlite3

def create_tables():
    # 连接到 snake_game.db（如果没有，会自动新建）
    conn = sqlite3.connect('snake_game.db')
    cur = conn.cursor()

    # 创建 users 表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        current_level INTEGER DEFAULT 1
    )
    ''')

    # 创建 user_scores 表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS user_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("✅ snake_game.db 创建成功，表 users 和 user_scores 已创建好！")

if __name__ == "__main__":
    create_tables()

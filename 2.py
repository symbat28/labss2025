import sqlite3
import curses
import random

# 连接到数据库
def connect_db():
    return sqlite3.connect('snake_game.db')

# 获取或创建用户
def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()

    # 查询用户是否存在
    cur.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
        print(f"欢迎回来，{username}！")
    else:
        # 如果不存在，创建新用户
        cur.execute("INSERT INTO users (username, current_level) VALUES (?, ?)", (username, 1))
        conn.commit()
        user_id = cur.lastrowid
        print(f"新用户 {username} 已创建！")

    conn.close()
    return user_id

# 保存分数
def save_score(user_id, score):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO user_scores (user_id, score) VALUES (?, ?)", (user_id, score))
    conn.commit()
    conn.close()
    print(f"得分 {score} 已保存到数据库！")

# 贪吃蛇游戏
def snake_game(user_id):
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)  # 窗口大小
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = curses.KEY_RIGHT
    score = 0

    snake = [[4,10], [4,9], [4,8]]
    food = [10,20]
    win.addch(food[0], food[1], '*')

    while True:
        win.border(0)
        win.addstr(0, 2, 'Score: ' + str(score) + ' ')
        win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120)

        prevKey = key
        event = win.getch()
        key = event if event != -1 else prevKey

        if snake[0][0] in [0, 19] or snake[0][1] in [0, 59] or snake[0] in snake[1:]:
            break

        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            score += 10
            food = None
            while food is None:
                nf = [
                    random.randint(1, 18),
                    random.randint(1, 58)
                ]
                food = nf if nf not in snake else None
            win.addch(food[0], food[1], '*')
        else:
            last = snake.pop()
            win.addch(last[0], last[1], ' ')

        win.addch(snake[0][0], snake[0][1], '#')

    curses.endwin()
    save_score(user_id, score)

# 主函数
def main():
    username = input("请输入用户名：")
    user_id = get_or_create_user(username)
    snake_game(user_id)

if __name__ == "__main__":
    main()




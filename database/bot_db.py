import random
import sqlite3


def sql_create():
    global db,cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")


    db.execute("CREATE TABLE IF NOT EXISTS mentors"
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "telegram_id INTEGER UNIQUE NOT NULL,"
               "username VARCHAR (100),"
               "name VARCHAR (100) NOT NULL,"
               "direction TEXT,"
               "age INTEGER NOT NULL,"
               "gender VARCHAR (10),"
               "groups INTEGER NOT NULL)")


    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO mentors "
            "(telegram_id, username, name, direction, age, gender, groups)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()
async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors ").fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.from_user.id,
                           f"id - {random_user[0]}, \nИмя - {random_user[1]}, \nНаправление - {random_user[2]}, \n"
                           f"Возраст - {random_user[3]}, \nГруппа - {random_user[4]}")
# async def sql_command_random():
#     users = cursor.execute("SELECT * FROM mentors").fetchall()
#     random_user = random.choice(users)
#     await return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_all_ids():
    return cursor.execute("SELECT telegram_id FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()


sql_create()
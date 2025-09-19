import sqlite3

def connection():
    connect = sqlite3.connect("databace_func.db")
    return connect

def execute(statement, value=None):
    with connection() as con:
        cursor = con.cursor()
        cursor.execute(statement, value or [])
        return cursor

def create_databse(name_table, statement: dict):
    data = [f"{key} {value}" for key, value in statement.items()]
    print(data)
    execute(f"""CREATE table IF NOT EXISTS {name_table} ({','.join(data)})""")

def insert_table(name_table, statement:dict):
    placeholders = ','.join("?" * len(statement))
    name = ','.join(statement.keys())
    value = tuple(statement.values())
    execute(f"""INSERT OR IGNORE INTO {name_table} ({name}) VALUES ({placeholders})""", value)

def update_table(name_table, statement: dict, id: int):
    data = [f"{key} = '{value}'" for key, value in statement.items()]
    data = ','.join(data)
    execute(f"""UPDATE {name_table} SET {data} WHERE id={id}""")

def delete_table(name_table, id):
    execute(f"DELETE FROM {name_table} WHERE id={id}")

def selecte_from_table(name_table, statement: list):
    data = ','.join(statement)
    with connection() as con:
        cursor = con.cursor()
        cursor.execute(f"""SELECT {data} FROM {name_table}""")
        res = cursor.fetchall()
        return res


# print(create_databse('test', {"id": "INTEGER"}))
# print(insert_table('test', {"id": 1}))
# print(update_table('test', {"id": 2}, 1))
# print(selecte_from_table("test", ["id"]))
import sqlite3

class Database_Manager:
    def __init__(self, filename):
        self.connections = sqlite3.connect(filename)

    def __del__(self):
        self.connections.close()

    def execute(self, statement, values=None):
        with self.connections:
            cursor = self.connections.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, name_table, statement: dict):
        statement = [f'{key_name} {value_statement}' for key_name, value_statement in statement.items()]
        # print(','.join(statement))
        self.execute(f"""CREATE TABLE IF NOT EXISTS {name_table} ({','.join(statement)})""")

    def data_add_table(self, name_table, statement: dict):
        placeholders = ','.join('?' * len(statement))
        name_columns = ','.join(statement.keys())
        columns_value = tuple(statement.values())
        # print(name_columns)
        self.execute(f"""INSERT OR IGNORE INTO {name_table} ({name_columns}) VALUES ({placeholders})""", columns_value)

    def update_table(self, name_table, statement: dict, id: int):
        data = [f'{key} = "{value}"' for key, value in statement.items()]
        data = ''.join(data)
        print(data)
        self.execute(f"""UPDATE {name_table} SET {data} WHERE id={id}""")

    def delete_table(self, name_table, data: dict):
        placeholders = [f'{column} = ?' for column in data.keys()]
        delete_criteria = ' AND '.join(placeholders)
        print(delete_criteria)
        self.execute(f"""DELETE FROM {name_table} WHERE {delete_criteria};""", tuple(data.values()))

    def select_from_table(self, table_name, criteria=None, order_by=None):
        criteria = criteria or {}
        # print("criteria:", criteria)
        query = f"""SELECT * from {table_name}"""

        if criteria:
            placeholders = [f'{column} = ?' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f' WHERE {select_criteria}'

        if order_by:
            query += f" ORDER BY {order_by}"
        # print("query:", query)
        return self.execute(query, tuple(criteria.values()))

    def select_from_table2(self, name_table, array: list, id):
        data = ','.join(array)
        print(data)
        with self.connections:
            cursor = self.connections.cursor()
            if id.isdigit():
                cursor.execute(f"""SELECT {data} FROM {name_table} WHERE id={id}""")
            elif id == "":
                cursor.execute(f"""SELECT {data} FROM {name_table}""")
            res = cursor.fetchall()
            return res


# a = Database_Manager('database.db')
# print(a.create_table('test', {'id': 'INTEGER', 'name': 'TEXT'}))
# print(a.data_add_table('test', {'id': '1', 'name': 'ruslan'}))
# print(a.update_table('test', {'name': 'ruslan'}, 1))
# print(a.delete_table('test', {'id': 1}))
# print(a.select_from_table('test', ['id', 'name'], input("Оставьте пустую строку для того, чтобы вывести все или введите id\n")))
# connect = sqlite3.connect('test')
# cursor = connect.cursor()
# res = cursor.fetchall()

# print(a.select_from_table('test'))

# create_table = input("Название таблицы: ")
# amount_placeholders = int(input("Количество полей: "))
# statement = {}
# for i in range(0, amount_placeholders):
#     key = input("Имя поля: ")
#     value = input("Значение: ")
#     statement[key] = value



# print(a.select_from_table2('test', ['name', 'id'], ''))
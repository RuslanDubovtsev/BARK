from Database.database import Database_Manager
from datetime import datetime
import sys

db = Database_Manager('bookmarks.db')

class Create_Bookmarks_TableCommand:
    def execute(self):
         db.create_table('bookmarks',
                        {'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
                         'title': 'TEXT NULL',
                         'url': 'TEXT NULL',
                         'data_added': 'TEXT NOT NULL',
                         })



class Add_Bookmark:
    def execute(self, user_dict: dict):
        user_dict['data_added'] = datetime.utcnow().isoformat()
        db.data_add_table('bookmarks', user_dict)

        return "Закладка добавлена!"


class Delete_Bookmark:
    def execute(self, id):
        db.delete_table('bookmarks', {"id": id})
        return "Закладка удалена!"



class Select_from_Bookmark:
    def __init__(self, order_by='data_added'):
        self.order_by = order_by

    def execute(self):
        selected = db.select_from_table('bookmarks', order_by=self.order_by).fetchall()
        a_str = ''

        for elem in selected:
            a_str += f"Id: {elem[0]}\n" \
                     f"Title: {elem[1]}\n" \
                     f"URL: {elem[2]}\n" \
                     f"Date: {elem[3][:10]}\n________\n"
        return a_str

    def API_execute(self):
        selected = db.select_from_table('bookmarks', order_by=self.order_by).fetchall()
        return selected

class Select_from_Bookmark_with_Title:
    # def __init__(self, order_by="url"):
    #     self.order_by = order_by

    def execute(self, title):
        selected = db.select_from_table('bookmarks', criteria=title).fetchall()
        a_str = ''

        for elem in selected:
            a_str += f"URL: {elem[2]}\n"
        return a_str




class QuitCommand:
    def execute(self):
        sys.exit()

# a = Add_Bookmark()
# print(a.execute())
from Commands.commands import Create_Bookmarks_TableCommand, Add_Bookmark, Select_from_Bookmark, Database_Manager, \
    QuitCommand, Delete_Bookmark, Select_from_Bookmark_with_Title
from setting import Option, print_options, get_options
import os

def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)

def get_user_input(label, flag=True):
    value = input(f"{label}: ") or None
    while flag and not value:
        value = input(f"{label}: ") or None
    return value

def get_new_bookmark_data():
    return {
        "title": get_user_input('Title'),
        "url": get_user_input('URL'),
    }

def delete_bookmark_data():
    return int(get_user_input('enter id for deleting'))

def title_for_select():
    a = str(get_user_input("Вв едите имя закладки"))
    return {"Title": a}

if __name__ == "__main__":
    print("Добро пожаловать в программу BARK")
    options = {
        'A': Option('Создать закладку', Create_Bookmarks_TableCommand()),
        'B': Option("Показать список закладки по дате", Select_from_Bookmark()),
        'C': Option('Удалить закладку', Delete_Bookmark(), delete_bookmark_data),
        'D': Option('Добавить закладку', Add_Bookmark(), get_new_bookmark_data),
        'E': Option('Выйти', QuitCommand()),
        'F': Option("Показать список закладки по имени", Select_from_Bookmark_with_Title(), title_for_select),
    }
    print_options(options)
    user_choice = get_options(options)
    clear_screen()
    user_choice.execute()

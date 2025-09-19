import requests
import json

from setting import Option
from Commands.commands import Add_Bookmark

res = requests.get('https://api.github.com/users')

data = json.loads(res.text)
git_dict = {}
# print(data)
class Search_star_users:
    def search_login(self):
        my_list = []
        for elem in data:
            my_list.append(elem['login'])

        return my_list[:4]

    def choice_name(self):
        for i in self.search_login():
            print(i)
        choice = input("\nВыберите имя: ")
        while choice not in self.search_login():
            choice = input("\nВыберите имя: ")
        return choice

    def get_url_name(self):

        new_url = requests.get(f'https://api.github.com/users/{self.choice_name()}')
        dict_data = json.loads(new_url.text)
        print(dict_data)
        URL = dict_data['html_url']
        name = dict_data['login']
        return {"title": name, 'url': URL}

a = Search_star_users()

print(a.get_url_name())
# print(data)
# bookmark_dict = {"title": a.get("title"), "url": a.get("url")}
# print(bookmark_dict)
# print(Add_Bookmark().execute(bookmark_dict))
# print(a)

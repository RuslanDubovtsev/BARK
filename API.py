import requests
import json
from flask import Flask, jsonify
from Commands.commands import Select_from_Bookmark
app = Flask(__name__)

class BARK_API:
    def __init__(self):
        self.db_result = Select_from_Bookmark().API_execute()

    def transfer_to_json(self):
        my_list = []
        for i in self.db_result:
            # print(i)
            temp_dict = {}
            temp_dict["id"] = i[0]
            temp_dict["title"] = i[1]
            temp_dict["url"] = i[2]
            temp_dict["data_added"] = i[3]
            my_list.append(temp_dict)
        return my_list

    def flask_api(self):

        @app.route('/')
        def main():
            return jsonify({'bark': self.transfer_to_json()})

        if __name__ == "__main__":
            app.run(debug=True)


print(BARK_API().flask_api())









# a = [(1, 'w', 's', '2024-09-01T15:56:04.947637'), (4, 'sd', 'sdwd', '2024-09-01T16:43:35.299248')]
#
# my_dict = {}
# my_str = {}
#
# def sorted_select(data:list):
#     a_str = ''
#
#     for elem in data:
#         a_str += f"Id: {elem[0]}\n" \
#                  f"Title: {elem[1]}\n" \
#                  f"URL: {elem[2]}\n" \
#                  f"Date: {elem[3][:10]}\n________\n"
#     return a_str
#
# # print(sorted_select(a))




def include_data(label):
    question = input(f"{label}")
    if not question:
        question = input(f"{label}")
    return question

class Data_Bicycle:
    def __init__(self, bicycle_list):
        self.bicycle_list = bicycle_list

    def __str__(self):

        return self.bicycle_list

    def choice_bysicle(self):
        print(self.bicycle_list)
        choice = include_data("Какой велосипед выбираете?: ")
        if choice in self.bicycle_list:
            return True
        else:
            return False




def data_format():
    list_values = []
    for _ in range(2):
        bicycle_type = include_data("Вид/название велосипеда: ")
        frame = include_data("Рама: ")
        front_tire = include_data("Переднее колесо: ")
        back_tire = include_data("Заднее колесо: ")
        list_values += [f"Вид/Название: {bicycle_type}, Рама: {frame}, Переднее колесо: {front_tire}, Заднее колесо: {back_tire}\n"]

    return list_values


def data_storage():
    unsort_list = data_format()
    sort_string = ""

    for elem in unsort_list:
        sort_string += elem

    return sort_string


a = Data_Bicycle(data_storage())
print(a.choice_bysicle())
class Option:
    def __init__(self, name, commands, function=None):
        self.name = name
        self.commands = commands
        self.function = function


    def __str__(self):
        return self.name

    def execute(self):
        data = self.function() if self.function else None
        further = self.commands.execute(data) if data else self.commands.execute()
        print(further)


def print_options(name):
    for key, values in name.items():
        print(f'{key}, {values}')

def valid(choice, options):
    if choice in options or choice.upper() in options:
        return choice

def get_options(options):
    choice = input("Выберите вариант: ")
    while not valid(choice, options):
        choice = input("Выберите вариант: ")

    return options[choice.upper()]
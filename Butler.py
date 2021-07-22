# Author Kyle Morrison

class Butler:
    def __init__(self, name_given):
        self.name = name_given

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    waiter = Butler("jarvis")
    waiter.get_name()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

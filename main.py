# Author Kyle Morrison

class Butler:
    def __init__(self):
        self.name = "Jarvis"

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def print_hi(self):
        print("Hi i'm " + self.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    waiter = Butler()
    waiter.print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

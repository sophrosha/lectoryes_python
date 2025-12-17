from random import randint
from menu import Menu

lis_num = []
def generate_number_phone(list_num):
    while len(list_num) < 10:
        gen_num = str(randint(0, 999_999_99_99))
        if not gen_num in list_num:
            list_num.append(f"+7{gen_num}")
    return list_num


class Direct:
    def __init__(self, list_np):
        self.list_id = []
        self.id_num = 0
        self.list_np = list_np

    def _generate_id(self):
        self.id_num += 1
        number_id = self.id_num
        return number_id

    def sort_id(self):
        self.list_id.sort()
        print("Отсортированны id \n")

    def sort_num(self):
        self.list_np.sort()
        print("Отсортированны номера телефонов \n")

    def list_print(self):
        ind = 0
        while ind < len(self.list_np):
            print(f"Телефон: {self.list_np[ind]} :: Айди: {self.list_id[ind]}")
            ind += 1

    def add_number(self):
        print("Сколько добавить контактов")
        ans = int(input("> "))
        ind = 0
        print("d")
        while ans > ind:
            print("Введите номер телефона")
            ans1 = input("> ")
            print("Введите айди(по умолчанию генерируется)")
            ans2 = int(input("> "))
            if not ans2:
                ans2 = self._generate_id()
            print("=> Добавление номера телефона")
            self.list_np.append(ans1)
            print("=> Добавление айди")
            self.list_id.append(ans2)
            print("Готово!")
        print("e")

    def menu(self):
        for element in range(len(self.list_np) + 1):
            self.list_id.append(element)
        if not self.list_id and self.list_np:
            print("в списке отсуствуют значения")
            exit()

        print(":: Справочник ::")
        print("-= Введите команду help\n "
              "для информации по командам")
        while True:
            ans = input("> ")
            match ans:
                case "help":
                    print("-: список доступных команд\n")
                    print("?: sort_id - отсортировать по индефикационным номерам")
                    print("?: add_number - добавить новый телефон")
                    print("?: sort_num - отсортировать по номерам телефона")
                    print("?: list_print - вывести список с кодами и телефонами")
                    print("?: q/exit/void - выход")
                case "sort_id":
                    self.sort_id()
                case "sort_num":
                    self.sort_num()
                case "list_print":
                    self.list_print()
                case "q" | "exit" | "void":
                    print("-! Выход!")
                    break
                case "add_number":
                    self.add_number()
                case _:
                    print("Неверная команда. Введите help")
                    print("Вы хотите выйти? Y/n")
                    while True:
                        ans_1 = input("> ")
                        match ans_1:
                            case "Y" | "y":
                                exit()
                            case "N" | "n":
                                break
                            case _:
                                break

def task1():
    gen_num = generate_number_phone(lis_num)
    sortir = Direct(gen_num)
    sortir.menu()

class Book:
    def __init__(self, list_year, list_book):
        self.list_year = list_year
        self.list_book = list_book

    def sort_name(self):
        ind = 0
        while ind < len(self.list_book):
            self.list_
            self.list_book.append(self.list_book[ind])
            print("Отсортированны книги!")

    def sort_year(self):

if __name__ == "__main__":
    TASKS = {1: ["Сортировка номеров и айди", task1]}
    info = Menu("13.11.25", TASKS)
    info.Tasks()
    info.Answer()
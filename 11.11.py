from menu import Menu
from random import randint

class Number:
    def __init__(self, list_num):
        self.list_num = list_num

    def process(self):
        index_two_three = int(len(self.list_num) * (2 / 3))
        index_one_three = int(len(self.list_num) * (1 / 3))
        arithmetic_mean = sum(self.list_num) / len(self.list_num)
        if arithmetic_mean > 0:
            one_part = sorted(self.list_num[:index_two_three])
            two_part = sorted(self.list_num[index_two_three:], reverse=True)
            return one_part, two_part
        else:
            one_part = sorted(self.list_num[:index_one_three])
            two_part = sorted(self.list_num[index_one_three:], reverse=True)
            return one_part, two_part

class Student:
    def __init__(self, list_student=None):
        if list_student is None:
            list_student = []
        self.list_student = list_student

    def _print_grade(self):
        print("?> Список оценок:")
        print(*self.list_student, "\n")

    def _print_sorted_grade(self):
        print("?> Список сортированных оценок:")
        print(*sorted(self.list_student), "\n")

    def _retake_exam(self):
        try:
            print(f"-= Оценки: {self.list_student}")
            print(f"-= Введите элемент")
            while True:
                answer_element = int(input("> "))
                if answer_element > len(self.list_student):
                    print("!> Такого элемента не существует!")
                    break
                else:
                    print("-= Введите оценку. Должна быть от 1 до 12")
                    answer_rate = int(input("> "))
                    if answer_rate > 12:
                        print("!> Вы ввели число больше 12. Выход!")
                        break
                    else:
                        print()
                        self.list_student[answer_element-1] = answer_rate
                        print("Оценка изменена! \n")
                        break
        except ValueError:
            print("!> Введено не число, выход из программы")
            exit()

    def _add_rate(self):
        print("-= Введите число, если несколько то через пробел.")
        try:
            answer = input()
            list_new = answer.split()
            for num in list_new:
                self.list_student.append(int(num))
            print("-= Добавлено! \n")
        except ValueError:
            print("!> Введено не число, выход из программы")
            exit()


    def _is_scholarship(self):
        if not self.list_student:
            print("!!> Добавьте оценки!")
        arithmetic_mean = sum(self.list_student) / len(self.list_student)
        if arithmetic_mean >= 10.7:
            print("-= Студент может получить стипендию")
        else:
            print("-= Студент не может получить стипендию")
            print(f"-= Так как его балл равен {arithmetic_mean}")
            print(f"-= Что ниже числа 10.7")

    '''
        Так как _print_help не имеет используемых self методов
        то его можно пометить как статическим методом.
        
        Сам PyCharm на такое ругается
    '''
    @staticmethod
    def _print_help():
        print("Список доступных команд \n")
        print("print   - Вывод оценок")
        print("printed - Вывод сортированных оценок")
        print("retake  - Пересдача экзамена")
        print("ship    - Выходит ли стипендия")
        print("add     - Добавить оценку")
        print("exit    - Выход")


    def menu(self):
        print("Успеваемость")
        print("!>> Введите help для просмотра текущих команд")
        while True:
            answer = input(": ")
            match answer:
                case "q" | "exit" | "qq":
                    break
                case "help" | "h":
                    self._print_help()
                case "print":
                    self._print_grade()
                case "printed":
                    self._print_sorted_grade()
                case "retake":
                    self._retake_exam()
                case "ship":
                    self._is_scholarship()
                case "add":
                    self._add_rate()
                case _:
                    print("Такой команды не существует, введите help")

class BubbleFork:
    def __init__(self, list_num=None):
        if list_num is None:
            list_num = [randint(0, 12) for _ in range(0, 20 + 1)]
        self.list_num = list_num

    def main(self):
        for index in range(len(self.list_num) - 1, 0, - 1):
            print("-="*8)
            print("-= Начало сортировки")
            print(f"Первый индекс: {index}")
            for interior in range(0, index):
                print(f"Граница проверки элемента {interior}")
                if self.list_num[interior] > self.list_num[interior + 1]:
                    (self.list_num[interior],
                     self.list_num[interior + 1]) = (self.list_num[interior + 1],
                                                     self.list_num[interior])

def task_one():
    numbers_list = [randint(0, 12) for _ in range(0, 12 + 1)]
    num = Number(numbers_list)
    main, rest = num.process()
    print(f"Сгенерировано          ", *numbers_list)
    print(f"Основное сортировано   ", *main)
    print(f"Реверсивно сортировано ", *rest)
    return 1

def task_two():
    student = Student()
    student.menu()
    return 1

def task_three():
    bubble = BubbleFork()
    bubble.main()
    return 1

if __name__ == "__main__":
    TASKS = {
        1: ["Сортировка", task_one],
        2: ["Успеваемость", task_two],
        3: ["Пузырек", task_three]
    }
    DATE = "11.11.25"
    menu = Menu(DATE, TASKS)
    menu.Tasks()
    menu.Answer()
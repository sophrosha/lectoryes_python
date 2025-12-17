from random import randint

class SortFour:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.list3 = []
        self.list4 = []
        self.list5 = []
        self.dict5 = set()
    
    def generate_numbers(self):
        gen = lambda: [randint(0, 12) for _ in range(0, 12)]
        self.list1 = gen()
        self.list2 = gen()
        self.list3 = gen()
        self.list4 = gen()
    
    def __int__(self):
        self.generate_numbers()
    
    def _print(self):
        print("-= Списки")
        print(" ", *self.list1)
        print(" ", *self.list2)
        print(" ", *self.list3)
        print(" ", *self.list4)
        print("-= Пятый список")
        print(" ", *self.list5)

    @staticmethod
    def _help():
        print(":> Помощь.")
        print(" help          - помощь")
        print(" exit          - выход")
        print(" print         - вывод списков")
        print(" sort_plus     - сортировка в большую сторону")
        print(" sort_minus    - сортировка в меньшую сторону")
        print(" grep_value    - найти значение")
        print(" integrate_two - интеграция списка согласно 2 заданию")

    def _integrate(self):
        list00 = [*self.list1, *self.list2, *self.list3, *self.list4]
        self.list5 = list00

    def _sort_plus(self):
        self.list5 = sorted(self.list5)
        print("-= Отсортирован список в большую сторону!")
    
    def _sort_minus(self):
        self.list5 = sorted(self.list5, reverse=True)
        print("-= Отсортирован список с меньшую сторону!")

    def _grep_value(self):
        print("-= Введите число")
        answer = int(input("> "))
        for element in self.list5:
            if element == answer:
                print("Найдено число!")
                print(f"Число: {element}")
                list000 = []
                for numb in self.list5:
                    if numb == answer:
                        list000.append(numb)
                if len(list000) > 1:
                    print("Найдены числа")
                    print("=", *list000)
                    break
                else:
                    print("Повторяющихся чисел нету")

    def _integrate_two_task(self):
        list000 = [*self.list1, *self.list2, *self.list3, *self.list4]
        for element in list000:
            self.dict5.add(element)
        for element in self.dict5:
            self.list5.append(element)
        print("Интегрированны элементы!")

    def main(self):
        self.generate_numbers()
        self._integrate()
        print("Сгенерированны 4 списка")
        print("Введите help для просмотра комманд")
        while True:
            answer = input("> ")
            match answer:
                case "help":
                    self._help()
                case "exit":
                    print("!> Выход из программы!")
                    break
                case "print":
                    self._print()
                case "sort_plus":
                    self._sort_plus()
                case "sort_minus":
                    self._sort_minus()
                case "grep_value":
                    self._grep_value()
                case "integrate_two":
                    self._integrate_two_task()
                case _:
                    print("Неверная команда!")

if __name__ == "__main__":
    sorting = SortFour()
    sorting.main()
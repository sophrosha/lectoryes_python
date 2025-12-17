from random import randint

class TwoAndOne:
    def __init__(self):
        self.list_numbers = []

    def _generate_numbers(self):
        self.list_numbers = [randint(1, 10) for _ in range(0, 10 + 1)]
        return 1

    def _find_binary(self):
        if not self.list_numbers:
            print("Отсуствуют числа в списке!")
            return 0
        print("Бинарный поиск")
        print("Введите число для поиска")
        answer_binary = int(input("> "))
        low = 0
        high = len(self.list_numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = self.list_numbers[mid]
            if mid_val == answer_binary:
                print(f"Найдено число! Индекс {mid}")
                return 1
            elif mid_val < answer_binary:
                low = mid + 1
            else:
                high = mid - 1
        return 0

    def _find_lineal(self):
        if not self.list_numbers:
            print("Отсуствуют числа в списке")
            return 0
        print("Линейный поиск")
        print("Введите число для поиска")
        answer_lineal = int(input("> "))
        for ind, element in enumerate(self.list_numbers):
            if element == answer_lineal:
                print(f"Найденно число, индекс {ind}")
                return 1
        print("Число не найдено")
        return 0

    @staticmethod
    def _help():
        print(
            " print_list - Вывод сгенерированного списка \n",
            "find_binary - Поиск по бинарному алгоритму \n",
            "find_lineal - Поиск по линейному алгоритму \n",
            "regen_list - Перегенерировать список \n",
            "help - вывод команд \n",
            "exit - выход из программы \n"
        )

    def _print_list(self):
        print("Числа в списке")
        print(*self.list_numbers)

    def main(self):
        self._generate_numbers()
        print("Линейный и бинарный поиск")
        print("Сгенерирован список")
        print("help - команды первой задачи")
        while True:
            answer = input("> ")
            match answer:
                case "print_list":
                    self._print_list()
                case "find_binary":
                    self._find_binary()
                case "find_lineal":
                    self._find_lineal()
                case "help":
                    self._help()
                case "regen_list":
                    self._generate_numbers()
                    print("ok")
                case "exit":
                    break
                case _:
                    print("Команда не найдена.")

class Soda:
    def __init__(self, additive):
        self.additive = additive
        self.additives = [
            "лимон", "кола", "груша",
            "щелкунчик", "байкал"
        ]

    def show_my_drink(self):
        for element in self.additives:
            if element == self.additive.lower():
                print(f"Газировка и {self.additive}")
                return 1
        print("Обычная газировка")
        return 0



if __name__ == "__main__":
    print(
        "Меню задач 17.11.25\n",
        "1 - 1 и 2 задача\n",
        "2 - 3 задача\n"
    )
    ans = int(input("> "))
    if ans == 1:
        m = TwoAndOne()
        m.main()
    elif ans == 2:
        print("Введите добавку к газировке")
        while True:
            answer_soda = input("> ")
            match answer_soda:
                case "exit":
                    break
                case _:
                    if answer_soda:
                        n = Soda(answer_soda)
                        n.show_my_drink()
                        break
                    else:
                        print("Введена пустота, выход")
                        exit()
    else:
        print("Ничего не веденно, выход!")
        exit()
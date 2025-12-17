
# Задание 4
class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.exp_points = 0
        self.inventory = []

    def __str__(self):
        return (f" -= Имя игрока: {self.nickname}\n",
                f"-= Очки опыта: {self.exp_points}\n",
                "-= Инвентарь: {}\n".format(*self.inventory))

    def add_exp(self, exp):
        self.exp_points += exp

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        for ind, value in enumerate(self.inventory):
            if value is item:
                self.inventory.pop([ind])
        return f"Item not found"

# Задание 5
class Resistors:
    def __init__(self): pass

    @staticmethod
    def parallel(r1: int, r2: int):
        return (r1 * r2) / (r1 + r2)

    @staticmethod
    def consent(*args):
        list = []
        for num in args:
            list.append(int(num))
        return sum(list)

def main():
    print("Выберите задания")
    while True:
        ans = input("> ")
        match ans:
            case "resistors":
                r = Resistors()
                while True:
                    print("Введите вид вычисления транзисторов")
                    print("parallel или consent")
                    ans1 = input("> ")
                    match ans1:
                        case "parallel":
                            print("Введите значение r1 и r2 через пробел")
                            ans_par = input("> ")
                            list1 = ans_par.split()
                            print("Ответ:",
                                r.parallel(int(list1[0]), int(list1[1])))
                        case "consent":
                            print("Введите значения r1, r2, r... через пробел")
                            ans_con = input("> ")
                            list1 = ans_con.split()
                            print("Ответ", r.consent(list1))
                        case _:
                            print("Введена пустота или значение, выход")
                            break
            case "player":
                print("Введите ник персонажа, а так же опыт и предмет через запятую.")
                print("Название предмета должно быть через _")
                ans_player = input("> ")
                list_info_player = ans_player.split()
                player = Player(list_info_player[0])
                player.add_exp(list_info_player[1])
                player.add_item(list_info_player[2])
                print(player.__str__())
            case "exit":
                break
            case _:
                continue

if __name__ == "__main__":
    main()
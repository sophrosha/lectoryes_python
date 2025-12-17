import time
from snailrace import Snail
from print_race import print_race

def get_snail_name(index):
    while True:
        name = input(f"Введите имя улитки #{index + 1}: ").strip()
        if name == "":
            print("Имя не может быть пустым.")
        elif len(name) > 10:
            print("Имя должно быть не длиннее 10 символов.")
        else:
            return name

def get_num_snails():
    while True:
        num_input = input("Сколько улиток участвует (от 5 до 20)? ")
        try:
            num = int(num_input)
        except ValueError:
            print("Нужно ввести целое число.")
            continue
        if 5 <= num <= 20:
            return num
        else:
            print("Число должно быть от 5 до 20.")

def Menu():
    print("Добро пожаловать на Бега улиток!")
    num = get_num_snails()
    snails = []
    for i in range(num):
        name = get_snail_name(i)
        snails.append(Snail(name))

    print("\nГонка начинается!\n")
    time.sleep(1)

    results = []
    while len(results) < len(snails):
        for snail in snails:
            if not snail.finished:
                snail.sleep()
                snail.move()
                if snail.finished:
                    results.append(snail)
        print_race(snails)

    print("\nГонка окончена!\n")
    print("Топ 3:")
    for i in range(min(3, len(results))):
        place = i + 1
        print(f"{place}. {results[i].name}")

    print("\nРезультаты:")
    for i, snail in enumerate(results):
        print(f"{i + 1}. {snail.name}")

if __name__ == "__main__":
    Menu()
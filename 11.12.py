import random

class Hero:
    def __init__(
        self,
        lvl=1,
        name="Неизвестный",
        last_name="Без прозвища",
        lor="Неизвестно",
        history="Нет",
        hp=100,
        old=20,
        spells=None,
        radius=5,
        weaknesses=None,
        speed=3,
        intelligence=3,
        power=3,
        agility=3,
        lucky=3,
        power_damage=5,
        exp=0
    ):
        self.lvl = lvl
        self.name = name
        self.last_name = last_name
        self.lor = lor
        self.history = history
        self.hp = hp
        self.old = old
        self.spells = spells if spells is not None else []
        self.radius = radius
        self.weaknesses = weaknesses if weaknesses is not None else []
        self.gender = None
        self.attr = {
            "speed": speed,
            "intelligence": intelligence,
            "power": power,
            "agility": agility,
            "lucky": lucky,
            "power_damage": power_damage,
            "exp": exp
        }

    def attack_to_damage(self):
        return self.attr["power_damage"]

    def protection_to_damage(self):
        return self.attr["agility"] * 0.5


class Enemy:
    def __init__(self, name, attr):
        self.name = name
        self.attr = attr

    def attack_to_damage(self):
        return self.attr["power_damage"]

    def protection_to_damage(self):
        return self.attr["agility"] * 0.5


class BattleLog:
    wins = 0
    losses = 0
    draws = 0

    @staticmethod
    def record_result(result):
        match result:
            case "win":
                BattleLog.wins += 1
            case "loss":
                BattleLog.losses += 1
            case "draw":
                BattleLog.draws += 1

    @staticmethod
    def show_stats():
        print("\n=== СТАТИСТИКА ===")
        print(f"Побед: {BattleLog.wins}")
        print(f"Поражений: {BattleLog.losses}")
        print(f"Ничьих: {BattleLog.draws}")


def create_hero():
    name = input("Введите имя героя: ")
    last_name = input("Введите прозвище: ")
    print("Выберите класс:")
    print("1. Лучник")
    print("2. Воин")
    print("3. Маг")
    print("4. Танк")
    choice = input("Ваш выбор (1-4): ")

    match choice:
        case "1":
            return Hero(
                name=name,
                last_name=last_name,
                speed=6,
                agility=7,
                power_damage=8
            )
        case "2":
            return Hero(
                name=name,
                last_name=last_name,
                power=7,
                power_damage=9,
                agility=5
            )
        case "3":
            return Hero(
                name=name,
                last_name=last_name,
                intelligence=8,
                power_damage=10,
                agility=2
            )
        case "4":
            return Hero(
                name=name,
                last_name=last_name,
                power=6,
                agility=4,
                power_damage=6,
                speed=2
            )
        case _:
            print("Неверный выбор. Создан Воин по умолчанию.")
            return Hero(
                name=name,
                last_name=last_name,
                power=7,
                power_damage=9,
                agility=5
            )


def battle(hero, enemies):
    enemy_name = random.choice(list(enemies.keys()))
    enemy = enemies[enemy_name]

    print(f"\nБой с {enemy.name}!")
    hero_damage = hero.attack_to_damage()
    enemy_damage = enemy.attack_to_damage()

    print(f"{hero.name} наносит {hero_damage} урона.")
    print(f"{enemy.name} наносит {enemy_damage} урона.")

    if hero_damage > enemy_damage:
        print("Вы победили!")
        BattleLog.record_result("win")
    elif hero_damage < enemy_damage:
        print("Вы проиграли...")
        BattleLog.record_result("loss")
    else:
        print("Ничья!")
        BattleLog.record_result("draw")


def hero_menu(hero, enemies):
    while True:
        print("\n=== МЕНЮ БОЯ ===")
        print("1. Сразиться со случайным врагом")
        print("2. Показать статистику")
        print("/exit — Выйти из игры")
        command = input("Введите команду: ")

        match command:
            case "1":
                battle(hero, enemies)
            case "2":
                BattleLog.show_stats()
            case "/exit":
                return
            case _:
                print("Неизвестная команда.")


def main():
    enemies = {
        "Слизь": Enemy("Слизь", {
            "speed": 2, "intelligence": 1, "power": 3,
            "agility": 1, "lucky": 1, "power_damage": 4, "exp": 10
        }),
        "Гоблин": Enemy("Гоблин", {
            "speed": 5, "intelligence": 3, "power": 4,
            "agility": 5, "lucky": 3, "power_damage": 6, "exp": 20
        }),
        "Наблюдатель": Enemy("Наблюдатель", {
            "speed": 3, "intelligence": 8, "power": 2,
            "agility": 4, "lucky": 2, "power_damage": 5, "exp": 25
        }),
        "Орк": Enemy("Орк", {
            "speed": 4, "intelligence": 2, "power": 8,
            "agility": 3, "lucky": 2, "power_damage": 10, "exp": 30
        })
    }

    hero = create_hero()
    hero_menu(hero, enemies)


if __name__ == "__main__":
    main()

from random import randint
from time import sleep

class Animal:
    def __init__(self, nickname):
        self.nickname = str(nickname)

    def __str__(self):
        return f"{self.nickname}"

class Cat(Animal):
    def __init__(self, nickname):
        super().__init__(nickname)
        self.nickname = nickname
        self.voices = [
            "Мяу",
            "Мяяяя",
            "Meoow"
        ]

    def voice(self):
        random_number = randint(0, 2)
        text = self.voices[random_number]
        print(f"{self.nickname} Говорит: {text}")

    @staticmethod
    def run():
        ind = 0
        while ind < 100:
            print(f"Кошка пробежала {ind}м")
            ind += 1
        print("Кошка устала")

class Parrot(Animal):
    def __init__(self, nickname):
        super().__init__(nickname)
        self.nickname = nickname
        self.voices = [
            "Привет",
            "Бл*ть, выпусти из клетки",
            "чик-чирррик",
            "**свист**",
            "**хрюканье**"
        ]

    def voice(self):
        random_number = randint(0, 4)
        text = self.voices[random_number]
        print(f"{self.nickname} Говорит: {text}")

    @staticmethod
    def fly():
        ind = 0
        while ind < 100:
            print(f"Попугай пролетел {ind}м")
            sleep(0.1)
            ind += 1
        print("Попугай устал")


def main_one_task():
    print("--= Вызов классов")
    cat = Cat("Мася")
    parrot = Parrot("Кеша")
    print("--= Имена животных")
    print(f"Кошка: {cat.__str__()}")
    print(f"Попугай: {parrot.__str__()}")
    print("--= Голос животных")
    print("Кошка:")
    cat.voice()
    print("Попугай:")
    parrot.voice()


class Message:
    def __init__(self, sender, recipient):
        self.recipient = recipient
        self.sender = sender

    def show_header(self):
        print("--== Сообщение ==--")
        print(f"Отправитель: {self.sender}, получатель: {self.recipient}")

class StickerMessage(Message):
    def __init__(self, recipient, sender, count):
        super().__init__(recipient, sender)
        self.smiles = [
            ";)", ":)", ":D",
            ":P", ":(", ":'(",
            ":O", ":|", "xD",
            "<3"
        ]
        self.count = count

    def send(self):
        self.show_header()
        smile = self.smiles[self.count + 1]
        print(f"Отправленный смайл: {smile}")

class TextMessage(Message):
    def __init__(self, sender, recipient, text):
        super().__init__(sender, recipient)
        self.sender = sender
        self.recipient = recipient
        self.text = text

    def send(self):
        self.show_header()
        print("--== Сообщение")
        print(f"{self.text}")

def main_two_task():
    text_message = "Hi, how are you? My arch is break of one day ago. Fuck archlinux"
    sender = "sophrosha"
    recipient = "Dmitry"
    text_message = TextMessage(sender, recipient, text_message)
    text_message.send()

if __name__ == "__main__":
    print("Выберите задание")
    print("1, 2, 3")
    while True:
        ans = input("> ")
        match ans:
            case "1":
                main_one_task()
            case "2":
                main_two_task()
            case "3":
                pass
            case "exit":
                exit()
            case _:
                continue

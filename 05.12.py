class Editor:
    def __init__(self, list_data=None, name_program=None,
                 help_menu=None, elements=1):
        self.list_data = list_data
        self.name_program = name_program
        self.help_menu = help_menu
        self.elements = elements

    def menu(self):
        print(f"Console as {self.name_program}")
        print("commands printed in /help")
        while True:
            ans = input("> ")
            match ans:
                case "/add": self.add()
                case "/search": self.search()
                case "/replace": self.replace()
                case "/help": self.help()
                case "/print": self.printf()
                case _: break


    def add(self):
        counter = 0
        temp_element = []
        while counter != self.elements:
            ans = input("+> ")
            if len(ans) != 0:
                temp_element.append(ans)
            counter += 1
        temp_element.append(self.list_data)

    def search(self):
        ans = input("?> ")
        counter = 0
        for ind, element in enumerate(self.list_data):
            if ans == element[counter]:
                print("Searched values")
                print("{} in {}".format(element[counter], self.list_data[ind]))
                if len(element) < counter+1:
                    counter += 1

    def replace(self):
        ans1 = input("pos 1|> ")
        ans2 = input("pos 2|> ")
        ans3 = int(input("index |> "))
        for element in self.list_data:
            if element[ans3] == ans1:
                element[ans3] = ans2
            else:
                return 0
        return None

    def help(self):
        if self.help_menu is None:
            print("Help text is not initialised")
            return 0
        for element in self.help_menu:
            print("{} - {}".format(element[0], element[1]))
        return None

    def printf(self):
        print(f"{self.list_data}")
        return None

class TaskOne:
    def __init__(self):
        self.program = "Великие баскетболисты"
        self.data = [
            ["Michael Jordan", 198],
            ["LeBron James", 206],
            ["Kobe Bryant", 198],
            ["Wilt Chamberlain", 216],
            ["Bill Russell", 208],
            ["Magic Johnson", 206],
            ["Larry Bird", 206],
            ["Shaquille O'Neal", 216],
            ["Kareem Abdul-Jabbar", 218],
            ["Kevin Durant", 211],
            ["Stephen Curry", 188],
            ["Tim Duncan", 211],
            ["Hakeem Olajuwon", 213],
        ]
        self.help_text = [
            ["/help", "Показать список всех доступных команд"],
            ["/add", "Добавить нового баскетболиста в список"],
            ["/search", "Найти баскетболиста по имени или фамилии"],
            ["/replace", "Заменить данные существующего баскетболиста"],
            ["/print", "Вывести весь текущий список баскетболистов"]
        ]
        self.elements = 2

    def init(self):
        general = Editor(list_data=self.data, name_program=self.program,
                        help_menu=self.help_text, elements=self.elements)
        general.menu()

class TaskTwo:
    def __init__(self):
        self.program = "Англо-Французкий словарь"
        self.data = [
            ["hello", "bonjour"],
            ["goodbye", "au revoir"],
            ["yes", "oui"],
            ["no", "non"],
            ["please", "s'il vous plaît"],
            ["thank you", "merci"],
            ["you're welcome", "de rien"],
            ["how are you?", "comment allez-vous ?"],
            ["my name is", "je m'appelle"],
            ["I love", "j'adore"],
            ["good morning", "bonjour"],
            ["good evening", "bonsoir"],
            ["good night", "bonne nuit"],
            ["see you later", "à plus tard"],
            ["water", "eau"],
            ["bread", "pain"],
            ["wine", "vin"],
            ["cheese", "fromage"],
            ["friend", "ami"],
            ["family", "famille"],
            ["house", "maison"],
            ["car", "voiture"],
            ["cat", "chat"],
            ["dog", "chien"],
            ["beautiful", "beau"],
            ["big", "grand"],
            ["small", "petit"],
            ["happy", "heureux"],
            ["sad", "triste"],
            ["today", "aujourd'hui"],
            ["tomorrow", "demain"],
            ["yesterday", "hier"],
            ["I want", "je veux"],
            ["I have", "j'ai"],
            ["I am", "je suis"],
            ["where is", "où est"],
            ["what", "quoi"],
            ["when", "quand"],
            ["why", "pourquoi"],
            ["how", "comment"],
            ["one", "un"],
            ["two", "deux"],
            ["three", "trois"],
            ["four", "quatre"],
            ["five", "cinq"],
            ["six", "six"],
            ["seven", "sept"],
            ["eight", "huit"],
            ["nine", "neuf"],
            ["ten", "dix"]
        ]
        self.help_text = [
            ["/help", "Показать список всех доступных команд"],
            ["/add", "Добавить новое слово в список"],
            ["/search", "Найти слово на анг или на франц"],
            ["/replace", "Заменить слово"],
            ["/print", "Вывести весь текущие слова"]
        ]
        self.elements = 2

    def init(self):
        general = Editor(list_data=self.data, name_program=self.program,
                        help_menu=self.help_text, elements=self.elements)
        general.menu()

class TaskThree:
    def __init__(self):
        self.program = "Фирма"
        self.data = [
            ["Иванов Иван Иванович", "+7 (999) 123-45-67", "ivanov@example.com", "Менеджер", "101", "ivanov_skype"],
            ["Петрова Анна Сергеевна", "+7 (999) 234-56-78", "petrova@example.com", "Бухгалтер", "102", "anna_petrova"],
            ["Сидоров Дмитрий Алексеевич", "+7 (999) 345-67-89", "sidorov@example.com", "Программист", "205", "dima_sidorov_dev"],
            ["Кузнецова Елена Владимировна", "+7 (999) 456-78-90", "kuznetsova@example.com", "HR-специалист", "103", "elena_kuz"],
            ["Морозов Артём Олегович", "+7 (999) 567-89-01", "morozov@example.com", "Директор", "301", "artem_morozov_ceo"]
        ]
        self.help_text = [
            ["/help", "Показать список всех доступных команд"],
            ["/add", "Добавить нового сотрудника в список"],
            ["/search", "Найти сотрудника по ФИО или должности"],
            ["/replace", "Заменить данные существующего сотрудника"],
            ["/print", "Вывести весь текущий список сотрудников"]
        ]
        self.elements = 6  # ФИО, телефон, почта, должность, кабинет, Skype

    def init(self):
        general = Editor(list_data=self.data, name_program=self.program,
                        help_menu=self.help_text, elements=self.elements)
        general.menu()


class TaskFour:
    def __init__(self):
        self.program = "Книжная коллекция"
        self.data = [
            ["Фёдор Достоевский", "Преступление и наказание", "Роман", "1866", "672", "Эксмо"],
            ["Джордж Оруэлл", "1984", "Антиутопия", "1949", "328", "АСТ"],
            ["Габриэль Гарсиа Маркес", "Сто лет одиночества", "Магический реализм", "1967", "416", "Азбука"],
            ["Дж. Р. Р. Толкин", "Властелин колец", "Фэнтези", "1954", "1216", "АСТ"],
            ["Агата Кристи", "Десять негритят", "Детектив", "1939", "256", "Эксмо"],
            ["Харпер Ли", "Убить пересмешника", "Драма", "1960", "320", "Азбука"],
            ["Рэй Брэдбери", "451 градус по Фаренгейту", "Антиутопия", "1953", "192", "АСТ"],
            ["Антуан де Сент-Экзюпери", "Маленький принц", "Притча", "1943", "96", "Эксмо"]
        ]
        self.help_text = [
            ["/help", "Показать список всех доступных команд"],
            ["/add", "Добавить новую книгу в коллекцию"],
            ["/search", "Найти книгу по автору или названию"],
            ["/replace", "Заменить данные существующей книги"],
            ["/print", "Вывести всю текущую книжную коллекцию"]
        ]
        self.elements = 6  # автор, название, жанр, год, страницы, издательство

    def init(self):
        general = Editor(list_data=self.data, name_program=self.program,
                        help_menu=self.help_text, elements=self.elements)
        general.menu()

def main():
    task = input("Выберите задание (1-4): ")
    if task == "1":
        TaskOne().init()
    elif task == "2":
        TaskTwo().init()
    elif task == "3":
        TaskThree().init()
    elif task == "4":
        TaskFour().init()
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
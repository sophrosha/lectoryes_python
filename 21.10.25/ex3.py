note_book = {"Маша":
{'tel':'+7922123561','vk':'vk.com/masha321','youtube':'youtube.com/masha321','telegram'
:'t.me/masha321'},
"Маша":
{'tel':'+7922123561','vk':'vk.com/masha321','youtube':'youtube.com/masha321','telegram'
:'t.me/masha321'},
"Маша":
{'tel':'+7922123561','vk':'vk.com/masha321','youtube':'youtube.com/masha321','telegram'
:'t.me/masha321'},
"Маша":
{'tel':'+7922123561','vk':'vk.com/masha321','youtube':'youtube.com/masha321','telegram'
:'t.me/masha321'},
"Маша":
{'tel':'+7922123561','vk':'vk.com/masha321','youtube':'youtube.com/masha321','telegram'
:'t.me/masha321'},
}

user_input = input("Введите имя из списка контактов: ")

if user_input:
    user_search = user_input[0].upper() + user_input[1:].lower()
else:
    user_search = ""

if user_search in note_book:
    contact = note_book[user_search]
    print(f"Контакт: {user_search}")
    for key, value in contact.items():
        print(f"{key.capitalize()}: {value}")
else:
    print("Контакт не найден.")

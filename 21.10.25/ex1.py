# Основная функция.
# для возврата значений ошибок текста и самого вывода баллов
# буду использовать get_coords для создания возврата значений в кортеж
def scrabble(text):

    #=====
    # Обьявление переменных
    #=====

    # Словарь, слово: балл
    alphabet = {
        # English alphabet
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10,

        # Russian alphabet
        'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'с': 1, 'т': 1,
        'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2, 'р': 2, # "р" не было, на рандом добавил в 2 баллы.
        'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
        'й': 4, 'ы': 4,
        'ж': 5, 'з': 5, 'ч': 5, 'ц': 5,
        'ш': 8, 'э': 8, 'ю': 9,
        'ф': 10, 'щ': 10, 'ъ': 10}

    text = text.replace(' ', '') # убираю пробелы
    text = text.lower() # делаю все символы низкими
    score = 0 # нулевой счетчик баллов
    symb_err = [] # инициализация списка для символов не в алфавите

    # =====
    # Главная логика
    # =====

    for symbol in text:
        if symbol in alphabet:
            score += alphabet[symbol]
        else:
            symb_err.append(symbol)
    return score

# Функция мультиплеера
# Внутри встроена одиночная игра
# и интерактив ввиде выхода, выбора игры и ввода игроков
def parral_game(players):
    players = players.split() # преобразование в список.
    print(len(players))
    if len(players) == 1: # Если игрок один то вопрос переходить ли на одиночный режим
        print("- У вас один игрок\n- Выбираете режим одиночной?")
        print("Yes(1), No(0)")
        subm = int(input(":: "))
        if subm == 1: # Если да то начинается одиночная игра
            onepl_game = input("Введите текст: ")
            resopl = scrabble(onepl_game)
            print(f"Введенное слово: {onepl_game}, счет: {resopl}")
            exit()
        if subm == 0: # Если нет то опрашивается имя игроков
            subm_name = input("Введите снова имена игроков: ")
            subm_name = subm_name.split() # преобразую в список
            subm_name = players # называю его как основной входящий аргумент функции
    if len(players) > 1: # Мультиплеер
        score_list = [] # инициализация игрового списка, индекс игрока == индекс статистики
        for rond in range(1,10+1): # создание цикла на раунд
            print(f"{rond} round")
            for player_index in range(len(players)): # создания цикла на кол-во игроков
                print(f"Ход {players[player_index]}") 
                input_text = input(":: ")
                res = scrabble(input_text)
                score_list.append(res)
                if score_list[player_index] > 0:
                    score_list[player_index] += res
                print(f"Очки :: {score_list[player_index]}")
                print("--след--")
        score_top = max(score_list) # определение победителя
        score_top_index = score_list.index(score_top) # определение имени победителя
        print(f"Выйграл {players[score_top_index]}, результат {score_top}")
        print(f"Список игроков:")
        for num_player in range(len(players)): # создания цикла на вывод списка играющих, не по сортировке
            print(f"- {num_player}: {players[num_player]}, {score_list[num_player]}")
    else: # Выход из игры
        print("!Не веденны игроки, выход.")
        exit()

parral_game(input("- Для выхода из программы нажмите энтер без текста\n- Введите кол-во игроков: "))

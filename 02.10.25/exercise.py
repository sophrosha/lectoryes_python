from random import randint

# Небольшая информация.
# * Это распаковка элементов в списке, множествах списков и тд.
#
# Задания начал возносить в функции без принятия значения
# (если в самом задании не нужно указывать значения).
# Так как легче понимать где задание, чем писать комментарий.

# Задание 1
def task1():
    print("== 1 ЗАДАНИЕ ==")
    list_default = [] # создаем список
    min_num = -10     # Минимальное
    max_num = 10      # Максимальное
    elements = 20     # Кол во элементов

    # Создание списка через рандом
    for _ in range(elements):
        list_default.append(randint(min_num,max_num))
    print("Несорт:", *list_default)

    # Алгоритм пузырька
    for i in range(elements):
        for j in range(elements-1-i):
            if list_default[j] > list_default[j+1]:
                list_default[j], list_default[j+1] = list_default[j+1], list_default[j]
    print("Сорт:", *list_default)

# Задание 2
def task2():
    print("== 2 ЗАДАНИЕ ==")
    # Списки
    list_default = []  # создаем список
    list_even = []     # Создаем четный список
    list_odd = []      # Создаем не четный список
    list_min_max = []  # список min и max

    # Остальное
    min_number = -20   # Минимальное
    max_number = 20    # Максимальное
    elements = 45      # Кол во элементов
    index = 0          # Индекс

    # Создание списка через рандом
    for _ in range(elements):
        list_default.append(randint(min_number,max_number))

    # Алгоритм пузырька
    for i in range(elements):
        for j in range(elements-1-i):
            if list_default[j] > list_default[j+1]:
                list_default[j],list_default[j+1]=list_default[j+1],list_default[j]
    print("Нач список:", *list_default)
    print("Виды сортировок:")

    # Первый вид сортировки:
    while index <= 44:
        if list_default[index] % 2 == 0: list_even.append(list_default[index])
        index+=1
    print(" - 1. четные элементы:", *list_even[:len(list_even)//3])

    # Второй вид сортировки
    print(" - 2. min и max:", 
          min(list_default[:len(list_default)*2//3]), 
          max(list_default[:len(list_default)*2//3])
    )

    # Третий вид сортировки
    index=0 # обнуляю индекс
    while index <= 44:
        if list_default[index] % 2 != 0: list_odd.append(list_default[index])
        index+=1
    print(" - 3. нечетные элементы:", *list_odd[:len(list_default)*3//3])

# Мини бонус, просто хочу сделать ;)
def main():
    value = int(input("Выберите задание(1 или 2): "))
    if value == 1: task1()
    elif value == 2: task2()
    elif value == 0: exit()
    else:
        print("Введено не верное значение")
        main()
main()

#====
# Tasks
#====

def one_task(): # Форматированный текст при помощи табуляции.
    print("\n\"Don\'t compare yourself with anyone in this world...if you do so, you are insulting\nyourself.\""
          "\n\nBill Gates \n")

def two_task(): # Четные числа
    list_numbers=[]
    one_num = int(input("1_число :> "))
    two_num = int(input("2_число :> "))
    for nums in range(one_num,two_num+1):
        if nums%2==0:
            list_numbers.append(nums) # Добавление числа в список
    print("Четные числа:",*list_numbers) # Вывод чисел без скобок через операнд распаковки *

def thr_task(): # Квадрат
    # Перевод булева значения в true или false если у них низкие буквы
    def to_bool(bool_str):
        if bool_str.lower() == "true":
            return True
        elif bool_str.lower() == "false":
            return False
        else:
            return True

    # Интерактивное меню
    def interact():
        print("напишите значения в строку так: \"(ширина) (высота) (Заполнять квадрат(булево значение!) (патерн внутри если заполнять квадрат))\"\n"
              "Обязательно заполнять аргументы через пробел! Допустимо через - или ,")
        answer = input(":> ") # опрашиваю пользователя, как в bash с $1/$2/$n....
        lis = answer.split() # превращаю тип данных в список(все определяется по пробелам)
        cube(int(lis[0]), int(lis[1]), to_bool(lis[2]), lis[3]) # передаю эти значения, так же назначаю на ширину и высоту тип данных int, а на булево значение проверку если оно другое

    # Сам алгоритм(грубо говоря мозги)
    def cube(width, height, bool_fill, pattern):
        if bool_fill == True:
            for height_cube in range(1,height+1):
                print(pattern*width)
        elif bool_fill == False:
            print(pattern*width)
            for height_cube in range(1,height-2):
                print(pattern, " "*(width-4), pattern)
            print(pattern*width)
    interact() # Вызов интерактивного меню

#====
# Main
#====

def main(): # Основные функции
    def tasks(ans): # Модуль перехода к заданиями
        if ans == 1:
            one_task() # Так как задания изолированые, входные аргументы не передаются
        elif ans == 2:
            two_task()
        elif ans == 3:
            thr_task()

    def menu(): # Основной модуль выбора задания
        while True: # Так как программа подразумевает запуск нескольких заданий
                    # Мы делаем цикличную работу, пока не будет выбран 0 для brake.
            print("Домашнее задание от 23.10.25\nВыберите номер задания:\n"
              ":-1 формат текст\t" ":-2 четн числа\n" ":-3 квадрат\t\t"
              ":-0 Выход\n")
            answer = int(input(":> "))
            if answer == 0:
                print(":: exit!")
                break
            tasks(answer) # Переход к модулю перехода к заданиям
    menu()

if __name__ == "__main__": # Используем скрипт как основной а не как импорт
    main()

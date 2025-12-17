#num1 = '' # 1 слаг
#num2 = '' # 2 слаг 
#operation = '' # оператор

# Ввод выражения
#letter_num = 0

# Поиск знака и индекса
#user_str = input("Enter num: ")
#for i in range(0, len(user_str)): 
#    if user_str[i] in "+-*/":
#        letter_num = i
#        operation = user_str[i]

# Поиск 1 числа
#for i in range(0, letter_num):
#    num1 += user_str[i]

# Поиск 2 числа
#for i in range(letter_num + 1, len(user_str)): # увеличение индекса на единицу
#    num2 += user_str[i]

# Преобразование типа
#num1 = int(num1)
#num2 = int(num2)

#if operation == "+":
#    result = num1 + num2
#elif operation == "-":
#    result = num1 - num2
#elif operation == "*":
#    result = num1 * num2
#elif operation == "/":
#    result = num1 / num2
#print("result: ", result)

#===
# Задания
#===

# 1 Задание
# Для того чтоб не показаться что я взял у ии то обьясню что делает код
#num = str(input()) # считывание
#rev = '' # создание пустой строки
#for i in range(len(num) -1, -1, -1): Создание цикла и в радиусе(подсчитать(num) -start, -step, -stop), тоесть от конца
#    rev += num[i] # записывание num в rev с индексом i
#print(rev) 
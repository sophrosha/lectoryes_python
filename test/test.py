import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from menu import Menu # Импортирую модуль, подразумеваю что он в каталоге где и ваш файл.

# Создаю для теста 3 функции
def hi(): 
	print("Hello World")
def name(): 
	ans = int(input("введи имя"))
	print(f"Твое имя {ans}")
def radius():
	for i in range(0,10+1):
		print(i)

# Создаю константу TASKS.
# Примерные значения словаря:
# число_задания: ["описание задания", название_функции]
TASKS = {
	1: ["Вывод hello world", hi],
	2: ["Вывод имени человека", name],
	3: ["Создание радиуса до 10", radius]
}

# Условие проверки не импортирования модуля
# а так же инициализация модуля Menu.
if __name__ == "__main__":
	# Указываю дату выполнения задания, и словарь с заданиями
	info = Menu("25.10.25", TASKS)
	info.Tasks() # Показываю список заданий и их описания
	info.Answer() # Инициализирую опросник

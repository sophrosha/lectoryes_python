# Experiment::monte-carlo
import datetime
from random import randint

def getBirthdays(numberOfBirthDays):
    birthdays = [] # Список дней рожддения
    for i in range(numberOfBirthDays):
        # Год в нашей имитации роли не играет
        # Лишь бы в обьектах дней рождения он был одинаков
        startOfYear = datetime.date(2000,1,1)
        # случайный день года
        randomNumberOfDays = datetime.timedelta(randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
'''
Принимает список дней рождения. обрабатывает его и
возвращает совпадения в датах, кот.
Встречаются несколько раз.
'''

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # даты не совпадают, выход.
    for a, birthdayA in enumerate(birthdays): # enumerate() про списку
        for b, birthdayB in enumerate(birthdays[a+1 : ]):
            if birthdayA == birthdayB:
                return birthdayA # даты совпали

def main():
    # Кортеж мес в году
    MONTHS = ('Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec')
    print("Симуляция совпадения дней рождения")
    while True:
        print("Сколько симуляции хотите сделать?\n PS max=100")
        response = input(":>")
        if response.isdecimal() and 0 < int(response): # Для неограниченного ввода значений убираем <= 100
            numBDats = int(response) # При комментировании прилетает ошибка неопределенного типа данных.
            break
    print()
    # Генерируем и отображаем дни рождения
    day_birth = getBirthdays(numBDats) # Так как существует вторая переменная birthdays, то она перезаписывает данные по новому. По этому при выполнении кода на 59 строке переменная перезаписывается.
    for i, birthday in enumerate(day_birth): # Изменение переменной(43 строка)
        if i != 0:
            print(", ", end='')
        month = MONTHS[birthday.month - 1]
        dateText = "{} {}".format(month, birthday.day)
        print(dateText, end='')
    print()
    print()
    print(f"Генерация {numBDats} случайных симуляции")
    input("Нажмите Enter для старта....")
    print("Запуск 100.000 симуляции")
    simMatch = 0
    for i in range(100_000):
        if i % 1_000 == 0: # меняем число с 10_000 на 1_000
            print(i, " запущена симуляция...")
        birthdays = getMatch(day_birth) # Изменение переменной(43 строка)
        if getMatch(day_birth) != None: # Изменение переменной(43 строка)
            simMatch += 1
    print(":"*11)
    print("Было выполнено 100.000 симуляции.")
    probability = round(simMatch/100_000*100,2)
    print("Процент совпадения",probability)
    print("Кол-во дат для исследования:",numBDats)
    print("Кол-во циклов симуляции:",simMatch)


if __name__ == "__main__":
    main()

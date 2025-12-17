def get_percent(number):
    if 0 <= number < 500:
        return 3
    elif 500 <= number <= 1000:
        return 5
    elif number >= 1000:
        return 8

def salary(manag):
    casing = 200
    percen = manag / 100
    summ = casing * percen
    final = summ + casing
    return final

manager_1 = salary(get_percent(int(input("уровень продаж 1 менеджера :: "))))
manager_2 = salary(get_percent(int(input("уровень продаж 2 менеджера :: "))))
manager_3 = salary(get_percent(int(input("уровень продаж 3 менеджера :: "))))
manager_top = max(manager_1, manager_2, manager_3)
manager_gener = [ manager_1, manager_2, manager_3 ]

def why_manager(top):
    if top == manager_1:
        return 'Менеджер 1'
    elif top == manager_2:
        return 'Менеджер 2'
    elif top == manager_3:
        return 'Менеджер 3'
why_man = why_manager(manager_top)
favor_manager = manager_top + 200



print("Лучший менеджер: {}. Зарплата(с премией): {}$".format(why_man, favor_manager))
print("---")
print("Остальные менеджеры:\n"
      "  - {}$, Первый менеджер\n"
      "  - {}$, Второй менеджер\n"
      "  - {}$, Третий менеджер"
      .format(manager_1, manager_2, manager_3))


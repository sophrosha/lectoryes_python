import sys as os

price_call = int(input("Стоймость разговора, в мин :: "))
operators = [
    "tmobile",
    "t2",
    "mts",
    "yota"
]

print("Список доступных операторов:")
for el in operators:
    print(f" - {el}")

def operator_func(operator_num):
    match operator_num:
        case "tmobile":
            math_num = 3.9 * price_call
            print("{} Rub".format(math_num))
            os.exit(1)
        case "t2":
            math_num = 3.60 * price_call
            print("{} Rub".format(math_num))
            os.exit(1)
        case "mts":
            math_num = 2.5 * price_call
            print("{} Rub".format(math_num))
            os.exit(1)
        case "yota":
            math_num = 2.50 * price_call
            print("{} Rub".format(math_num))
            os.exit(1)
        case _:
            print("Указан оператор не из списка!")
            os.exit(0)

operator_select = input('\n' "Введите оператора из списка :: ")
operator_func(operator_select)




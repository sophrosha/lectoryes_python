import sys

number_input = int(input("Введите число :: "))

if number_input < 100 and number_input > 1:
    if number_input % 3 and number_input % 5:
        print("Fizz Buzz")
        sys.exit(1)
    elif number_input % 3 != 0 and number_input % 5 != 0:
        print(number_input)
        sys.exit(1)
    elif number_input % 3 == 0:
        print("Fizz")
        sys.exit(1)
    elif number_input % 5:
        print("Buzz")
        sys.exit(1)

else:
    print("ОШИБКА! Введено число не в диапазоне")
    sys.exit(1)



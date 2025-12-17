import sys

number = int(input("Введите число :: "))
stage = float(input("Введите степень(0-7) :: "))

if stage <= 7 and stage >= 1:
    numbd = number ** stage
    print("Ответ: {}".format(numbd))
    sys.exit(1)

else:
    print("ОШИБКА, введена степень выше/ниже диапазона")
    sys.exit(1)
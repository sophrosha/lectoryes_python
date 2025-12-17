import random
# Так как меня не было на паре я буду честен,
# некоторые задания смотрел у одногруппницы
# но смотрел как они выполняются.

#===
# Задание 3
#===
print("-= Задание 3 =-")

# Обьявляю переменные
lis = []
n = 15
iterations = 0

# Создание списка из 15 чисел
for i in range(n):
    lis.append(random.randint(1,100))
print(f"1: ", lis)

# Сортировка от большего к меньшему
i = 0
while i < n - 1:
    m,j = i,i+1
    while j < n:
        if lis[j] < lis[m]: 
            m = j
        j += 1
    # меняем местами
    lis[i], lis[m] = lis[m], lis[i]
    i += 1
    iterations += 1
print(f"2: ", lis)
print(f"3: ", iterations)

#===
# Задание 4
#===
print("-= Задание 4 =-")

# обьявляю переменные
words = [ "apple", "banana", "cherry", "date", "apricot" ]
n = len(words)
j = 0

for i in range(1, n):#1-5
    key = words[i]#apple
    j = i - 1#1-1 0
    # Сдвигаем элементы вправо, пока они больше key
    while j >= 0 and words[j] > key:
        words[j + 1] = words[j]
        j -= 1
    words[j + 1] = key
print(words)

#===
# Задание 5
#===
print("-= Задание 5 =-")

# Обьявляю переменные
lisb = ["1", "10", "3", "5", "7", "8"]
k = 2
fix_k = lisb[k]
oth_el = []

for i in range(len(lisb)):
    if i != k:
        oth_el.append(lisb[i])

n = len(oth_el)
for i in range(n):
    for j in range(0, n - i - 1):
        if oth_el[j] > oth_el[j + 1]:
            oth_el[j], oth_el[j + 1] = oth_el[j + 1], oth_el[j]

left_par = oth_el[:k]
right_par = oth_el[k:]

res = left_par + [fix_k] + right_par

print(res)


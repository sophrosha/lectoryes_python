# === Питон михаил петров
import random

#N = 10
#list_sort_buble = []
#for _ in range(N):
#    list_sort_buble.append(random.randint(0,100))
#print(f"Не сортированный список: {list_sort_buble}")

# Сортировка пузырьком
#for i in range(N):
#    for j in range(N - 1 - i):
#        if list_sort_buble[j] > list_sort_buble[j+1]:
#            list_sort_buble[j], list_sort_buble[j+1] = list_sort_buble[j+1], list_sort_buble[j]
#print(f"Отсортированный список: {list_sort_buble}")

#===
# :: Теория
#===

# 2 Пары Артем Данилов
#def hello():
#    print("Hello world")
#hello()

#def one_two(one): # one принимает значения
#    num = one + 1
#    return num
#print(one_two(10))

# Расчитывание круга
#def circle(r):
#    area = 3.14*r*r
#    return area
#print(circle(10))

# Факториал
# 5! = 5*4*3*2*1
# 0! = 1
# 6! = 6 * 5!
# n! = n * (n-1)!

# Рекурсия
#def f(n):
#    if n == 1: return n
#    return n * f(n-1) # рекурсивная функция, вызывающая саму себя.
#print(f(5))

#===
# :: Задания
#===

# 1 task
#def rectg(a,b):
#    return (a+b)*2
#print(rectg(20,5))

# 2 task
#def chetnoe(numb):
#    if numb%2==0: return numb
#    else: return numb+1
#print(f"четное: {chetnoe(2)}, нечетное: {chetnoe(3)}")

# 3 task
#cel=5
#def cel_far(gr):
#    return (gr*9/5)+32
#print(f"Цельсий {cel}, Фаренгейт: {cel_far(cel)}")

# 4 task
#def sechour(secn):
#    return secn/3600
#print(sechour(1000))

# 5 task
#def month(numbs):
#    if numbs in [4,6,9,11]: # Если число равен значению в списке то вывести то число месяца
#        return 30
#    if numbs in [1,3,5,7,8,10,12]:
#        return 31
#    if numbs in 2:
#        return 28
#    else:
#        return "nin"
#print(month(5))


#===
# Практика рекурсия
#===

#def num_aver(a,b,c):
#    return (a+b+c)/3
#print(num_aver(2,3,5))

#def num_mezdu(a,b,c):

# 1 решение а не if
#   if a<=b<=c or c<=b<=a:
#       return b
#   elif b<=a<=c or c<=a<=b:
#       return a
#   else:
#       return c

# 2 решение в одну строку
#   sorted([a,b,c])[1]

#print(num_mezdu(1,2,3))

#def num_mod(a,b,c):
#    if a == b or b == c:
#        return b
#    if b == c or c == a:
#        return c
#    if c == a or a == b:
#        return a
#    else:
#        return a,b,c
#print(num_mod(3,3,3))

#def nat_num(a):
#    total=0
#    for i in range(1, a+1):
#        total+=i
#    return total
#print(nat_num(5))
#2 задание
b = input()
lis = [int(ind) for ind in b]
b_min = b[0]
print(f"минимум: {b_min} список: {b}")

#3 задание
b = input()
lis = [int(i) for i in b]
index_num = 0
std_num = 0
while True:
    if lis[index_num] <= 1:
        std_num += 1
    elif lis[index_num] <= 1:
        std_num += 1
    elif lis[index_num] % 2 == 0 or lis[index_num] % 3 == 0:
        std_num += 1
    index_num += 1
    if index_num == len(lis) - 1:
        print(f"Кол во простых чисел: {std_num}, список: {lis}")

#4 задание
list = [1, 2, 3, 4, 5, 6, 10, 22, 343, 4]
num_input = int(input())
del_list = list.remove(num_input)
print(f"удаленные элементы: {num_input} \n список: {list}")

#5 задание
list1 = [1, 2, 3, 4, 5]
list2 = [100, 200, 300, 200]
def lis_obe(lis1, lis2):
    return lis1 + lis2
print(lis_obe(list1, list2))

# 6 задание
spisok = [1, 2, 3, 4, 10, 12]
stepen = 2
print([i ** stepen for i in spisok])

from time import time
from random import randint

'''
start = time()

for i in range(100_000_00):
    x = i

finish = time()
print(finish - start)



SIZE = 100_100
def append_time():
    start = time()
    arr = []
    for i in range(SIZE):
        arr.append(1)
    finish = time()
    print("append:", finish - start)

def insert_time():
    start = time()
    arr = []
    for i in range(SIZE):
        arr.insert(0, 1)
    finish = time()
    print("insert:", finish - start)


START_ELEMENT_NUMBER = 1
END_ELEMENT_NUMBER = 1_000_000_000_000
ARR_NUMBER_SIZE = 1_000_000

def append_time():
    arr = {}
    start = time()
    for i in range(ARR_NUMBER_SIZE):
        arr[i] = (randint(START_ELEMENT_NUMBER, END_ELEMENT_NUMBER))
    finish = time()
    result = finish - start
    return result

def generate_list():
    _list = []
    start = time()
    for i in range(ARR_NUMBER_SIZE):
        _list.append(randint(START_ELEMENT_NUMBER, END_ELEMENT_NUMBER))
    finish = time()
    result = finish - start
    return result, _list

def find_number_in_list():
    _result, _list = 0, generate_list()
    for i in _list:
        generated_element = randint(START_ELEMENT_NUMBER, END_ELEMENT_NUMBER)
        if generated_element == i:
            _result += 1
    return _result

generated_list, _ = generate_list()
print("arr:", append_time())
print("list:", generated_list)
print("Searched elements in list", find_number_in_list())
'''

one = [int(i) for i in range(10)]
two = [int(i) for i in range(10_000)]
three = [int(i) for i in range(10_000_000)]

def call_list():
    INDEX = 5
    start_one = time()
    for i in range(1_000):
        one[INDEX]
    end_one = time()

    start_two = time()
    for i in range(1_000):
        two[INDEX]
    end_two = time()

    start_three = time()
    for i in range(1_000):
        three[INDEX]
    end_three = time()

    one_result, two_result, three_result = end_one - start_one, end_two - start_two, end_three - start_three
    return one_result, two_result, three_result

def find_sum():
    start_one = time()
    for _ in range(1000):
        sum(one)
    end_one = time()

    start_two = time()
    for _ in range(1000):
        sum(two)
    end_two = time()

    start_three = time()
    for _ in range(1000):
        sum(three)
    end_three = time()

    one_result, two_result, three_result = end_one - start_one, end_two - start_two, end_three - start_three
    return one_result, two_result, three_result

def main():
    print("->")
    one_dot_call, two_dot_call, three_dot_call = call_list()
    print("->>")
    one_dot_find, two_dot_find, three_dot_find = find_sum()
    print("->>>")
    print(f"call list: \n 10: {one_dot_call},\n 10_000: {two_dot_call},\n 100_000: {three_dot_call}\n")
    print(f"find list: \n 10: {one_dot_find},\n 10_00: {two_dot_find},\n 100_000: {three_dot_find}")

if __name__ == "__main__":
    main()
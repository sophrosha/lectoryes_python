# Задача 1
def circle_stats(radius):
    pi = 3.14159
    circuit = 2 * pi * radius
    square = pi * (radius ** 2)
    return (circuit, square)

# Задача 2
def count_vowels(text):
    dict = {}
    for kirilic in text:
        if kirilic in dict:
            dict[kirilic] = dict[kirilic] + 1
        else:
            dict[kirilic] = 1
    return dict

# Задача 3
def fizzbuzz_sum(n):
    cout = 0
    for num in range(1, n):
        if num % 3 == 0:
            continue
        elif num % 5 == 0:
            continue
        else:
            cout += num
    return cout

# Задача 4
def remove_duplicates_sorted(list):
    non_duplicates = []
    for num in list:
        if num in non_duplicates:
            continue
        else:
            non_duplicates.append(num)
    n = len(non_duplicates)
    for i in range(n):
        for j in range(0, n - i - 1):
            if non_duplicates[j] > non_duplicates[j + 1]:
                non_duplicates[j], non_duplicates[j + 1] = non_duplicates[j + 1], non_duplicates[j]
    return non_duplicates

# Задача 5
def merge_dicts(dict1, dict2):
    dicts = {**dict1, **dict2}
    for key, value in dicts.items():
        if key in dicts:
            cout += value
    return cout

# Задача 6
def rw_file():
    file = numbers.txt
    new_file = filtered.txt
    list = []
    with open(file, 'r', encoding='utf-8') as file_opened:
        file_opened = file_opened.readlines()
        for line in file_opened:
            i = int(line.strip())
            if i % 2 == 0:
                list.append(i)
            elif i > 0:
                list.append(i)
    with open(new_file, 'w', encoding='utf-8') as file_opened:
        for element in list:
            file.write("\n".join(element))

# Задача 7
def apply_to_list(func, lst):
    new_list = []
    for element in lst:
        apply_element = func(element)
        new_list.append(apply_element)
    return new_list

# Задача 8
def safe_divide(a, b):
    try:
        a, b = int(a), int(b)
        result = a / b
        return result
    except ZeroDivisionError:
        return "Ошибка"
    except TypeError:
        return "Ошибка"
    except ValueError:
        return "Ошибка"

# Задача 9
def csv_math():
    file = "students.csv"
    new_file = "new_students.csv"
    list_values_new = []
    with open(file, 'r', encoding='utf-8') as file_opened:
        file_opened = file_opened.readlines()
        for line in file_opened:
            line = line.strip()
            list_values = line.split(',')
            list_new = []
            for values in list_values:
                if isinstance(values, str):
                    list_values_aft.append(values)
                elif not values:
                    list_values_aft.append(0)
                else:
                    list_values_aft.append(values)
            cout_values = (list_new[1] + list_new[2] + list_new[3]) / 3
            list_values_new.append("{}, {}".format(list_new[0], cout_values))
    with open(new_file, 'w', encoding='utf-8') as file_opened:
        for element in list_values_new:
            file_opened.write("\n", join(element))

# Задача 10
def text_analyzer(text):
    dict = {}
    #char_count
    dict['char_count'] = text.strip()
    #word_count
    dict['word_count'] = len(text.split(' '))
    #sentence_count
    dict['sentence_count'] = len(text.replace('!', '.').replace('?', '.').split('.'))
    #most_common_word
    text_most = max(set(text), key=text)
    dict['most_common_word'] = text_most
    return dict

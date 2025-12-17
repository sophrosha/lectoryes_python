# Файлы питон
'''
Типы файлов:
    1. Текстовые(*.txt, *.rtf, *.json)
    2. Бинарные(*.bin)
Операции:
    1. Открытие файлв
    2. Чтение\Запись
    3. Закрытие файла

f = open(file_name, access_mode) # чтение записи
access_mode = режим открытия файла

r,w = чтение/запись Онли!
Создает новый файл, если его нету
rb/wb = чтение/запись Бинарно!
r+ = чтение и запись
w+ = чтение и запись
rb+ = чтение и запись Бинарно!
wb+ = чтение и запись Бинарно!
a = обновление содержимого
a+ = обновление содержимого
ab = тоже самое, бинарное
ab+ = тоже самое, бинарное
'''

#f = open('example.txt','r')
#print(f) # вывод информации об обьекте.
#print(*f) # Вывод текста внутри
#f.close

#with open('example.txt', 'r') as f:
#    f.write("Hello World")
#with open('example.txt', 'w') as f:
#    print(f.read(4))
#with open('example.txt', 'a') as f:
#    f.write("Хай\n")
#    f.write("Слава NixOS\n")
#with open('example2.txt','r') as f:
#    print(f.read())

'''
f.readline() - Чтение строки, с указанием номера
f.readlines() - Чтение всех строк
f.fileno() - дескриптор файла в числе
f.flush() - очистка внутреннего буфера
f.isatty() - возвращает истину, если файл привязан к транскриптору
f.next() - возвращает след строку файла
f.seek() - находит строку файла
f.seekable() - проверяет, поддерживает ли файл случайный доступ
f.tell() - получает позицию в файле
f.truncate() - уменьшает размер файла стирая данные
f.writelines(list[]) - записывает последовательность файла
'''
import os


def file_collector(path):
    path = os.path.normpath(path)
    result = {'dirs': [], 'files': []}
    for pths, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result['dirs'].append(dir)
        for file in filenames:
            result['files'].append(file)
    with open('skiper.txt', 'w') as f:
        f.write("\n {:<50} \n".format("Directories"))
        for dir in result['dirs']:
            f.write(f"\n {dir} \n")
        f.write("\n {:<50} \n".format("Files"))
        for file in result['files']:
            f.write(f"\n {file} \n")


path = "C:\intel"
file_collector(path)

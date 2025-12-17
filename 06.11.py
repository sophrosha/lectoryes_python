import math


# Работа с вещественными числами.
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


class task:
    def __init__(self) -> None:
        self.x = [i for i in frange(0, 0.5, 6)]
        self.y1 = [(1 + abs(i)) / (math.sqrt(1 + i + i * i)) for i in self.x]
        self.y2 = [(1 + math.cos(i) ** 4) / (3 + i) for i in self.x]
        self.file = 'test.txt'

    # Создание data.txt для записи данных в столбцы
    def create_file(self) -> bool:
        with open(self.file, 'w', encoding='utf-8') as outfile:
            outfile.write('# значения x, y1 и y2\n')
            for xi, yli, y2i in zip(self.x, self.y1, self.y2):
                outfile.write('%10.5f %10.5f %10.5f\n' % (xi, yli, y2i))
        outfile.close()
        return True

    # Находим сумму значений y=y1+y2
    def summ_values(self) -> list:
        result = map(lambda i1, i2: i1 + i2, self.y1, self.y2)
        return list(result)

    # Добавление результата x и y в data.txt из двух колонок
    def result(self) -> bool:
        with open(self.file, 'a', encoding='utf-8') as outfile:
            outfile.write('# Результат задания x и y\n')
            for xi, yli in zip(self.x, self.summ_values()):
                outfile.write('%10.5f %10.5f\n' % (xi, yli))
            outfile.close()
            return True


# Инициализация
if __name__ == "__main__":
    init = task()
    init.create_file()
    init.summ_values()
    init.result()

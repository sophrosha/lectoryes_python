from auto import Auto

if __name__ == '__main__':
    car = Auto(
        'Жигули',
        'Красный',
        'ВАЗ-2101',
          50,
        4,
         100,
         True
    )

    car.refuel(30)
    car.light()
    car.move()
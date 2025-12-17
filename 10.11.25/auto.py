class Auto:
    def __init__(self, name, color, model, fuel, wheels, speed, light1):
        self.name = name
        self.color = color
        self.model = model
        self.fuel = fuel
        self.wheels = wheels
        self.speed = speed
        self.light1 = light1

    def move(self):
        distance = 1
        fel = self.fuel
        print(f"Начато движение, скорость: {self.speed}")
        if fel > 0:
            while fel > 0:
                print(f"Машина проехала {distance}")
                fel -= 1
                distance += 1
                print(f"Осталось топливо {fel}")
        else:
            print("Топливо отсуствует")
        print(f"Машина остановилась, топливо {fel}")

    def light(self):
        if self.light1 == True:
            print("Фары включенны")
        else:
            print("Фары выключенны")

    def refuel(self, value_fuel):
        if value_fuel < 0:
            print("Машина не заправленна, пропуск")
        else:
            self.fuel += value_fuel
            print(f"Машина заправленна, кол-во топлива {self.fuel}")
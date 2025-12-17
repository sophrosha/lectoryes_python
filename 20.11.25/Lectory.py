# nasledovanie
#class Person:
#    def __init__(self, name):
#        self.__name = name

#    def getname(self):
#        return self.__name

#    def display_info(self):
#        print(f"Name {self.getname}")

#class employee(Person):
#    def work(self):
#        print(f"{self.getname} works")

#def main():
#    tom = employee("Tom")
#    print(tom.getname())
#    tom.display_info().
#    tom.work()

#if __name__ == "__main__":
#    main()
from random import randint

class NPC:
    def __init__(self, name, hp) -> None:
        self.__name = name
        self.__hp = hp

    def __str__(self) -> str:
        return f"Зовут {self.name()}, здоровье: {self.hp()}"

    def attack(self) -> int:
        return self.hp - randint(0, 12)

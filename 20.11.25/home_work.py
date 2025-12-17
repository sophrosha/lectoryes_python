from random import randint

NPC_DAMAGE_MAX = 10
SWORDSMAN_DAMAGE_MAX = 50
MAGE_DAMAGE_MAX = 100
START_NUMBER = 0

class npc:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def __str__(self):
        return f"Имя игрока: {self.name}, здоровье: {self.hp}"

    def attack(self):
        return randint(START_NUMBER, NPC_DAMAGE_MAX)

class swordsman(npc):
    def __init__(self, name, hp,
                 min_damage, max_damage):
        super().__init__(name, hp)
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        return randint(START_NUMBER, SWORDSMAN_DAMAGE_MAX)

class mage(npc):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self):
        return randint(START_NUMBER, MAGE_DAMAGE_MAX)
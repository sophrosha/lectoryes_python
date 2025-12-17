import random

class Snail:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.is_sleeping = False
        self.is_drifting = False
        self.finished = False
        self.max_num_snails = 20
        self.max_name_length = 10
        self.finish_line = 40

    def move(self):
        # Улитка, уже финишировавшая, не двигается
        if self.finished:
            return

        if self.is_sleeping:
            return

        # Шанс ускорения (дрифт)
        if random.random() < 0.1:
            self.is_drifting = True
            step = random.randint(3, 6)
        else:
            self.is_drifting = False
            step = random.randint(0, 2)

        self.position += step
        if self.position >= self.finish_line:
            self.position = self.finish_line
            self.finished = True

    def sleep(self):
        if self.finished:
            return
        # Шанс уснуть
        if not self.is_sleeping and random.random() < 0.05:
            self.is_sleeping = True
        # Шанс проснуться
        elif self.is_sleeping and random.random() < 0.3:
            self.is_sleeping = False
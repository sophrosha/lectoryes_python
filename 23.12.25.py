import random
import tkinter as tk
import sys

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

NUMBER_OF_LOGOS = 1
PAUSE_AMOUNT = 20  # в миллисекундах для after()
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


class LogoBouncer:
    def __init__(self, root):
        self.root = root
        self.root.title("DVD Logo Bouncer")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(root, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.width = 800
        self.height = 600
        self.logos = []

        self.canvas.bind('<Configure>', self.on_resize)
        self.create_logos()
        self.animate()

    def on_resize(self, event):
        self.width = event.width
        self.height = event.height

    def create_logos(self):
        for _ in range(NUMBER_OF_LOGOS):
            logo = {
                COLOR: random.choice(COLORS),
                X: random.randint(50, self.width - 50),
                Y: random.randint(50, self.height - 50),
                DIR: random.choice([UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT])
            }
            logo['id'] = self.canvas.create_text(
                logo[X], logo[Y],
                text="DVD",
                fill=logo[COLOR],
                font=('Arial', 24, 'bold')
            )
            self.logos.append(logo)

    def update_position(self, logo):
        if logo[DIR] == UP_RIGHT:
            logo[X] += 5
            logo[Y] -= 5
        elif logo[DIR] == UP_LEFT:
            logo[X] -= 5
            logo[Y] -= 5
        elif logo[DIR] == DOWN_RIGHT:
            logo[X] += 5
            logo[Y] += 5
        elif logo[DIR] == DOWN_LEFT:
            logo[X] -= 5
            logo[Y] += 5

        text_width = 60
        text_height = 30

        if logo[X] <= text_width // 2 and logo[Y] <= text_height // 2:
            logo[DIR] = DOWN_RIGHT
            self.change_logo_color(logo)
        elif logo[X] <= text_width // 2 and logo[Y] >= self.height - text_height // 2:
            logo[DIR] = UP_RIGHT
            self.change_logo_color(logo)
        elif logo[X] >= self.width - text_width // 2 and logo[Y] <= text_height // 2:
            logo[DIR] = DOWN_LEFT
            self.change_logo_color(logo)
        elif logo[X] >= self.width - text_width // 2 and logo[Y] >= self.height - text_height // 2:
            logo[DIR] = UP_LEFT
            self.change_logo_color(logo)
        elif logo[X] <= text_width // 2:
            logo[X] = text_width // 2
            if logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
                self.change_logo_color(logo)
            elif logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
                self.change_logo_color(logo)
        elif logo[X] >= self.width - text_width // 2:
            logo[X] = self.width - text_width // 2
            if logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
                self.change_logo_color(logo)
            elif logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
                self.change_logo_color(logo)
        elif logo[Y] <= text_height // 2:
            logo[Y] = text_height // 2
            if logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
                self.change_logo_color(logo)
            elif logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
                self.change_logo_color(logo)
        elif logo[Y] >= self.height - text_height // 2:
            logo[Y] = self.height - text_height // 2
            if logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
                self.change_logo_color(logo)
            elif logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
                self.change_logo_color(logo)

    def change_logo_color(self, logo):
        new_color = random.choice(COLORS)
        while new_color == logo[COLOR]:
            new_color = random.choice(COLORS)
        logo[COLOR] = new_color
        self.canvas.itemconfig(logo['id'], fill=new_color)

    def animate(self):
        for logo in self.logos:
            self.update_position(logo)
            self.canvas.coords(logo['id'], logo[X], logo[Y])

        self.root.after(PAUSE_AMOUNT, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    app = LogoBouncer(root)

    def on_closing():
        root.destroy()
        sys.exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
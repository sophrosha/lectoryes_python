import tkinter as tk
import random


class FifteenPuzzle:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Пятнашки")
        self.size = 4
        self.buttons = []
        self.steps = 0
        self.steps_label = None
        self.empty_row = self.size - 1
        self.empty_col = self.size - 1
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)
        self.steps_label = tk.Label(top_frame, text="Шаги: 0", font=("Arial", 14))
        self.steps_label.pack(side=tk.LEFT, padx=10)
        restart_button = tk.Button(top_frame, text="Рестарт", command=self.new_game)
        restart_button.pack(side=tk.RIGHT, padx=10)
        game_frame = tk.Frame(self.root)
        game_frame.pack()

        for row in range(self.size):
            button_row = []
            for col in range(self.size):
                btn = tk.Button(
                    game_frame,
                    text="",
                    width=6,
                    height=3,
                    command=lambda r=row, c=col: self.click(r, c)
                )
                btn.grid(row=row, column=col, padx=2, pady=2)
                button_row.append(btn)
            self.buttons.append(button_row)

    def new_game(self):
        numbers = list(range(1, self.size * self.size))
        random.shuffle(numbers)
        numbers.append(0)

        index = 0
        for row in range(self.size):
            for col in range(self.size):
                value = numbers[index]
                if value == 0:
                    self.empty_row = row
                    self.empty_col = col
                    self.buttons[row][col].config(text="", state=tk.DISABLED)
                else:
                    self.buttons[row][col].config(text=str(value), state=tk.NORMAL)
                index += 1

        self.steps = 0
        self.update_steps_label()

    def update_steps_label(self):
        self.steps_label.config(text=f"Шаги: {self.steps}")

    def click(self, row, col):
        if self.is_adjacent(row, col):
            self.swap_tiles(row, col)
            self.steps += 1
            self.update_steps_label()
            if self.is_solved():
                self.show_win_message()

    def is_adjacent(self, row, col):
        return (
            (abs(row - self.empty_row) == 1 and col == self.empty_col) or
            (abs(col - self.empty_col) == 1 and row == self.empty_row)
        )

    def swap_tiles(self, row, col):
        self.buttons[self.empty_row][self.empty_col].config(
            text=self.buttons[row][col].cget("text"),
            state=tk.NORMAL
        )
        self.buttons[row][col].config(text="", state=tk.DISABLED)
        self.empty_row, self.empty_col = row, col

    def is_solved(self):
        expected = 1
        for row in range(self.size):
            for col in range(self.size):
                if row == self.size - 1 and col == self.size - 1:
                    return True
                text = self.buttons[row][col].cget("text")
                if text == "" or int(text) != expected:
                    return False
                expected += 1
        return True

    def show_win_message(self):
        win_window = tk.Toplevel(self.root)
        win_window.title("Победа!")
        label = tk.Label(win_window, text=f"Вы выиграли!\nШагов: {self.steps}", font=("Arial", 16))
        label.pack(padx=20, pady=20)
        button = tk.Button(win_window, text="Закрыть", command=win_window.destroy)
        button.pack(pady=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = FifteenPuzzle()
    game.run()
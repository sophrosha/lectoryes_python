import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.x_score = 0
        self.o_score = 0
        self.current_player = True

        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

        self.score_label = tk.Label(
            self.window,
            text=f"X: {self.x_score}   O: {self.o_score}",
            font=("normal", 16)
        )
        self.score_label.grid(row=0, column=0, columnspan=3)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.window,
                    text="",
                    font=("normal", 40),
                    width=4,
                    height=2,
                    command=lambda r=i, c=j: self.make_move(r, c)
                )
                btn.grid(row=i + 1, column=j, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)

        self.reset_button = tk.Button(
            self.window,
            text="Сброс",
            font=("normal", 14),
            command=self.reset_game
        )
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.window.mainloop()

    def make_move(self, row, col):
        if self.buttons[row][col]["text"] != "":
            return

        mark = "X" if self.current_player else "O"
        self.buttons[row][col]["text"] = mark
        self.board[row][col] = mark

        if self.check_winner():
            if self.current_player:
                self.x_score += 1
            else:
                self.o_score += 1
            self.update_score()
            self.disable_buttons()
        elif self.is_board_full():
            pass
        else:
            self.current_player = not self.current_player

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn["state"] = "disabled"

    def update_score(self):
        self.score_label.config(text=f"X: {self.x_score}   O: {self.o_score}")

    def reset_game(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["state"] = "normal"
        self.current_player = True

if __name__ == "__main__":
    game = TicTacToe()
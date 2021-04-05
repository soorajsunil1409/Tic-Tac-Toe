from tkinter import *

board = [
    ["0", "0", "0"],
    ["0", "0", "0"],
    ["0", "0", "0"]
]

class Board:
    btn_stats = []
    def __init__(self, win, size):
        self.win = win
        self.size = size
        self.create_board()
        self.update_btns()

    def create_board(self):
        for i in range(len(board)):
            for j in range(len(board[0])):
                a = Button(text="")
                a.place(x=self.size[0]/3*j, y=self.size[0]/3*i, height=self.size[0]/3, width=self.size[0]/3)
                self.btn_stats.append((a, board[i][j]))

        print(self.btn_stats)

    def update_btns(self):
        for btn in self.btn_stats:
            btn[0].config(text=btn[1])

if __name__ == "__main__":
    win = Tk()
    win.title("Tic - Tac - Toe")
    win.resizable(False, False)
    win.geometry("600x600")
    app = Board(win, (600, 600))
    win.mainloop()

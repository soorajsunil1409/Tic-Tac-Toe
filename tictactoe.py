from tkinter import *

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
size = (600, 700)

class Board:
    btn_stats = []
    current = "X"

    def __init__(self, win, size):
        self.win = win
        self.size = size

    def create_board(self):
        for i in range(len(board)):
            for j in range(len(board[0])):
                a = Button(text="", font=("Helvetica", 40), disabledforeground="white")
                a.place(x=self.size[0]/3*j, y=self.size[0]/3*i, height=self.size[0]/3, width=self.size[0]/3)
                self.btn_stats.append(a)

        print(self.btn_stats)

    def update_btns(self):
        for btn in self.btn_stats:
            btn.config(text="")

    def init_bindings(self):
        for btn in self.btn_stats:
            btn.bind("<Button-1>", self.write)

    def write(self, e):
        btn = e.widget
        if btn["state"] == NORMAL: btn.config(text=self.current)
        btn["state"] = DISABLED
        self.flip()

    def flip(self):
        self.current = "X" if self.current == "O" else "O"

    def reset(self, e):
        self.current = "X"
        self.update_btns()


def main():
    win = Tk()
    win.title("Tic - Tac - Toe")
    win.resizable(False, False)
    win.geometry("600x700")

    app = Board(win, size)
    app.create_board()
    app.update_btns()
    app.init_bindings()

    reset_btn = Button(text="Reset", font=("Helvetica", 40))
    reset_btn.place(x=0, y=size[0], width=size[0], height=abs(size[1]-size[0]))
    reset_btn.bind("<Button-1>", app.reset)

    win.mainloop()


if __name__ == "__main__":
    main()


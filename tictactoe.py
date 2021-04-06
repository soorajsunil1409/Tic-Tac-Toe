from tkinter import *
from tkinter import messagebox

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
size = (723, 823)

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

    def update_btns(self):
        for btn in self.btn_stats:
            btn.config(text="")
        self.enable_all_btns()

    def init_bindings(self):
        for btn in self.btn_stats:
            btn.bind("<Button-1>", self.write)

    def write(self, e):
        btn = e.widget
        if btn["state"] == NORMAL: 
            btn.config(text=self.current)
            self.win.update()
            btn["state"] = DISABLED
            self.check_win()
            self.flip()

    def flip(self):
        self.current = "X" if self.current == "O" else "O"

    def reset(self, e):
        self.current = "X"
        self.update_btns()

    def disable_all_btns(self):
        for btn in self.btn_stats:
            btn["state"] = DISABLED

    def enable_all_btns(self):
        for btn in self.btn_stats:
            btn["state"] = NORMAL

    def check_win(self):
        btn = self.btn_stats
        if (
            (btn[0]["text"] == "X" and btn[1]["text"] == "X" and btn[2]["text"] == "X") or (btn[0]["text"] == "O" and btn[1]["text"] == "O" and btn[2]["text"] == "O") or
            (btn[3]["text"] == "X" and btn[4]["text"] == "X" and btn[5]["text"] == "X") or (btn[3]["text"] == "O" and btn[4]["text"] == "O" and btn[5]["text"] == "O") or
            (btn[6]["text"] == "X" and btn[7]["text"] == "X" and btn[8]["text"] == "X") or (btn[6]["text"] == "O" and btn[7]["text"] == "O" and btn[8]["text"] == "O") or

            (btn[0]["text"] == "X" and btn[3]["text"] == "X" and btn[6]["text"] == "X") or (btn[0]["text"] == "O" and btn[3]["text"] == "O" and btn[6]["text"] == "O") or
            (btn[1]["text"] == "X" and btn[4]["text"] == "X" and btn[7]["text"] == "X") or (btn[1]["text"] == "O" and btn[4]["text"] == "O" and btn[7]["text"] == "O") or
            (btn[2]["text"] == "X" and btn[5]["text"] == "X" and btn[8]["text"] == "X") or (btn[2]["text"] == "O" and btn[5]["text"] == "O" and btn[8]["text"] == "O") or
            
            (btn[0]["text"] == "X" and btn[4]["text"] == "X" and btn[8]["text"] == "X") or (btn[0]["text"] == "O" and btn[4]["text"] == "O" and btn[8]["text"] == "O") or
            (btn[2]["text"] == "X" and btn[4]["text"] == "X" and btn[6]["text"] == "X") or (btn[2]["text"] == "O" and btn[4]["text"] == "O" and btn[6]["text"] == "O")
        ):
            messagebox.showinfo("YAY!!!", f"{self.current} won the match")
            self.disable_all_btns()
        elif (btn[0]["text"] != "" and btn[1]["text"] != "" and btn[2]["text"] != "" and btn[3]["text"] != "" and btn[4]["text"] != "" and btn[5]["text"] != "" and btn[6]["text"] != "" and btn[7]["text"] != "" and btn[8]["text"] != ""):
            messagebox.showinfo("TIE!!!", f"The match was a tie!!")
            self.disable_all_btns()
            


def main():
    win = Tk()
    win.title("Tic - Tac - Toe")
    win.resizable(False, False)
    win.geometry(f"{size[0]}x{size[1]}")

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


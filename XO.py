# -*- coding: utf-8 -*-
import tkinter

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.window = window
        self.add_lines()

    def add_lines(self, *coords):
        coords = (
            (100, 0, 100, 300),
            (200, 0, 200, 300),
            (0, 100, 300, 100),
            (0, 200, 300, 200)
        )
        for coord in coords:
            self.create_line(coord)
#    def add_o(self, state):
#        self.creare_oval()

window = tkinter.Tk()
game = TicTacToe(window)

game.pack()
window.mainloop()

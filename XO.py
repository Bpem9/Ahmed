# -*- coding: utf-8 -*-
import tkinter

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.window = window
        self.add_lines()
        self.state = [None]*9
        self.bind('<Button-1>', self.click)

    def add_lines(self):
        coords = (
            (100, 0, 100, 300),
            (200, 0, 200, 300),
            (0, 100, 300, 100),
            (0, 200, 300, 200)
        )
        for coord in coords:
            self.create_line(coord)
#    def add_o(self, state):
#        self.create_oval()
    def add_x(self, column, row):
        self.row = row
        self.column = column
        x = {1 : '50', 2 : '100', 3 : '150'}
        y = {1 : '50', 2 : '100', 3 : '150'}
        coords = (
            (x[column] - 25, y[row] - 25, x[column] + 25, y[row] + 25),
            (x[column] + 25, y[row] - 25, x[column] - 25, y[row] + 25)
        )
        for coord in coords:
            self.create_line(coord)
    def click(self, event):
        if event.y < 100:
            if event.x < 100:
                position = 0
            elif event.x > 100 | event.x < 200:
                position = 1
            elif event.x > 200:
                position = 2
        elif event.y > 100 | event.y < 200:
            if event.x < 100:
                position = 3
            elif event.x > 100 | event.x < 200:
                position = 4
            elif event.x > 200:
                position = 5
        else:
            if event.x < 100:
                position = 6
            elif event.x > 100 | event.x < 200:
                position = 7
            elif event.x > 200:
                position = 8
        col = event.x // 100
        r = event.y // 100


window = tkinter.Tk()
game = TicTacToe(window)

game.pack()
window.mainloop()

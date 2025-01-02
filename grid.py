import pygame as pg
import random

class Grid:
    def __init__ (self,width,height,cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        #creates a 3d array of row x columns filled with 0's
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self,window):
        for row in range(self.rows):
            for col in range(self.columns):
                colour = (237,183,7) if self.cells[row][col] else (55,55,55)
                pg.draw.rect(window,colour,(col * self.cell_size, row * self.cell_size, self.cell_size-1, self.cell_size-1)) #cell-size - 1 to give the illusion of grid lines
                

    def fill_randomly(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([0,0,0,1])

    def clear_grid(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0

    def toggle_cell(self,row,col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.cells[row][col] = not self.cells[row][col]


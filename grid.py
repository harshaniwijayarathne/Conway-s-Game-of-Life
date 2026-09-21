import random

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        # 2D array
        # 0 = dead cell
        # 1 = live cell
        self.cells = [
            [0 for _ in range(columns)]
            for _ in range(rows)
        ]

    def randomize(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([0, 0, 0, 1])

    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0
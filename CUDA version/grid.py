import numpy as np

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        # NumPy 2D array for CUDA compatibility (0 = dead cell, 1 = live cell)
        self.cells = np.zeros((rows, columns), dtype=np.int32)

    def randomize(self):
        # Randomly fill grid with 0s and 1s using NumPy
        self.cells = np.random.choice([0, 0, 0, 1], size=(self.rows, self.columns)).astype(np.int32)

    def clear(self):
        self.cells.fill(0)
from grid import Grid

class Simulation:
    def _init_(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)

    def draw(self, window):   
        self.grid.draw(window) 
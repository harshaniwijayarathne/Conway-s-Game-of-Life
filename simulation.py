from grid import Grid

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbours(self, grid, row, column):  
        live_neighbors = 0

        neighbor_offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for offset in neighbor_offsets:
            if self.grid.cells[row + offset[0]][column + offset[1]] == 1:
                live_neighbors += 1

        return live_neighbors        
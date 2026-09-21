from grid import Grid

class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbours(self, grid, row, column):  
        live_neighbors = 0

        neighbor_offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for offset in neighbor_offsets:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:
                live_neighbors += 1

        return live_neighbors        
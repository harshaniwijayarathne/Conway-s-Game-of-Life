from grid import Grid

class Simulation:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid = Grid(rows, columns)
        self.temp_grid = Grid(rows, columns)

    def count_live_neighbours(self, row, column):

        live_neighbors = 0

        for row_offset in [-1, 0, 1]:
            for column_offset in [-1, 0, 1]:

                # Don't count the cell itself
                if row_offset == 0 and column_offset == 0:
                    continue

                new_row = row + row_offset
                new_column = column + column_offset

                # Boundary check
                if (
                    0 <= new_row < self.rows
                    and
                    0 <= new_column < self.columns
                ):
                    if self.grid.cells[new_row][new_column] == 1:
                        live_neighbors += 1

        return live_neighbors

    def update(self):

        for row in range(self.rows):
            for column in range(self.columns):

                live_neighbors = self.count_live_neighbours(
                    row,
                    column
                )

                current_cell = self.grid.cells[row][column]

                # Live cell
                if current_cell == 1:

                    if live_neighbors == 2 or live_neighbors == 3:
                        self.temp_grid.cells[row][column] = 1
                    else:
                        self.temp_grid.cells[row][column] = 0

                # Dead cell
                else:

                    if live_neighbors == 3:
                        self.temp_grid.cells[row][column] = 1
                    else:
                        self.temp_grid.cells[row][column] = 0

        # Copy next generation into current generation
        for row in range(self.rows):
            for column in range(self.columns):
                self.grid.cells[row][column] = self.temp_grid.cells[row][column]

    def randomize(self):
        self.grid.randomize()
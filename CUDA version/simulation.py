from numba import cuda
import numpy as np
from grid import Grid

@cuda.jit
def update_grid_kernel(current_grid, next_grid, rows, columns):
    # Get 2D thread indices
    col, row = cuda.grid(2)
    
    if row < rows and col < columns:
        live_neighbors = 0
        
        # Count live neighbors in 3x3 window
        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):
                if row_offset == 0 and col_offset == 0:
                    continue
                
                nbr_row = row + row_offset
                nbr_col = col + col_offset
                
                if 0 <= nbr_row < rows and 0 <= nbr_col < columns:
                    if current_grid[nbr_row, nbr_col] == 1:
                        live_neighbors += 1
                        
        # Apply Game of Life rules
        current_cell = current_grid[row, col]
        if current_cell == 1:
            if live_neighbors == 2 or live_neighbors == 3:
                next_grid[row, col] = 1
            else:
                next_grid[row, col] = 0
        else:
            if live_neighbors == 3:
                next_grid[row, col] = 1
            else:
                next_grid[row, col] = 0

class Simulation:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.grid = Grid(rows, columns)
        self.temp_grid = Grid(rows, columns)

    def randomize(self):
        self.grid.randomize()

    def update(self):
        # Move host (CPU) data to device (GPU) memory
        d_current = cuda.to_device(self.grid.cells)
        d_next = cuda.to_device(self.temp_grid.cells)

        # Set block and grid dimensions
        threadsperblock = (16, 16)
        blockspergrid_x = (self.columns + threadsperblock[0] - 1) // threadsperblock[0]
        blockspergrid_y = (self.rows + threadsperblock[1] - 1) // threadsperblock[1]
        blockspergrid = (blockspergrid_x, blockspergrid_y)

        # Run CUDA kernel on GPU
        update_grid_kernel[blockspergrid, threadsperblock](d_current, d_next, self.rows, self.columns)

        # Copy updated results back from GPU to CPU
        self.grid.cells = d_next.copy_to_host()
import time
from numba import cuda
import numpy as np

# Experiment parameters
ROWS = 500
COLUMNS = 500
ITERATIONS = 100

# CUDA Kernel for updating grid
@cuda.jit
def update_grid_kernel(current_grid, next_grid, rows, columns):
    col, row = cuda.grid(2)
    
    if row < rows and col < columns:
        live_neighbors = 0
        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):
                if row_offset == 0 and col_offset == 0:
                    continue
                
                nbr_row = row + row_offset
                nbr_col = col + col_offset
                
                if 0 <= nbr_row < rows and 0 <= nbr_col < columns:
                    if current_grid[nbr_row, nbr_col] == 1:
                        live_neighbors += 1
                        
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

# Create initial random state using NumPy
grid_cells = np.random.choice([0, 0, 0, 1], size=(ROWS, COLUMNS)).astype(np.int32)
temp_cells = np.zeros((ROWS, COLUMNS), dtype=np.int32)

# Move data to GPU device memory
d_current = cuda.to_device(grid_cells)
d_next = cuda.to_device(temp_cells)

# Define thread blocks and grid dimensions
threadsperblock = (16, 16)
blockspergrid_x = (COLUMNS + threadsperblock[0] - 1) // threadsperblock[0]
blockspergrid_y = (ROWS + threadsperblock[1] - 1) // threadsperblock[1]
blockspergrid = (blockspergrid_x, blockspergrid_y)

# Start timer
start_time = time.perf_counter()

# Run 100 iterations on GPU
for _ in range(ITERATIONS):
    update_grid_kernel[blockspergrid, threadsperblock](d_current, d_next, ROWS, COLUMNS)
    # Swap pointers
    d_current, d_next = d_next, d_current

# Ensure GPU execution is finished
cuda.synchronize()

# Stop timer
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

print("--------------------------------")
print("Conway's Game of Life - CUDA GPU Benchmark")
print("--------------------------------")
print(f"Grid size    : {ROWS} x {COLUMNS}")
print(f"Iterations   : {ITERATIONS}")
print(f"Execution time: {execution_time:.6f} seconds")
print("--------------------------------")
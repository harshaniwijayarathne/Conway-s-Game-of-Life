import time
from simulation import Simulation


# Experiment parameters
ROWS = 500
COLUMNS = 500
ITERATIONS = 100


# Create simulation
simulation = Simulation(ROWS, COLUMNS)

# Create initial random state
simulation.randomize()


# Start timer
start_time = time.perf_counter()


# Run 100 generations
for _ in range(ITERATIONS):
    simulation.update()


# Stop timer
end_time = time.perf_counter()


# Calculate execution time
execution_time = end_time - start_time


print("--------------------------------")
print("Conway's Game of Life - CPU")
print("--------------------------------")
print(f"Grid size    : {ROWS} x {COLUMNS}")
print(f"Iterations   : {ITERATIONS}")
print(f"Execution time: {execution_time:.6f} seconds")
print("--------------------------------")
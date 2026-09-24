import pygame
import sys
from simulation import Simulation

# Initialize Pygame
pygame.init()

# Display settings
GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 10
FPS = 30

# Calculate number of cells
ROWS = WINDOW_HEIGHT // CELL_SIZE
COLUMNS = WINDOW_WIDTH // CELL_SIZE

# Create Pygame window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life - CUDA GPU Accelerated")

# Create clock
clock = pygame.time.Clock()

# Create simulation
simulation = Simulation(ROWS, COLUMNS)
simulation.randomize()

# Run iterations
for iteration in range(100):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update simulation using GPU CUDA kernel
    simulation.update()

    # Clear window and draw cells
    window.fill(GREY)

    for row in range(ROWS):
        for column in range(COLUMNS):
            color = (0, 255, 0) if simulation.grid.cells[row][column] == 1 else (55, 55, 55)
            pygame.draw.rect(
                window,
                color,
                (
                    column * CELL_SIZE,
                    row * CELL_SIZE,
                    CELL_SIZE - 1,
                    CELL_SIZE - 1
                )
            )

    pygame.display.update()
    print(f"CUDA Iteration: {iteration + 1}/100")
    clock.tick(FPS)

pygame.quit()
sys.exit()
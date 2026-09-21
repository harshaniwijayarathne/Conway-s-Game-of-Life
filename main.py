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
window = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT)
)

pygame.display.set_caption("Conway's Game of Life")

# Create clock
clock = pygame.time.Clock()

# Create simulation
simulation = Simulation(ROWS, COLUMNS)

# Create random initial state
simulation.randomize()

# Run exactly 100 iterations
for iteration in range(100):

    # Check for window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update simulation
    simulation.update()

    # Clear the window
    window.fill(GREY)

    # Draw the grid
    for row in range(ROWS):
        for column in range(COLUMNS):

            if simulation.grid.cells[row][column] == 1:

                # Draw live cell
                pygame.draw.rect(
                    window,
                    (0, 255, 0),
                    (
                        column * CELL_SIZE,
                        row * CELL_SIZE,
                        CELL_SIZE - 1,
                        CELL_SIZE - 1
                    )
                )

            else:

                # Draw dead cell
                pygame.draw.rect(
                    window,
                    (55, 55, 55),
                    (
                        column * CELL_SIZE,
                        row * CELL_SIZE,
                        CELL_SIZE - 1,
                        CELL_SIZE - 1
                    )
                )

    # Update display
    pygame.display.update()

    # Show iteration number
    print(f"Iteration: {iteration + 1}/100")

    # Control simulation speed
    clock.tick(FPS)

# Close Pygame after 100 iterations
pygame.quit()
sys.exit()
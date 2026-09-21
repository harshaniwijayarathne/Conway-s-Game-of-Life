import pygame
import sys
from simulation import Simulation


pygame.init()

GREY = (29, 29, 29)

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750

CELL_SIZE = 25
FPS = 12

ROWS = WINDOW_HEIGHT // CELL_SIZE
COLUMNS = WINDOW_WIDTH // CELL_SIZE

window = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT)
)

pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

# Create simulation
simulation = Simulation(ROWS, COLUMNS)

# Create random initial state
simulation.randomize()


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update simulation
    simulation.update()

    # Draw grid
    window.fill(GREY)

    for row in range(ROWS):
        for column in range(COLUMNS):

            if simulation.grid.cells[row][column] == 1:

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

    pygame.display.update()

    clock.tick(FPS)
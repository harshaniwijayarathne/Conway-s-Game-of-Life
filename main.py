import pygame, sys
from simulation import Simulation

pygame.init()

GREY = (29,29,29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 25
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life") 

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
simulation.grid.cells[3][4] = 1
simulation.grid.cells[3][5] = 1
simulation.grid.cells[4][4] = 1
simulation.grid.cells[2][5] = 1
print(simulation.count_live_neighbours(simulation.grid, 3, 4))

#simulation loop
while True:

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updating State

    # 3. Drawing
    window.fill(GREY)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
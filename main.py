#TODO: 
# Add Legend for controls
# Check out other pygame features i can add

import pygame as pg
import sys
from grid import Grid
from simulation import Simulation

pg.init()

#screen resolution
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

CELL_SIZE = 12
FPS = 12

#colours
GREY = (29,29,29)
WHITE = (255,255,255)
BLACK = (0,0,0)

#create window
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pg.display.set_caption("Game Of Life")

#create GUI
font = pg.font.Font(None,24)
controls = [
    "CONTROLS:",
    "MOUSE CLICK - Add Cell",
    "SPACEBAR - (Un)Pause",
    "UP - Speed UP",
    "DOWN - Slow DOWN",
    "R - randomize",
    "C - clear"
]
legend_surfaces = [font.render(line,True,WHITE) for line in controls]

clock = pg.time.Clock()
simulation = Simulation(WINDOW_WIDTH,WINDOW_HEIGHT,CELL_SIZE)


#Simulation Loop
while True:

    #Event Handling
    for event in pg.event.get():
        #quit game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()

            row = pos[1] // CELL_SIZE
            col = pos[0] // CELL_SIZE
            simulation.toggle_cell(row,col)



        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                simulation.toggle_sim()
                if simulation.is_running():
                    pg.display.set_caption("Simulation Running")
                else:
                    pg.display.set_caption("Simulation Paused")
            elif event.key == pg.K_UP:
                FPS += 2
                pg.display.set_caption("Speeding Up")

            elif event.key == pg.K_DOWN:
                pg.display.set_caption("Slowing Down")
                if FPS > 5:
                    FPS -= 2
            elif event.key == pg.K_r:
                simulation.create_random_state()
                pg.display.set_caption("Random State Created")

            elif event.key == pg.K_c:
                simulation.clear()
                pg.display.set_caption("Clearing Grid")


                


    #Update Grid State
    simulation.update()



    #Draw Grid
    window.fill(GREY)
    simulation.draw(window)

    # Draw the legend
    x, y = 10, 10  # Top-left corner position
    for surface in legend_surfaces:
        window.blit(surface, (x, y))
        y += surface.get_height() + 5  # Add spacing between line

    pg.display.update()
    clock.tick(FPS)
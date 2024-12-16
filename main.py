import pygame as pg
from tile import Tile

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
reset_button_font = pg.font.Font("font_fredoka_one.ttf", 32)

def is_inside_button(mouse: tuple[int, int], coords: tuple[int, int], dimensions: tuple[int, int]):
    return coords[0] < mouse[0] < coords[0] + dimensions[0] and coords[1] < mouse[1] < coords[1] + dimensions[1]
    

bg = (225, 231, 239)
blank_tile = (211, 211, 211)
blank_tile_hover = (170, 200, 200)
painted_tile = (44, 44, 44)
painted_tile_hover = (55, 55, 90)

pos_x_grid = 200
pos_y_grid = 200

painted_matrix = [[False for _ in range(15)] for _ in range(9)]

dimensions_reset_button = (150, 100)
coords_reset_button = (1032, 50)
dimensions_set_button = (150, 100)
coords_set_button = (1032, 200)


########################################################
######################    MAIN    ######################
########################################################


while True:

    mouse = pg.mouse.get_pos()
    screen.fill(bg)

    pos_x_grid = 200
    pos_y_grid = 200


    if is_inside_button(mouse, coords_reset_button, dimensions_reset_button):
        pg.draw.rect(screen, (227, 150, 43), (coords_reset_button, dimensions_reset_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_reset_button, dimensions_reset_button), width=3)
    else:
        pg.draw.rect(screen, (201, 134, 34), (coords_reset_button, dimensions_reset_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_reset_button, dimensions_reset_button), width=3)


    screen.blit(reset_button_font.render("RESET", True, (13, 13, 13)), (1052, 70))    


    if is_inside_button(mouse, coords_set_button, dimensions_set_button):
        pg.draw.rect(screen, (227, 150, 43), (coords_set_button, dimensions_set_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_set_button, dimensions_set_button), width=3)
    else:
        pg.draw.rect(screen, (201, 134, 34), (coords_set_button, dimensions_set_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_set_button, dimensions_set_button), width=3)

    screen.blit(reset_button_font.render("SET", True, (13, 13, 13)), (1052, 220))

    
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit() 
        if ev.type == pg.MOUSEBUTTONDOWN:

            x_click, y_click = pg.mouse.get_pos()
            i = (y_click - 200) // 52
            j = (x_click - 200) // 52

            if -1 < i < 9 and 0 <= j < 15: 
                painted_matrix[i][j] = not painted_matrix[i][j]
            
            if is_inside_button((x_click, y_click), coords_reset_button, dimensions_reset_button):
                painted_matrix = [[False for _ in range(15)] for _ in range(9)]


            if is_inside_button((x_click, y_click), coords_set_button, dimensions_set_button):
                painted_matrix = [[True for _ in range(15)] for _ in range(9)]

    pg.draw.rect(screen, (5, 5, 5), ((pos_x_grid - 2, pos_y_grid - 2), (52 * 15 + 2, 52 * 9 + 2))) # black rectangle behind the grid, to look like the separator lines

    for i in range(9):
        for j in range(15):
            if painted_matrix[i][j]:
                if is_inside_button(mouse, (pos_x_grid + 52 * j, pos_y_grid), (50, 50)):
                    pg.draw.rect(screen, painted_tile_hover, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))
                else:
                    pg.draw.rect(screen, painted_tile, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))

            else:
                if is_inside_button(mouse, (pos_x_grid + 52 * j, pos_y_grid), (50, 50)):
                    pg.draw.rect(screen, blank_tile_hover, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))
                else:
                    pg.draw.rect(screen, blank_tile, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))
        pos_y_grid += 52

    pg.display.flip()
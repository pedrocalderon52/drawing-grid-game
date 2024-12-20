import pygame as pg
from tile import Tile

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
reset_button_font = pg.font.Font("fonts/font_fredoka_one.ttf", 32)
running = True

def is_inside_button(mouse: tuple[int, int], coords: tuple[int, int], dimensions: tuple[int, int]):
    return coords[0] < mouse[0] < coords[0] + dimensions[0] and coords[1] < mouse[1] < coords[1] + dimensions[1]

def is_inside_circle(mouse: tuple, center_coords: tuple, center_radius: float):
    return (((mouse[0] - center_coords[0]) ** 2 + (mouse[1] - center_coords[1]) ** 2) ** 0.5) <= center_radius
    

black = (44, 44, 44)
red = (156, 62, 78)
green = (80, 161, 76)
blue = (53, 124, 148)

black_hover = (66, 65, 65)
red_hover = (125, 50, 63)
green_hover = (87, 186, 82)
blue_hover = (41, 98, 117)


colors = [black, red, green, blue]
hover_colors = [black_hover, red_hover, green_hover, blue_hover]

bg = (225, 231, 239)
blank_tile = (211, 211, 211)
blank_tile_hover = (170, 200, 200)
painted_tile_color = black
hover_painted_tile_color = (55, 55, 90)

pos_x_grid = 200
pos_y_grid = 200

painted_matrix = [[Tile(painted_tile_color, hover_painted_tile_color, painted = False) for _ in range(15)] for _ in range(9)]

dimensions_reset_button = (150, 100)
coords_reset_button = (1032, 50)
dimensions_set_button = (150, 100)
coords_set_button = (1032, 200)
coords_center_colors_button = (200, 100)
radius_circle_button = 25


########################################################
######################    MAIN    ######################
########################################################


while running:

    mouse = pg.mouse.get_pos()
    screen.fill(bg)

    pos_x_grid = 200
    pos_y_grid = 200

    selected_color_index = colors.index(painted_tile_color)

    # printing the reset button

    if is_inside_button(mouse, coords_reset_button, dimensions_reset_button):
        pg.draw.rect(screen, (227, 150, 43), (coords_reset_button, dimensions_reset_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_reset_button, dimensions_reset_button), width=3)
    else:
        pg.draw.rect(screen, (201, 134, 34), (coords_reset_button, dimensions_reset_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_reset_button, dimensions_reset_button), width=3)


    screen.blit(reset_button_font.render("RESET", True, (13, 13, 13)), (1052, 70))    

    # printing the set button

    if is_inside_button(mouse, coords_set_button, dimensions_set_button):
        pg.draw.rect(screen, (227, 150, 43), (coords_set_button, dimensions_set_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_set_button, dimensions_set_button), width=3)
    else:
        pg.draw.rect(screen, (201, 134, 34), (coords_set_button, dimensions_set_button))
        pg.draw.rect(screen, (13, 6, 0), (coords_set_button, dimensions_set_button), width=3)

    screen.blit(reset_button_font.render("SET", True, (13, 13, 13)), (1052, 220))

    # printing the color buttons

    pg.draw.circle(screen, (4, 4, 4), (coords_center_colors_button[0] + selected_color_index * 100, coords_center_colors_button[1]), radius_circle_button + 5, width=3)
    for i in range(4):
        if is_inside_circle(mouse, (coords_center_colors_button[0] + i * 100, coords_center_colors_button[1]), radius_circle_button):
            pg.draw.circle(screen, colors[i], (coords_center_colors_button[0] + i * 100, coords_center_colors_button[1]), radius_circle_button)
            pg.draw.circle(screen, (130, 130, 130), (coords_center_colors_button[0] + i * 100, coords_center_colors_button[1]), radius_circle_button + 5, width=3)
        else:
            pg.draw.circle(screen, hover_colors[i], (coords_center_colors_button[0] + i * 100, coords_center_colors_button[1]), radius_circle_button)
            
    
    for ev in pg.event.get():
        if ev.type == pg.QUIT: # quit
            running = False
        if ev.type == pg.MOUSEBUTTONDOWN: # click

            x_click, y_click = pg.mouse.get_pos() # get click info
            i = (y_click - 200) // 52
            j = (x_click - 200) // 52

            if -1 < i < 9 and 0 <= j < 15: # if click is inside a tile
                painted_matrix[i][j].change_tile(colors[selected_color_index], hover_colors[selected_color_index]) 
            
            if is_inside_button((x_click, y_click), coords_reset_button, dimensions_reset_button): # if click is inside reset button
                painted_matrix = [[Tile(painted_tile_color, hover_painted_tile_color, painted = False) for _ in range(15)] for _ in range(9)]


            if is_inside_button((x_click, y_click), coords_set_button, dimensions_set_button): # if click is inside set button
                painted_matrix = [[Tile(painted_tile_color, hover_painted_tile_color, painted = True) for _ in range(15)] for _ in range(9)]

            for i in range(4): # if click is inside one of the color buttons
                if is_inside_circle((x_click, y_click), (coords_center_colors_button[0] + 100 * i, coords_center_colors_button[1]), radius_circle_button):
                    painted_tile_color = colors[i]
                    hover_painted_tile_color = hover_colors[i]
                    

    pg.draw.rect(screen, (5, 5, 5), ((pos_x_grid - 2, pos_y_grid - 2), (52 * 15 + 2, 52 * 9 + 2))) # black rectangle behind the grid, to look like the separator lines

    for i in range(9): # going through the matrix, to print it
        for j in range(15):
            if painted_matrix[i][j].painted:
                if is_inside_button(mouse, (pos_x_grid + 52 * j, pos_y_grid), (50, 50)): # w/ hover
                    pg.draw.rect(screen, painted_matrix[i][j].hover_color, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))
                else:
                    pg.draw.rect(screen, painted_matrix[i][j].color, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))

            else:
                if is_inside_button(mouse, (pos_x_grid + 52 * j, pos_y_grid), (50, 50)): # w/ hover
                    pg.draw.rect(screen, blank_tile_hover, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))
                else:
                    pg.draw.rect(screen, blank_tile, ((pos_x_grid + j * 52, pos_y_grid), (50, 50)))
        pos_y_grid += 52

    pg.display.flip()
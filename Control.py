import pygame
import pygame.locals
from dcc_graphics import proto_graphics

if __name__ == "__main__":
    game_over=False
    pg=proto_graphics()
    pg.load_background("img/map/[FE8] Indoor Tutorial.png",20,25)
    while not game_over:
        pg.draw()
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                game_over = True
            elif event.type == pygame.locals.KEYDOWN:
                pressed_key = event.key

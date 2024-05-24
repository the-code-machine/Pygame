import pygame
pygame.init()
white =(255,255,255)
black = (0,0,0)
red=(255,0,0)
## Making Window for game
gd =pygame.display.set_mode((700,500))
game_over =True
while game_over:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=False


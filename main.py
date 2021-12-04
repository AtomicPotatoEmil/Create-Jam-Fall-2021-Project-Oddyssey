import pygame
import game_screen

pygame.init()

screen = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("An Oddyssey")

clock = pygame.time.Clock()

screens = [game_screen.Screen(screen)]

playing = True

while playing:

    
    dt = clock.tick() / 1000

    screens[0].run()
    if screens[0].level_quit:
        playing = False

    pygame.display.update()

pygame.quit()


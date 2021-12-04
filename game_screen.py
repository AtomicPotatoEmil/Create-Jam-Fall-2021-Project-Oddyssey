import pygame

class Screen:

    def __init__(self, screen):
        self.screen = screen
        self.level_quit = False
        self.overworld_surface = pygame.Surface((1920, 540))
        self.underworld_surface = pygame.Surface((1920, 540))
    

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.level_quit = True
            
            self.screen.fill((255, 255, 255))
        
        self.overworld_surface.fill((0, 0, 200))
        self.underworld_surface.fill((200, 0, 0))
        self.screen.blit(self.overworld_surface, (0, 0))
        self.screen.blit(self.underworld_surface, (0, 540))
        pass

    def overworld(self):
        pass

    def underworld(self):
        pass
    
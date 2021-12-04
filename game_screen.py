import pygame
from Map import Map

class Screen:

    def __init__(self, screen):
        self.screen = screen
        self.level_quit = False

        self.is_overworld = True

        # OVERWORLD
        self.overworld_surface = pygame.Surface((1920, 540))

        self.overworld_bg = pygame.image.load("data/sprites/map/OverworldBackground.png")
        self.overworld_back_wave = pygame.image.load("data/sprites/map/OverworldSeaBack.png")
        self.overworld_front_wave = pygame.image.load("data/sprites/map/OverworldSeaFront.png")
        self.overworld_bg_parallax = Map(self.overworld_surface, self.overworld_bg, 0, 1, 0, 0)
        self.overworld_back_wave_parallax = Map(self.overworld_surface, self.overworld_back_wave, 450, 1, 0.5, 20)
        self.overworld_front_wave_parallax = Map(self.overworld_surface, self.overworld_front_wave, 500, 2, 0.5, 20)
        self.ship_layer_imgs = [
            pygame.transform.scale(pygame.image.load("data/sprites/ship/ShipBack.png"), (600, 400)),
            pygame.transform.scale(pygame.image.load("data/sprites/ship/ShipFront.png"), (600, 400)) 
            ]
        
        self.overworld_ship_hitboxes = [
            pygame.Rect(510, 445, 550, 10), pygame.Rect(630, 515, 370, 10), pygame.Rect(505, 375, 580, 10),
            pygame.Rect(505, 375, 35, 90), pygame.Rect(1025, 375, 35, 90), pygame.Rect(1060, 357, 10, 90),
            pygame.Rect(600, 445, 35, 70), pygame.Rect(1000, 445, 35, 70), pygame.Rect(505, 355, 35, 20)]
        
        # UNDERWORLD
        self.underworld_surface = pygame.Surface((1920, 540))

        self.flipped_ship_layer_imgs = [
            pygame.transform.flip(self.ship_layer_imgs[0], False, True),
            pygame.transform.flip(self.ship_layer_imgs[1], False, True)
        ]
    

    def run(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.level_quit = True
            
            #DEBUG
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.is_overworld = False
                if event.key == pygame.K_x:
                    self.is_overworld = True
            
        self.screen.fill((255, 255, 255))
        
        # OVERWORLD
        self.overworld_surface.fill((0, 0, 200))
        self.overworld_bg_parallax.Map_mover()
        self.overworld_back_wave_parallax.Map_mover()
        if self.is_overworld:
            self.overworld()
        self.overworld_front_wave_parallax.Map_mover()
        

        # UNDERWORLD
        self.underworld_surface.fill((200, 0, 0))
        if not self.is_overworld:
            self.underworld()

        # Main Screen
        self.screen.blit(self.overworld_surface, (0, 0))
        self.screen.blit(self.underworld_surface, (0, 540))


    def overworld(self):
        self.overworld_surface.blit(self.ship_layer_imgs[0], (500, 140)),
        self.overworld_surface.blit(self.ship_layer_imgs[1], (500, 140))
        for rect in self.overworld_ship_hitboxes:
            pygame.draw.rect(self.overworld_surface, (255, 0, 0), rect, 2)
        

    def underworld(self):
        self.underworld_surface.blit(self.flipped_ship_layer_imgs[0], (500, 0)),
        self.underworld_surface.blit(self.flipped_ship_layer_imgs[1], (500, 0))
        pass
    
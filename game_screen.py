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
        self.ship_ladder = pygame.transform.scale(pygame.image.load("data/sprites/ship/Ladder.png"), (60, 100))
        
        self.overworld_ship_hitboxes = [
            pygame.Rect(510, 445, 550, 10), pygame.Rect(630, 515, 370, 10), pygame.Rect(505, 375, 580, 10),
            pygame.Rect(505, 375, 35, 90), pygame.Rect(1025, 375, 35, 90), pygame.Rect(1060, 357, 10, 90),
            pygame.Rect(600, 445, 35, 70), pygame.Rect(1000, 445, 35, 70), pygame.Rect(505, 355, 35, 20)]
        
        self.top_to_bottom_overworld = pygame.Rect(900, 300, 50, 50)
        self.middle_to_top_overworld = pygame.Rect(900, 390, 50, 50)
        self.middle_to_buttom_overworld = pygame.Rect(680, 390, 50, 50)
        self.buttom_to_middle_overworld = pygame.Rect(680, 470, 50, 50)
        
        
        # UNDERWORLD
        self.underworld_surface = pygame.Surface((1920, 540))

        self.underworld_bg = pygame.image.load("data/sprites/map/UnderworldBackground.png")
        self.underworld_back_wave = pygame.image.load("data/sprites/map/UnderworldWaterBack.png")
        self.underworld_front_wave = pygame.image.load("data/sprites/map/UnderworldWaterFront.png")
        self.underworld_bg_parallax = Map(self.underworld_surface, self.underworld_bg, 0, 1, 0, 0)
        self.underworld_back_wave_parallax = Map(self.underworld_surface, self.underworld_back_wave, 0, 1, 0.5, 20)
        self.underworld_front_wave_parallax = Map(self.underworld_surface, self.underworld_front_wave, -25, 2, 0.5, 20)
        self.flipped_ship_layer_imgs = [
            pygame.transform.flip(self.ship_layer_imgs[0], False, True),
            pygame.transform.flip(self.ship_layer_imgs[1], False, True)
        ]

        self.flipped_ladder = pygame.transform.flip(self.ship_ladder, False, True)

        self.underworld_ship_hitboxes = [
            pygame.Rect(510, 85, 550, 10), pygame.Rect(630, 15, 370, 10), pygame.Rect(505, 155, 580, 10),
            pygame.Rect(505, 75, 35, 90), pygame.Rect(1025, 75, 35, 90), pygame.Rect(1060, 94, 10, 90),
            pygame.Rect(600, 25, 35, 70), pygame.Rect(1000, 25, 35, 70), pygame.Rect(505, 165, 35, 20)
        ]

        self.top_to_bottom_underworld = pygame.Rect(900, 170, 50, 50)
        self.middle_to_top_underworld = pygame.Rect(900, 100, 50, 50)
        self.middle_to_buttom_underworld = pygame.Rect(680, 100, 50, 50)
        self.buttom_to_middle_underworld = pygame.Rect(680, 20, 50, 50)

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
        pygame.draw.rect(self.overworld_surface, (0, 255, 0), self.top_to_bottom_overworld, 2)
        pygame.draw.rect(self.overworld_surface, (0, 255, 0), self.middle_to_top_overworld, 2)
        pygame.draw.rect(self.overworld_surface, (0, 255, 0), self.middle_to_buttom_overworld, 2)
        pygame.draw.rect(self.overworld_surface, (0, 255, 0), self.buttom_to_middle_overworld, 2)
        self.overworld_front_wave_parallax.Map_mover()
        

        # UNDERWORLD
        self.underworld_surface.fill((200, 0, 0))
        self.underworld_bg_parallax.Map_mover()
        self.underworld_back_wave_parallax.Map_mover()
        if not self.is_overworld:
            self.underworld()
        pygame.draw.rect(self.underworld_surface, (0, 255, 0), self.top_to_bottom_underworld, 2)
        pygame.draw.rect(self.underworld_surface, (0, 255, 0), self.middle_to_top_underworld, 2)
        pygame.draw.rect(self.underworld_surface, (0, 255, 0), self.middle_to_buttom_underworld, 2)
        pygame.draw.rect(self.underworld_surface, (0, 255, 0), self.buttom_to_middle_underworld, 2)
        self.underworld_front_wave_parallax.Map_mover()

        # Main Screen
        self.screen.blit(self.overworld_surface, (0, 0))
        self.screen.blit(self.underworld_surface, (0, 540))


    def overworld(self):
        self.overworld_surface.blit(self.ship_layer_imgs[0], (500, 140))
        self.overworld_surface.blit(self.ship_ladder, (900, 350))
        self.overworld_surface.blit(self.ship_ladder, (680, 420))
        self.overworld_surface.blit(self.ship_layer_imgs[1], (500, 140))
        for rect in self.overworld_ship_hitboxes:
            pygame.draw.rect(self.overworld_surface, (255, 0, 0), rect, 2)
        

    def underworld(self):
        self.underworld_surface.blit(self.flipped_ship_layer_imgs[0], (500, 0)),
        self.underworld_surface.blit(self.flipped_ladder, (900, 90))
        self.underworld_surface.blit(self.flipped_ladder, (680, 20))
        self.underworld_surface.blit(self.flipped_ship_layer_imgs[1], (500, 0))
        for rect in self.underworld_ship_hitboxes:
            pygame.draw.rect(self.underworld_surface, (255, 0, 0), rect, 2)
    
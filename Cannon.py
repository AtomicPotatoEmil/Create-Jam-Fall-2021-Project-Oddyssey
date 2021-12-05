import pygame

class Cannon:

    def __init__(self, screen, x, y, width, height, facing_left, flipped):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing_left = facing_left
        self.flipped = flipped
        self.img = pygame.transform.scale(pygame.image.load("data/sprites/ship/SideCannonUnselected.png"), (self.width, self.height))
        self.img_selected = pygame.transform.scale(pygame.image.load("data/sprites/ship/SideCannonSelected.png"), (self.width, self.height))
        if self.facing_left:
            self.img = pygame.transform.flip(self.img, True, False)
            self.img_selected =pygame.transform.flip(self.img_selected, True, False)
        if self.flipped:
            self.img = pygame.transform.flip(self.img, False, True)
            self.img_selected = pygame.transform.flip(self.img_selected, False, True)
        
        self.rect = self.img.get_rect(x = self.x, y = self.y)
        self.selected = False
    
    def draw(self):
        if self.selected:
            self.screen.blit(self.img_selected, (self.x, self.y))
        else:
            self.screen.blit(self.img, (self.x, self.y))
        

        

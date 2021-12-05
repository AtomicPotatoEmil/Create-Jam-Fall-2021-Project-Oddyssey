import pygame

class Player:

    def __init__(self, screen, x, y, width, height, speed, flipped, collision_tolerance, animation_speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.flipped = flipped
        self.collision_tolerance = collision_tolerance
        self.animation_speed = animation_speed
        self.going_right = False
        self.going_left = False
        self.has_cannon_ball = True
        if self.flipped:
            self.animation = {
               "RIGHT": (
                   pygame.transform.flip(pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyLeft1.png"), (width, height)), False, True),
                   pygame.transform.flip(pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyLeft2.png"), (width, height)), False, True)
                   ),
                "LEFT": (
                   pygame.transform.flip(pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyRight1.png"), (width, height)), False, True),
                   pygame.transform.flip(pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyRight2.png"), (width, height)), False, True)
                   )
            }
        else:
            self.animation = {
                "RIGHT": (
                    pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyLeft1.png"), (width, height)),
                    pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyLeft2.png"), (width, height)),
                ),
                "LEFT": (
                    pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyRight1.png"), (width, height)),
                    pygame.transform.scale(pygame.image.load("data/sprites/characters/player1/OddyRight2.png"), (width, height)),
                )
            }

        self.animation_index = 0
        self.current_animation = "LEFT"
        self.rect = self.animation["LEFT"][self.animation_index].get_rect(x = self.x, y = self.y)
    
    def update(self, dt):
        if self.going_right:
            self.x += self.speed * dt
        elif self.going_left:
            self.x -= self.speed * dt
            
        self.rect = self.animation[self.current_animation][int(self.animation_index)].get_rect(x = self.x, y = self.y)

    def draw(self, dt):
        if self.going_right:
            self.current_animation = "RIGHT"
            self.animation_index += self.animation_speed * dt
        if self.going_left:
            self.current_animation = "LEFT"
            self.animation_index += self.animation_speed * dt
        if self.animation_index >= len(self.animation[self.current_animation]):
                self.animation_index = 0
        self.screen.blit(self.animation[self.current_animation][int(self.animation_index)], (self.x, self.y))
        pass

    def check_collision(self, other_rect):
        if self.rect.colliderect(other_rect):
            if abs(other_rect.left - self.rect.right) < self.collision_tolerance:
                self.going_right = False
                print(self.can_go_right)
            if abs(other_rect.right - self.rect.left) < self.collision_tolerance:
                self.going_left = False
                
        else:
            self.can_go_right = True
            self.can_go_left = True
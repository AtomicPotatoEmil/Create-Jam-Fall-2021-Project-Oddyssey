import pygame

class Map:
    def __init__(self, Surface, image_path, y, x_vel, y_vel, move_max):
        self.surface = Surface
        self.image_path = image_path
        self.image1 = self.image_path
        self.image2 = self.image_path

        self.x1 = 0
        self.x2 = 1920
        self.start_y = y
        self.y = y

        self.x_vel = x_vel
        self.y_vel = y_vel
        self.move_max = move_max

    def Map_mover(self):
        self.surface.blit(self.image1, (self.x1, self.y))
        self.surface.blit(self.image2, (self.x2, self.y))

        if self.x1 > 0 or self.x2 > 0:
            self.x1 -= self.x_vel
            self.x2 -= self.x_vel
            self.y -= self.y_vel

        if self.x1 <= -1920:
            self.x1 = 1920
        if self.x2 <= -1920:
            self.x2 = 1920

        if self.y < self.start_y - self.move_max:
            self.y_vel *= -1
        if self.y > self.start_y:
            self.y_vel *= -1
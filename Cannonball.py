
class Cannonball:
    def __init__(self, surface, image_path, vel, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.vel = vel
        self.image = image_path
        self.rect = (self.x, self.y, 28, 28)

    def shoot(self, DT):
        self.rect = (self.x, self.y, 28, 28)
        self.surface.blit(self.image, (self.x, self.y))
        self.x += self.vel * DT
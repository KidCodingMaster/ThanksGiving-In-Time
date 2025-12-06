import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        
        self.image = pygame.Surface((25, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_frect(center=(x, y))
        
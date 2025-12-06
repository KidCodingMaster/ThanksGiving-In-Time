import pygame
import json

def read_json():
    with open('./settings.json', 'r') as f:
        return json.load(f)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        
        self.settings = read_json()
        
        self.pos = pygame.Vector2(x, y)
        
        self.image = pygame.Surface((25, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_frect(center=self.pos)
        
        self.speed = 1.8
        
    def clamp(self, num, _max, _min):
        if num > _max:
            return _max
        if num < _min:
            return _min
        
        return num
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speed
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speed
        if keys[pygame.K_UP]:
            self.pos.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos.y += self.speed
            
        self.pos.x = self.clamp(
            self.pos.x,
            self.settings['center_x'] + 348,
            self.settings['center_x'] - self.settings['center_y'] + 12
        )
        self.pos.y = self.clamp(self.pos.y, self.settings['screen_height'] - 25, 25)
            
        self.rect = self.image.get_frect(center=self.pos)
        
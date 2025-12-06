import pygame
import json

def read_json():
    with open('./settings.json', 'r') as f:
        return json.load(f)

class Game:
    def __init__(self):
        self.settings = read_json()
        
        self.screen = pygame.display.set_mode((self.settings['screen_width'], self.settings['screen_height']))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
            pygame.display.update()
            
if __name__ == '__main__':
    game = Game()
    game.run()
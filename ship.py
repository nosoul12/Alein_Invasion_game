import pygame

class Ship:
 def __init__(self, ai):
    self.screen = ai.screen
    self.screen_rect = ai.screen.get_rect()
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.rect.midbottom = self.screen_rect.midbottom

def blitme(self):
    self.screen.blit(self.image, self.rect)
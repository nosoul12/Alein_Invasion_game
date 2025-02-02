import sys
import pygame
from setting import Setting
from ship import Ship

class AlienInvasion:

	def __init__(self):
		pygame.init()
		self.settings = Setting()
		self.ship = Ship(self)
		self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
	

	def run_game(self):
		while True:
			# Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()
			# Make the most recently drawn screen visible.
			pygame.display.flip()
if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
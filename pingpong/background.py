import pygame
import pathlib
class Background():
    """A class to represent a background"""

    def __init__(self, screen):
        self.screen = screen

        # Get background rect and set it equal to screen rect
        #background_img_path = str(pathlib.Path('images/background1.png').expanduser().resolve())
        background_img_path = 'C:/Users/husza/VSWorkSpace/.vscode/pingpong/images/background1.png'
        self.image = pygame.image.load(background_img_path)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set rects equal
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the background on the screen"""
        self.screen.blit(self.image, self.rect)
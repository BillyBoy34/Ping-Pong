import pygame

class Player1():
    """Class for the paddles on the sides"""

    def __init__(self, screen, pp_settings):
        """Initializes attributes"""
        self.screen = screen
        self.pp_settings = pp_settings
        self.color = (171, 209, 221)
        self.speed = 0

        # Create paddle and get screen rect
        self.rect = pygame.Rect(0, 0, self.pp_settings.paddle_width, self.pp_settings.paddle_height)
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery

        # Get the exact position of the paddle
        self.y = float(self.rect.centery)

        # Movement flags
        self.move_up = False
        self.move_down = False

    def update(self):
        """Update the position of the paddle."""
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.y -= self.pp_settings.paddle_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.pp_settings.paddle_speed_factor

        # Update the position again
        self.rect.centery = self.y


    def draw_paddles(self):
        """Draw the two paddles on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Player2():
    """Class for the paddles on the sides"""

    def __init__(self, screen, pp_settings):
        """Initializes attributes"""
        self.screen = screen
        self.pp_settings = pp_settings
        self.color = (171, 209, 221)
        self.speed = 0

        # Create paddle and get screen rect
        self.rect = pygame.Rect(0, 0, self.pp_settings.paddle_width, self.pp_settings.paddle_height)
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        # Get the exact position of the paddle
        self.y = float(self.rect.centery)

        # Movement flags
        self.move_up = False
        self.move_down = False

    def update(self):
        """Update the position of the paddle."""
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.y -= self.pp_settings.paddle_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.pp_settings.paddle_speed_factor

        # Update the position again
        self.rect.centery = self.y

    def draw_paddles(self):
        """Draw the two paddles on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)








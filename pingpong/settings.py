import pygame

class Settings():
    """This class holds the settings"""  # --> docstrings

    def __init__(self):
        """Initializing attributes"""

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.win_caption = "Ping Pong"
        self.bg_color = (0, 0, 0)

        # Paddle settings
        self.paddle_width = 30
        self.paddle_height = 150
        self.paddle_color = (255, 255, 255)

        # Paddles speed factor
        self.paddle_speed_factor = 9

        # Ball settings
        self.ball_width = 50
        self.ball_height = 50
        self.ball_color = (255, 0, 0)
        self.ball_speed = [6, 6]

        # Score settings
        self.score_font = pygame.font.SysFont(None, 200)
        self.score_color = (255, 153, 153)






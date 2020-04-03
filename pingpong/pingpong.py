import pygame
from settings import Settings
from game_events import Game_Events
from paddle import Player1, Player2
from background import Background
from ball import Ball
from score import Score1, Score2

class PongPong():
    """Main class of the game"""

    def __init__(self):
        """Initialize attributes of the pongpong game."""
        pygame.init()

        # Settings
        self.pp_settings = Settings()

        # Screen related code
        self.screen = pygame.display.set_mode((self.pp_settings.screen_width, self.pp_settings.screen_height))
        pygame.display.set_caption(self.pp_settings.win_caption)
        # pygame.display.set_icon(pygame.image.load())
        self.bg_color = self.pp_settings.bg_color

        # Paddle instance
        self.player1 = Player1(self.screen, self.pp_settings)
        self.player2 = Player2(self.screen, self.pp_settings)

        # Background instance
        self.background = Background(self.screen)

        # Ball instance
        self.ball = Ball(self.screen, self.pp_settings, self.player1, self.player2)

        # Score instance
        self.score1 = Score1(self.screen, self.ball, self.pp_settings)
        self.score2 = Score2(self.screen, self.ball, self.pp_settings)

        # Game_events instance
        self.ge = Game_Events(self.screen, self.bg_color, self.player1, self.player2,
                              self.background, self.ball, self.score1, self.score2)

        # Runs the game
        self.run_game()

    def run_game(self):
        """Function which runs the game"""
        while True:
            # Looks for mouse and keyboard inputs
            self.ge.event_manager()

            # update the paddles
            self.ge.update_paddles()

            # update the score
            self.ge.update_score()

            # update the ball
            self.ge.update_ball()

            # Update the screen
            self.ge.update_screen()


running_pong = PongPong()







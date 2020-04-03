import pygame
import sys

class Game_Events():
    """Class for checking the game events"""

    def __init__(self, screen, bg_color, player1, player2, background, ball, score1, score2):
        """Initializing game events attributes"""
        self.screen = screen
        self.bg_color = bg_color
        self.player1 = player1
        self.player2 = player2
        self.background = background
        self.ball = ball
        self.score1 = score1
        self.score2 = score2

    def keydown_events(self, event):
        """Looks for all key-press events"""
        if event.key == pygame.K_w:
            self.player1.move_up = True
        elif event.key == pygame.K_s:
            self.player1.move_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_UP:
            self.player2.move_up = True
        elif event.key == pygame.K_DOWN:
            self.player2.move_down = True

    def keyup_events(self, event):
        """Looks for all key releases"""
        if event.key == pygame.K_w:
            self.player1.move_up = False
        elif event.key == pygame.K_s:
            self.player1.move_down = False

        if event.key == pygame.K_UP:
            self.player2.move_up = False
        elif event.key == pygame.K_DOWN:
            self.player2.move_down = False

    def event_manager(self):
        """Look for mouse and keyboard inputs"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)

    def update_ball(self):
        """Update the ball"""
        self.ball.movement_ball()

    def update_paddles(self):
        """Update the paddles"""
        self.player1.update()
        self.player2.update()

    def update_score(self):
        """Updates score"""
        self.score1.update()
        self.score2.update()

    def update_screen(self):
        """Updates objects and states on the screen"""

        # Fill the background
        self.background.blitme()
        self.score1.draw_score()
        self.score2.draw_score()
        self.player1.draw_paddles()
        self.player2.draw_paddles()
        self.ball.particles_ball()
        self.ball.draw_ball()

        pygame.display.flip()
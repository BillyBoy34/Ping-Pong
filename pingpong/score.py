import pygame.ftfont

class Score1():
    """A class for the score of the game"""

    def __init__(self, screen, ball, pp_settings):
        """Initializes score attributes"""
        self.screen = screen
        self.ball = ball
        self.pp_settings = pp_settings
        self.score_count = 0

        self.score_rect = self.render_score().get_rect()
        self.screen_rect = self.screen.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx - 150
        self.score_rect.centery = 100

    def render_score(self):
        self.score_image = self.pp_settings.score_font.render(str(self.score_count), True,
                                                              self.pp_settings.score_color)
        return self.score_image

    def update(self):
        """Makes score go up if ball touches the wall"""
        if self.ball.rect.right > self.screen_rect.right:
            self.score_count += 1

        self.render_score()

    def draw_score(self):
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)


class Score2():
    """A class for the score of the game"""

    def __init__(self, screen, ball, pp_settings):
        """Initializes score attributes"""
        self.screen = screen
        self.ball = ball
        self.pp_settings = pp_settings
        self.score_count = 0

        self.score_rect = self.render_score().get_rect()
        self.screen_rect = self.screen.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx + 150
        self.score_rect.centery = 100

    def render_score(self):
        self.score_image = self.pp_settings.score_font.render(str(self.score_count), True,
                                                              self.pp_settings.score_color)
        return self.score_image

    def update(self):
        """Makes score go up if ball touches the wall"""
        if self.ball.rect.left < 0:
            self.score_count += 1

        self.render_score()

    def draw_score(self):
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
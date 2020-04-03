import pygame
import random


class Ball():
    """A class to represent the ball for the game"""

    def __init__(self, screen, pp_settings, player1, player2):
        """Initializes attributes"""
        self.screen = screen
        self.pp_settings = pp_settings
        self.player1 = player1
        self.player2 = player2
        self.color = self.pp_settings.ball_color
        self.particles = []

        # Create ball
        self.rect = pygame.Rect(0, 0, self.pp_settings.ball_width, self.pp_settings.ball_height)
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center

    def movement_ball(self):
        self.rect = self.rect.move(self.pp_settings.ball_speed)
        if self.rect.left < 0 or self.rect.right > self.screen_rect.right:
            self.pp_settings.ball_speed[0] = -self.pp_settings.ball_speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom:
            self.pp_settings.ball_speed[1] = -self.pp_settings.ball_speed[1]

        if self.rect.colliderect(self.player1.rect):
            self.pp_settings.ball_speed[0] = -self.pp_settings.ball_speed[0]
        if self.rect.colliderect(self.player2.rect):
            self.pp_settings.ball_speed[0] = -self.pp_settings.ball_speed[0]

    def particles_ball(self):
        # pick random color
        colors = [
            (255, 255, 255),
            (255, 0, 0),
            (200, 42, 200),
            (32, 23, 103),
            (45, 230, 0),
            (255,215,0),
            (0,191,255),
            (23, 45, 12),
            (139,0,0),
            (100, 102, 230),
            (120, 150, 200),
            (12, 83, 245),
            (0, 0, 0),
            (30, 40, 50),
            (200, 50, 150)
        ]
        self.color = colors[random.randint(0, len(colors)-1)]


        self.particles.append([[self.rect.centerx, self.rect.centery], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(self.screen, self.color, [int(particle[0][0]), int(particle[0][1])],
                               int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 5)




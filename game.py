import pygame
import os
from mesa import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("freesans", 20)

        self.ruta_cartas = os.path.join(main_dir, "data", "Cards")
        pygame.display.set_caption("Move Cards")

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self)
        self.mesa = Mesa(self)
        self.ganar = Ganar(self, self.mesa)

        self.states = {
            'start': self.start,
            'mesa': self.mesa,
            'ganar': self.ganar
        }

    def run(self):
        while True:
            pygame.display.set_caption(f"{self.clock.get_fps() :.1f}")
            self.states[self.gameStateManager.get_state()].run()


class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state

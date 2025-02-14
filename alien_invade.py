import sys
import pygame


class AlienInvasion:
    """Overall class to manage game asset and behaviour  """

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (200,230
    def run_game(self):
        """Start the main loop for the game """
        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            self.screen.fill(self.bg_color)

            # Make the most recently drawn scren visible
            pygame.display.flip()
            self.clock.tick(60)



if __name__ == "__main__":
    # make a game instance, and run the game 
    ai = AlienInvasion()
    ai.run_game()

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():

    pygame.init()
    Clock = pygame.time.Clock()

    dt = 0

    VERSION = pygame.version.ver

    print(f"Starting Asteroids with pygame verion: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH/ 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        Second = Clock.tick(60)
        dt = Second / 1000


if __name__ == "__main__":
    main()

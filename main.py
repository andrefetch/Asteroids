import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides_with(object):
                    log_event("asteroid_shot")
                    shot.kill()
                    object.kill()

        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        Second = Clock.tick(60)
        dt = Second / 1000


if __name__ == "__main__":
    main()

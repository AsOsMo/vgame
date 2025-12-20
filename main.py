import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    dt = 0
    p_thing = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a_thing = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        updatable.update(dt)
        for rocks in asteroids:
            if rocks.collides_with(p_thing):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("Black")
        for things in drawable:
            things.draw(screen)
        pygame.display.flip()
        deltatime = clock.tick(60)
        dt = deltatime / 1000
        # print(dt)


if __name__ == "__main__":
    main()

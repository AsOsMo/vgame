import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


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
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, drawable, updatable)

    dt = 0
    p_thing = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a_thing = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        log_state()

        updatable.update(dt)

        for shot in shots:
            for rocks in asteroids:
                if rocks.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    rocks.kill()
                elif rocks.collides_with(p_thing):
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

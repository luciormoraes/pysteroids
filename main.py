# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *

def main():
    pygame.init()

    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    clock = pygame.time.Clock()  # Control frame rate
    dt = 0
    running = True
    colour = (0,0,0)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    player = Player(x,y)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(colour)

        updatable.update(dt)
        # player.draw(screen)
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        # player.update(dt)

        res = clock.tick(60)
        dt = res / 1000

    pygame.quit()

if __name__ == "__main__":
    main()



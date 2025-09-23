import pygame, constants
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        pygame.Surface.fill(screen,"black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()

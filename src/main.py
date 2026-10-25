import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from location import Location


def main():
    print("Hello from pquest!")
    print(f"Starting pquest with pygame version: {pygame.version.ver}")

    _ = pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0

    try:
        location = Location(1, "./resource/Location_1.png")
    except ValueError as ex:
        print("Location is not created. Abort the program.")
        return

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        location.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000   # regulates the running speed by passing the maximum frame-rate and the program will wait if needed.

#---------------------------------------------------------------------

if __name__ == "__main__":
    main()

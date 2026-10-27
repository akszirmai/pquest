import pygame

from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from src.location import Location
from src.logger import log_event, log_state


def main():
    print("Hello from pquest!")
    print(f"Starting pquest with pygame version: {pygame.version.ver}")

    _ = pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0

    try:
        location = Location(1, "./resource/Location_1.png")
        log_event("Location loaded")
    except ValueError as ex:
        print("Location is not created. Abort the program.")
        log_event(f"Location {1} loading failed")
        return

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        _ = screen.fill("black")
        location.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000   # regulates the running speed by passing the maximum frame-rate and the program will wait if needed.

#---------------------------------------------------------------------

if __name__ == "__main__":
    main()

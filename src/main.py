import pygame

from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from src.location import Location, World
from src.logger import log_event, log_state
from src.player import Player


def main():
    print("Hello from pquest!")
    print(f"Starting pquest with pygame version: {pygame.version.ver}")

    _ = pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0

    world = World("./resource/PQU_game_world.json")
    world.load_world()
#    print(world.world_details)
#    print(" ")
    try:
        world.process_read_world()
    except (ValueError, KeyError) as ex:
        print(f"{ex.args[0]} \nWorld loading FAILED !!! Program aborted")
        return



    for loc in world.locations:
        crn_str: str = ""
        for pnt in loc.corners:
            crn_str += f"({pnt.x}, {pnt.y}) "
#        print(f"ID: {loc.id}, imagefile: {loc.loc_img_path}, corner points:{crn_str}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player: Player = Player(200, 200)
    all_sprites = pygame.sprite.Group(player)

 #   all_sprites.add(player)

    while True:
#        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
#        print(f"Position {player.position}")
        _ = screen.fill("black")
        world.locations[0].draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000   # regulates the running speed by passing the maximum frame-rate and the program will wait if needed.

#---------------------------------------------------------------------

if __name__ == "__main__":
    main()

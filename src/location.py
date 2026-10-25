import pygame


class Location:

    def __init__(self, id: int, loc_img_path: str):
        self.id = id
        self.loc_img_path = loc_img_path
        self.loc_img : pygame.Surface
        print(f"Try loading image file from: {self.loc_img_path}")

        load_res : int = self.load_image(self.loc_img_path)
        if load_res != 0:
            print(f"Location {self.id} cannot be initiated.")
            raise ValueError(f"Failed to create Location {self.id}")


    def load_image(self, img_file: str) -> int:
        try:
            self.loc_img = pygame.image.load(img_file)
        except FileNotFoundError:
            print(f"Location image file: {img_file} cannot be found")
            return 1
        except Exception as ex:
            template= "Some other type of exception with type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return 2
        self.imagerect = self.loc_img.get_rect()
        return 0

    def draw(self, screen : pygame.Surface) -> None:
        pygame.draw.circle(screen, "red", pygame.Vector2(200, 200), 20*self.id, 3)
        screen.blit(self.loc_img, self.imagerect)

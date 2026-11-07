from dataclasses import dataclass
import json
from typing import Any

import pygame
from pygame.rect import Rect

from src.constants import (
    LOC_IMAGE_LOAD_FAIL,
    LOC_IMAGE_LOAD_SUCCESS,
    LOC_IMAGE_NOT_FOUND,
)

@dataclass
class Point:
    x: float
    y: float

class Location:

    def __init__(self, id: int, name: str, loc_img_path: str):
        self.id = id
        self.name = name
        self.loc_img_path = loc_img_path
        self.loc_img : pygame.Surface
        self.imagerect : Rect
        self.corners : list[Point] = []

    def load_image(self, img_file: str) -> int:
        try:
            self.loc_img = pygame.image.load(img_file)
        except FileNotFoundError:
            print(f"Location image file: {img_file} cannot be found")
            return LOC_IMAGE_NOT_FOUND
        except Exception as ex:
            template= "Some other type of exception with type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return LOC_IMAGE_LOAD_FAIL
        self.imagerect = self.loc_img.get_rect()
        return LOC_IMAGE_LOAD_SUCCESS


    def set_corners(self, LL: Point, LR: Point, UR: Point, UL: Point):
        self.corners.append(LL)
        self.corners.append(LR)
        self.corners.append(UR)
        self.corners.append(UL)


    def draw(self, screen : pygame.Surface) -> None:
        _ = pygame.draw.circle(screen, "red", pygame.Vector2(200, 200), 20*self.id, 3)
        _ = screen.blit(self.loc_img, self.imagerect)

class World:

    def __init__(self, world_desc_path: str):
        self.world_desc_path = world_desc_path
        self.world_details: dict[str, Any] = {}
        self.locations : list[Location] = []

    def process_read_world(self):
        print(self.world_details["locations"])

        for loc_data in self.world_details["locations"]:
            try:
                loc_ID : int = loc_data["ID"]
                loc_name : str = loc_data["name"]
                loc_image_file : str = loc_data["image name"]
            except KeyError as ex:
                raise ValueError(f"Location data detail \"{ex.args[0]}\" is not found")

            location: Location = Location(loc_ID, loc_name, "./resource/" + loc_image_file)
            print(f"Try loading image file from: {loc_image_file}")
            load_res : int = location.load_image(location.loc_img_path) # Later to replace it, no need for the parameter, since it is an already set property

            if load_res != 0:
                print(f"Location {loc_ID} cannot be initiated.")
                raise ValueError(f"Failed to create Location {loc_ID}. Abort")
            self.locations.append(location)

            cp_LL: Point | None = None
            cp_LR: Point | None = None
            cp_UR: Point | None = None
            cp_UL: Point | None = None

            for cornertype, cornerpoint in loc_data["corners"].items():   # cornerpoint - a dictionary of 4 elements: LL, LR, UR and UL
                if cornertype == "LL":
                    cp_LL = Point(cornerpoint["x"], cornerpoint["y"])
                    continue
                if cornertype == "LR":
                    cp_LR = Point(cornerpoint["x"], cornerpoint["y"])
                    continue
                if cornertype == "UR":
                    cp_UR = Point(cornerpoint["x"], cornerpoint["y"])
                    continue
                if cornertype == "UL":
                    cp_UL = Point(cornerpoint["x"], cornerpoint["y"])
                    continue
                raise ValueError(f"Unidentified cornertype {cornertype}")

            if cp_LL == None or cp_LR == None or cp_UR == None or cp_UL == None:
                raise ValueError("At least one corner point value is missing")
            location.set_corners(cp_LL, cp_LR, cp_UR, cp_UL)


    def load_world(self):
        with open(self.world_desc_path, 'r') as f:
            self.world_details = json.load(f)

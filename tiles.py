import pygame
from window_size import TILE_HEIGHT,TILE_WIDTH
class Tile:
    image_path = "sprites/tile_image.png"
    is_traversable = True
    def __init__(self,x,y):
        
        self.x =x
        self.y =y

    @classmethod
    def get_image_path(cls):
        return cls.image_path
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class GroundTile(Tile):
    image_path = "sprites/ground_tile_image.png"

    is_traversable = True
    def __init__(self, x, y):
        super().__init__(x,y)
class WallTile(Tile):
    image_path = "sprites/wall_tile_image.png"

    is_traversable = False
    
    def __init__(self, x, y):
        super().__init__(x,y)

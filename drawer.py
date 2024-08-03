import window_size
import tiles
import pygame
from player import Player
class Drawer:
    tile_images = {}
    player_image = None
    def __init__(self):
        tile_classes = tiles.Tile.__subclasses__()
        #tile image initialization
        for tile_class in tile_classes:
            self.tile_images[tile_class] = Drawer.__initialize_image(tile_class.get_image_path())
        
        #player image initialization
        Drawer.player_image = pygame.image.load(Player.get_image_path())
        Drawer.player_image = pygame.transform.scale(Drawer.player_image,(window_size.PLAYER_WIDTH,window_size.PLAYER_HEIGHT))
    
    @staticmethod
    def __initialize_image(path):
        new_image = pygame.image.load(path)
        new_image = pygame.transform.scale(new_image,(window_size.TILE_WIDTH,window_size.TILE_HEIGHT))
        return new_image
    @staticmethod   
    def draw_scene(canvas,player,tiles):
        canvas.fill(0)
        Drawer.draw_tiles(canvas,tiles,player)
        Drawer.draw_player(canvas,player)
    @classmethod
    def draw_player(cls,canvas,player):
        canvas.blit(cls.player_image,(window_size.WINDOW_WIDTH/2-window_size.PLAYER_WIDTH/2,window_size.WINDOW_HEIGHT/2-window_size.PLAYER_HEIGHT/2))
    @classmethod
    def draw_tiles(cls,canvas,tiles_to_draw,player):
        
        for tile in tiles_to_draw:
            tile_screen_x,tile_screen_y = Drawer.calculate_screen_position(tile,player)
            canvas.blit(cls.tile_images[type(tile)],(tile_screen_x,tile_screen_y))

    #take a tile position (3,3)
    #subtract the player position (3,3) - (2,2) = (1,1)
    #scale the position up to screen (1,1) * 16 = (16,16)
    #add (half the screen - player width) to adjust for the player being in the middle
    @staticmethod
    def calculate_screen_position(tile,player):
        relative_x = tile.get_x()-player.get_x()
        relative_y = tile.get_y()-player.get_y()
        scaled_x = relative_x*window_size.TILE_WIDTH
        scaled_y = relative_y*window_size.TILE_HEIGHT
        adjusted_x = scaled_x+(window_size.WINDOW_WIDTH/2-window_size.PLAYER_WIDTH/2)
        adjusted_y = scaled_y+(window_size.WINDOW_HEIGHT/2-window_size.PLAYER_HEIGHT/2)
        return (adjusted_x,adjusted_y)
        

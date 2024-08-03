import pygame
from player import Player
import map_strings
from drawer import Drawer
from tile_map import TileMap
import window_size
import title_screen_images
from sprite_sheet_utils.glerb_alphabet import alphabet_sprites
#make window
canvas = pygame.display.set_mode((window_size.WINDOW_WIDTH,window_size.WINDOW_HEIGHT))

#make clock
game_clock = pygame.time.Clock()
fps = 120

#make player
player = Player(5,5,window_size.PLAYER_WIDTH/window_size.TILE_WIDTH,window_size.PLAYER_HEIGHT/window_size.TILE_HEIGHT)

#make drawer
drawer = Drawer()

#make map
starting_map = TileMap(map_strings.map_string)
movement_key_queue= []

#scene
scene = "game"

#game loop
running = True
while running:
    user_events = pygame.event.get()
    #events
    for event in user_events:
        if event.type == pygame.QUIT:
            running = False
        

    match scene:
        case "title":
            canvas.blit(title_screen_images.title,(0,0))


            pygame.display.update()
            game_clock.tick(fps)

        case "game":
            for event in user_events:
                player.update_movement_queue(event)

            player.movement(starting_map)
    
            drawer.draw_scene(canvas,player,starting_map.tiles)

            pygame.display.update()
            game_clock.tick(fps)
        case _:
            raise Exception("Scene Error")



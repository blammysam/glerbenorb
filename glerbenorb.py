import pygame
from map_game.player import Player
import map_game.map_strings as map_strings
from map_game.drawer import Drawer
from map_game.tile_map import TileMap
import window_size
from button_and_button_accessories.button import Button
from title_screen.title_screen import TitleScreen
from scene_state import SceneState
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
SceneState.set_scene_state("title")

#game loop
running = True

while running:
    user_events = pygame.event.get()
    #events
    for event in user_events:
        if event.type == pygame.QUIT:
            running = False
        

    match SceneState.get_scene_state():
        case "title":
            TitleScreen.update_buttons(user_events)
            TitleScreen.display(canvas)
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



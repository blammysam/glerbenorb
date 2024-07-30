import pygame
from player import Player
import map_strings
from drawer import Drawer
from tile_map import TileMap
import window_size
#make window
canvas = pygame.display.set_mode((window_size.WINDOW_WIDTH,window_size.WINDOW_HEIGHT))

#make clock
game_clock = pygame.time.Clock()
fps = 120

#make player
player = Player(5,5,2,2)

key_presses = {"up":0,"down":0,"right":0,"left":0}

#make drawer
drawer = Drawer()

#make map
starting_map = TileMap(map_strings.map_string)

def event_checks():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                key_presses["left"] = 1
            if event.key == pygame.K_d:
                key_presses["right"] = 1
            if event.key == pygame.K_w:
                key_presses["up"] = 1
            if event.key == pygame.K_s:
                key_presses["down"] = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key_presses["left"] = 0
            if event.key == pygame.K_d:
                key_presses["right"] = 0
            if event.key == pygame.K_w:
                key_presses["up"] = 0
            if event.key == pygame.K_s:
                key_presses["down"] = 0
#game loop
running = True
while running:
    event_checks()
        
    print(player.get_x(),player.get_y())
    player.movement(key_presses)
    #background
    
    drawer.draw_scene(canvas,player,starting_map.tiles)

    pygame.display.update()
    game_clock.tick(fps)


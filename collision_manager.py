import math

class CollisionManager:


    @staticmethod
    def attempt_player_move(direction,player,tile_map):
        near_tiles = CollisionManager.get_near_tiles(tile_map,player)
        for tile in near_tiles:

            player_collided_position = CollisionManager.check_collision(player,direction,tile)
            if(player_collided_position is not None):
                return (player_collided_position[0],player_collided_position[1])
        normal_move_position = (player.get_x()+ player.get_walk_speed()*direction[0],player.get_y()+player.get_walk_speed()*direction[1])
        return normal_move_position
               
                

    @staticmethod
    def check_collision(player,direction,tile):
        if tile.is_traversable is True:
            return None
        #get the player position
        player_left = player.get_x()
        player_top = player.get_y()
        player_right = player_left + player.get_width()
        player_bottom = player_top + player.get_height()

        #get tile position
        tile_left = tile.get_x()
        tile_top = tile.get_y()
        tile_middle_x = tile_left +0.5
        tile_middle_y = tile_top +0.5
        #----- actually the start of the next tile 
        tile_right = tile_left+1
        tile_bottom = tile_top+1

        #player position if they were to move uninterrupted
        next_player_x = player.get_x()+(player.get_walk_speed()*direction[0])
        next_player_y = player.get_y()+(player.get_walk_speed()*direction[1])
        
        #to be returned for player use
        after_collision_player_x = player_left
        after_collision_player_y = player_top
        
        collided = False
        #if in the next frame the player would overlap the tile,
        # then check which side of the center the original player position is
        # then send the position next to the tile back to the player (return it)
        if(CollisionManager.check_box_collision(next_player_x,player_top,player.get_width(),player.get_height(),tile.get_x(),tile.get_y(),1,1)):
            collided = True
            #player on left 
            if(player_right < tile_middle_x): 
                #move player to the left - 1
                after_collision_player_x = tile_left-player.get_width()
            #player on right
            elif(player_left >= tile_middle_x):
                after_collision_player_x = tile_right
            
        if(CollisionManager.check_box_collision(player_left,next_player_y,player.get_width(),player.get_height(),tile.get_x(),tile.get_y(),1,1)):
            collided = True
            #player on top
            if(player_bottom < tile_middle_y):
                after_collision_player_y = tile_top-player.get_height()
            #player below
            elif(player_top >= tile_middle_y):
                after_collision_player_y = tile_bottom
        if(collided):
            print("colided")
            return (after_collision_player_x,after_collision_player_y)
        else:
            return None

        

    @staticmethod
    def check_box_collision(x1,y1,w1,h1,x2,y2,w2,h2):
        if (x1+w1 > x2 and x1 < x2+w2 and y1 + h1 > y2 and y1 < y2 + h2):
            return True
        return False
    @staticmethod
    def get_near_tiles(tile_map, player):
        near_tiles = []
        #just added int() to player.width/height to quick fix -- might cause problems
        for i in range(int(player.width)+3):
            for j in range(int(player.height)+3):
                near_tile = tile_map.tile_positions.get((math.floor(player.get_x())-1+j,math.floor(player.get_y())-1+i))
                if(near_tile is not None):
                    near_tiles.append(near_tile)
        return near_tiles

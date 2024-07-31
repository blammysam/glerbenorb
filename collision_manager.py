import math

class CollisionManager:


    @staticmethod
    def attempt_player_move(direction,player,tile_map):
        near_tiles = CollisionManager.get_near_tiles(tile_map,player)
        for tile in near_tiles:
            #only check collision if tile is not traversable
            if not tile.is_traversable:
                
                on_side_x,on_side_y = CollisionManager.calculate_on_sides(player,tile)
                player_stop_position = CollisionManager.check_overlaps_for_player_stop_position(player,direction,on_side_x,on_side_y,tile)
                if(player_stop_position is not None):
                    return player_stop_position
        return None
               
                

    @staticmethod
    def check_overlaps_for_player_stop_position(player,direction,on_side_x,on_side_y,tile):
        new_player_x = player.get_x()
        new_player_y = player.get_y()
        
        collided = False
        
        if(on_side_y == "overlap"):

            if(on_side_x == "left" and direction[0] == 1):
                #if player overlaps from the left (o -> |)
                if(player.get_x()+player.get_width()+player.get_walk_speed()>=tile.get_x()):

                    new_player_x = tile.get_x()-player.get_width()
                    collided = True
                #if player overlaps from the right (| <- o)
            elif(on_side_x == "right" and direction[0] == -1):
                if(player.get_x() - player.get_walk_speed() <= tile.get_x() + 1):
                    new_player_x = tile.get_x()+1
                    collided = True
        #if overlapping on X axis, check either side on y axis
        if(on_side_x == "overlap"):
            if(on_side_y == "up" and direction[1] == 1):
                #if player overlaps from the top
                if(player.get_y()+player.get_height()+player.get_walk_speed()>=tile.get_y()):
                    new_player_y = tile.get_y()-player.get_height()
                    collided = True
            elif(on_side_x == "down" and direction[1] == -1):
                #if player overlaps from the bottom
                if(player.get_y() - player.get_walk_speed() <= tile.get_y() + 1):
                    new_player_y = tile.get_y()+1
                    collided = True
        if collided is True:
            print("COLLIDED")
            print(new_player_x,new_player_y)
            return (new_player_x,new_player_y)
        else:
            return None

                
    @staticmethod
    def calculate_on_sides(player,tile):
        on_side_x = None
        on_side_y = None
        if(player.get_x() + player.get_width() < tile.get_x()):
            on_side_x = "left"
        elif(player.get_x() > tile.get_x()+1):
            on_side_x = "right"
        else:
            on_side_x = "overlap"
        if(player.get_y() + player.get_height() < tile.get_y()):
            on_side_y = "up"
        elif(player.get_y() > tile.get_y()+1):
            on_side_y = "down"
        else:
            on_side_y = "overlap"
        return on_side_x,on_side_y
            
                    
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

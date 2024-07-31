from collision_manager import CollisionManager

class Player:
    image_path = "sprites/player_image.png"
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.walk_speed = 0.1
        self.width = width
        self.height = height
    @classmethod
    def get_image_path(cls):
        return cls.image_path
    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y = y
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_walk_speed(self):
        return self.walk_speed
    def movement(self,key_presses,tile_map):
        #movement updates
        x_direction = key_presses["right"]-key_presses["left"]
        y_direction = key_presses["down"]-key_presses["up"]
        
        stop_position = CollisionManager.attempt_player_move((x_direction,y_direction),self,tile_map)
        if(stop_position is None):
                
            self.x+=x_direction*self.walk_speed
            if(x_direction == 0):
                self.y+=y_direction*self.walk_speed
        else:
            self.set_x(stop_position[0])
            self.set_y(stop_position[1])
    




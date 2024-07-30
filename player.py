import pygame

class Player:
    image_path = "sprites/player_image.png"
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.max_walk_speed = 0.1
        self.width = width
        self.height = height
    @classmethod
    def get_image_path(cls):
        return cls.image_path
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def movement(self,key_presses):
        #movement updates
        x_direction = key_presses["right"]-key_presses["left"]
        y_direction = key_presses["down"]-key_presses["up"]
        self.x+=x_direction*self.max_walk_speed
        if(x_direction == 0):
            self.y+=y_direction*self.max_walk_speed
    




from .collision_manager import CollisionManager
import pygame
class Player:
    image_path = "sprites/player_image.png"
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.walk_speed = 0.1
        self.width = width
        self.height = height
        self.movement_queue = []
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
    def discard_from_movement_queue(self,direction):
        if direction in self.movement_queue:
            self.movement_queue.remove(direction)
    def update_movement_queue(self,event):   
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.discard_from_movement_queue("left")
                self.movement_queue.insert(0,"left")
            if event.key == pygame.K_d:
                self.discard_from_movement_queue("right")
                self.movement_queue.insert(0,"right")
            if event.key == pygame.K_w:
                self.discard_from_movement_queue("up")
                self.movement_queue.insert(0,"up")
            if event.key == pygame.K_s:
                self.discard_from_movement_queue("down")
                self.movement_queue.insert(0,"down")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.discard_from_movement_queue("left")
            if event.key == pygame.K_d:
                self.discard_from_movement_queue("right")
            if event.key == pygame.K_w:
                self.discard_from_movement_queue("up")
            if event.key == pygame.K_s:
                self.discard_from_movement_queue("down")
    def movement(self,tile_map):

        direction_vectors = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}
        if(len(self.movement_queue)==0):
            direction_vector = (0,0)
        else:
            direction_vector = direction_vectors[self.movement_queue[0]]
        
        
        new_position = CollisionManager.attempt_player_move(direction_vector,self,tile_map)
        self.set_x(new_position[0])
        self.set_y(new_position[1])





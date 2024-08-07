import pygame
from .glerb_alphabet import font_sprites
class Button:
    def __init__(self, position, button_size=None, text=None,font_size=None,click_function = None):
        self.position = position
        self.text = text
        self.selected = False
        self.font_size = font_size
        self.button_size=button_size
        self.letter_spacing = 2
        if(font_size is None):
            self.font_size = Button.calculate_font_size(self.button_size,self.text,self.letter_spacing)
        
        self.button_surface = pygame.Surface(self.button_size)
        self.button_surface.fill((255,255,255))
        for i,character in enumerate(self.text):
            font_sprites[character] = pygame.transform.scale(font_sprites[character],(self.font_size,self.font_size))
            self.button_surface.blit(font_sprites[character],((self.letter_spacing*i)+(i*self.font_size),0))

        
    @staticmethod
    def calculate_font_size(button_size, text,letter_spacing):
        #find the width fit (add width padding here)
        char_count = len(text)

        font_size = int((button_size[0]-(1+char_count*letter_spacing))/len(text))

        #if that size is bigger than the height, then return the height
        if(font_size > button_size[1]):
            #(add height padding here)
            return button_size[1]
        return font_size
    
    def display(self, canvas):
        canvas.blit(self.button_surface,self.position)
            
            
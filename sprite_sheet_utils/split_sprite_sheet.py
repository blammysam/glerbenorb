import pygame

def split_sprite_sheet(path,sprite_size):
    sheet = pygame.image.load(path)
    sheet_size = sheet.get_size()
    sprites_in_row = int(sheet_size[0]/sprite_size[0])
    sprites_in_column = int(sheet_size[1]/sprite_size[1])

    sprites = []
    for col in range(sprites_in_column):
        for row in range(sprites_in_row):
            sprite = pygame.Surface(sprite_size,pygame.SRCALPHA)
            sprite.blit(sheet,(0,0),pygame.Rect(col*sheet_size[0],row*sheet_size[1],sprite_size[0],sprite_size[1]))
            sprites.append(sprite)
    
    return sprites

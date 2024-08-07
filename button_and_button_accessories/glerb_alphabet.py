from .split_sprite_sheet import split_sprite_sheet
from string import ascii_lowercase
sprite_list=split_sprite_sheet("sprites/glerb_font_sprite_sheet.png",(200,200))
character_list = ascii_lowercase + " !?."
font_sprites = {}
for i,character in enumerate(character_list):
    font_sprites[character] = sprite_list[i]


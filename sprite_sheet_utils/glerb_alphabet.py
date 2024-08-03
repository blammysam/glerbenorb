from .split_sprite_sheet import split_sprite_sheet
from string import ascii_lowercase
letter_sprite_list=split_sprite_sheet("sprites/glerb_alphabet_sprite_sheet.png",(200,200))
alphabet_sprites = {}
for i,letter in enumerate(ascii_lowercase):
    alphabet_sprites[letter] = letter_sprite_list[i]


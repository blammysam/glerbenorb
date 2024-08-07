from button_and_button_accessories.button import Button
from scene_state import SceneState
import pygame

class TitleScreen:
    @staticmethod
    def game_start():
        SceneState.set_scene_state("game")

    title_image = pygame.image.load("sprites/title_screen_image.png")
    play_button = Button((700,400),(200,70),"start",click_function = game_start)
    @staticmethod
    def display(canvas):
        canvas.blit(TitleScreen.title_image,(0,0))
        TitleScreen.play_button.display(canvas)
    @staticmethod
    def update_buttons(user_events):
        for event in user_events:
            if(event.type == pygame.KEYDOWN):

                
                if event.key == pygame.K_RETURN:
                    TitleScreen.game_start()

    
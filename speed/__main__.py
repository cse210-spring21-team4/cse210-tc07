from game.director import Director
from game.input_service import Input_Service
from game.output_service import Output_Service
from asciimatics.screen import Screen
from game.menu import Menu

menu = Menu()


def main(screen):
    input_service = Input_Service(screen)
    output_service = Output_Service(screen)
    director = Director(input_service, output_service, menu.player)
    director.start_game()


while menu.main_menu():
    Screen.wrapper(main)

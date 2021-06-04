from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 
from game.menu import Menu


def main(screen, player=str):

    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game(player)


menu = Menu()
while menu.main_menu():
    Screen.wrapper(main, menu.player)

import logging
from typing import Callable
from levelup.controller import GameController
from levelup.direction import Direction

VALID_DIRECTIONS = [x.value for x in Direction]
VALID_COMMANDS = VALID_DIRECTIONS + ['q']
VALID_START_COMMANDS = ['s'] + ['q']
# This is prewritten for you. You should only have to change it to make the text copy match what your prompts should say
class GameApp:

    controller: GameController
    starting_pos = (-100,-100)

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
            else:
                print(f"{response} is an invalid input. Try again.")    
        return response

    def create_character(self):
        print("Welcome to Level Up Game")
        print("")
        print("                      %,,,,,,,,,,,,,,,,,,%/,,,,,,,,,,,,,,,,,.                   ")
        print("                    #%,,,,,,,,,,,,,,,,,,  %%,,,,,,,,,,,,,,,,,,                  ")
        print("                   %,,,,,,,,,,,,,,,,,,,    #%,,,,,,,,,,,,,,,,,,.                ")
        print("                 *%*******************      ,%*******************               ")
        print("                %/*******************         %*******************              ")
        print("              .%,,,,,,,,,,,,,,,,,,,,           %,,,,,,,,,,,,,,,,,,,,            ")
        print("             %#,,,,,,,,,,,,,,,,,,,.             %*,,,,,,,,,,,,,,,,,,,           ")
        print("            %,,,,,,,,,,,,,,,,,,,,                %#,,,,,,,,,,,,,,,,,,,,         ")
        print("          %&,,,,,,,,,,,,,,,,,,,,                  %&,,,,,,,,,,,,,,,,,,,,        ")
        print("         %.....................                    /%.....................      ")
        print("       %&.....................                       %.....................     ")
        print("      %......................                         %.....................    ")
        print("    #%.....................                            %......................  ")
        print("     /%...................                              %*...................   ")
        print("       %.................                                %&................     ")
        print("        #%,,,,,,,,,,,,,,***,,,,,                  %(,,,*****,,,,,,,,,,,,,,      ")
        print("          %,,,,,,,,,,,,****,,,,,                  %#,,,******,,,,,,,,,,,.       ")
        print("           %%*********/****,,,,,                  %%,,,*****,,*********         ")
        print("             %*******//****,,,,,                  %%,,,*****,,,******,          ")
        print("              %%///////****,,,,,                  %%,,,*****,,,,////            ")
        print("                %//////****,,,,,                  %&,,,*****,,,,,,/             ")
        print("                 %%////****,,,,,                  %&,,,*****,,,,,               ")
        print("                  .%///****,,,,,                  %%,,,*****,,,,                ")
        print("                    %//****,,,,,                  %%,,,*****,,.                 ")
        print("                     %%****,,,,,                  (%,,,*****,                   ")
                                                                                


        response = self.prompt("Press <s> to start the game or <q> to quit", lambda x: x in VALID_START_COMMANDS)
        if response == 'q':
            self.quit()
        character = self.prompt("Enter character name and press <Enter> to continue: ", lambda x: len(x) > 0)
        self.controller.create_character(character)
        print(f"Your character name is: {self.controller.status.character_name}")

    def move_loop(self):
        print(f"Your starting position is at {self.controller.status.current_position}")
        while True:
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or q to quit)",
                lambda x: x in VALID_COMMANDS,
            )
            if response == 'q':
                self.quit()
            direction = Direction(response)
            self.controller.move(direction)
            print(f"You moved {direction.name}")
            print(self.controller.status)
            for x in range(8,-1,-1):
                for y in range(9):
                    if (y,x) == self.controller.status.current_position:
                        print('P', end=' ')
                    else:
                        print('.', end=' ')
                print()
           
                

    def start(self):
        self.create_character()
        self.controller.start_game()
        self.starting_pos = self.controller.status.current_position
        self.move_loop()

    def quit(self):
        print(f"{self.controller.status.character_name} started at position: {self.starting_pos}")
        print(f"{self.controller.status.character_name} took {self.controller.status.move_count} moves.")
        print(f"{self.controller.status.character_name} ended at position: {self.controller.status.current_position}")
        # print(f"{self.controller.status.character_name} bounced off the edge of the map {self.controller.status.bounce_count} times.")
        print("")
        print("GAME OVER")
        print("")
        print("       ---_ ......._-_--.     ")
        print("      (|\ /      / /| \  \ ")
        print("      /  /     .'  -=-'   `.")
        print("     /  /    .'             )")
        print("   _/  /   .'        _.)   /")
        print("  / o   o        _.-' /  .'")
        print("  \          _.-'    / .'*|")
        print("   \______.-'//    .'.' \*|")
        print("      .  .// .'.' | _ _ \*|")
        print("      \`-|\_/ /    \ _ _ \*\ ")
        print("       `/'\__/      \ _ _ \*\ ")
        print("      /^|            \ _ _ \*")
        print("     '  `             \ _ _ \ ")
        print("                       \_")
        quit()

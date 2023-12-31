from levelup.character import Character
from levelup.direction import Direction
from levelup.map import Map
from levelup.position import Position




class GameStatus:
    character_name: str = ""
    current_position: tuple = (-100,-100)
    move_count: int = 0
    bounce_count: int = 0

    def __str__(self) -> str:
        return f"Character Name: {self.character_name} \t Character Position: {self.current_position} \t Character MoveCount: {self.move_count} \t Character BounceCount: {self.bounce_count}"

class GameController:
    status: GameStatus
    character: Character
    map: Map

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        if self.character == None:
            self.create_character(character_name="")
        self.map = Map()
        self.character.enter_map(self.map)           

        # Status code is written for you
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = 0
        self.status.bounce_count = 0

    # Pre-written for you
    def create_character(self, character_name: str) -> None:
        self.character = Character(character_name)
        self.status.character_name = self.character.name

    def move(self, direction: Direction) -> None:
        self.character.move(direction)

        # Status code is written for you
        if self.status.current_position == (self.character.current_position.x, self.character.current_position.y):
            self.status.bounce_count = self.status.bounce_count + 1
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = self.status.move_count + 1

    ## ************************************************
    ## METHODS THAT EXIST JUST TO HELP WITH TESTING -- PREWRITTEN FOR YOU
    ## ************************************************
    def set_character_position(self, xycoordinates: tuple) -> None:
        x = xycoordinates[0]
        y = xycoordinates[1]
        self.character.current_position = Position(x,y)
        self.status.current_position = xycoordinates

    def set_current_move_count(self, move_count: int) -> None:
        self.status.move_count = move_count

    def get_total_positions(self) -> int:
        return self.map.num_positions
    
    def initalize_game_for_testing(self) -> None:
        self.create_character("")
        self.start_game()

    

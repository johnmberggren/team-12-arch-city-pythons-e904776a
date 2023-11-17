from levelup.map import Map
from levelup.character import Character
from levelup.direction import Direction
from levelup.position import Position

class CharacterDouble (Character):

    ARBITRARY_POSITION = Position(5,5)
    is_move_called = False
    is_enter_map_called = False
    last_move_direction = None

    def __init__(self, character_name, current_postion=ARBITRARY_POSITION):
        self.current_position = current_postion
        print(self.current_position.x)
        print(self.current_position.y)

    def move(self, direction: Direction) -> None:
        self.last_move_direction = direction
        self.is_move_called=True
        self.current_position = self.map.calculate_new_position(self.current_position, direction)

    def enter_map(self, map: Map) -> None:
        self.is_enter_map_called=True

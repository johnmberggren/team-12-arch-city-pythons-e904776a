from levelup.position import Position
from levelup.direction import Direction
from levelup.map import Map

DEFAULT_CHARACTER_NAME = "Character"
is_move_called = False
is_enter_map_called = False
last_move_direction = None

class Character:
    # In python, we don't use getters. So no getPosition or getName for this class
    name = ""
    current_position :Position = Position(-100,-100)
    map :Map = Map()

    # Since python doesn't do method overloading, this is how we support a constructor with optional parameters
    def __init__(self, character_name=DEFAULT_CHARACTER_NAME):
        if character_name.strip() == '':
            self.name = DEFAULT_CHARACTER_NAME
        else:
            self.name = character_name

    def move(self, direction :Direction) -> None:
        self.last_move_direction = direction
        self.is_move_called=True
        self.current_position = self.map.calculate_new_position(self.current_position, direction)
    
    def enter_map(self, map :Map) -> None:
        self.is_enter_map_called=True
        self.map = map
        self.current_position = self.map.starting_position
        

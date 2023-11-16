from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    starting_position = Position(0,0)
    positions = []
    size: Tuple[int, int] = (10, 10)

    # Exists for easy testing
    num_positions = size[0]*size[1]

    def __init__(self):
        self.create_positions()

    def is_position_valid(self, position :Position) -> bool:
        # TODO: implement method here and remove the print statement below
        print("is_position_valid method not yet implemented")
        return False        

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        # TODO: implement method here and remove the print statement below
        print("calculate_new_position method not yet implemented")
        return None

    def create_positions(self) -> None:
        temp_pos = []
        for x in range(self.size[0]):
            y_range = []
            for y in range(self.size[1]):
                new_pos = Position(x,y)
                y_range.append(new_pos)
            temp_pos.append(y_range)
        self.positions = temp_pos

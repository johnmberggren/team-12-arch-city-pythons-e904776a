from unittest import TestCase
from levelup.position import Position


class TestPositionInitWithXY(TestCase):

    ARBITRARY_POSITION_X = 5
    ARBITRARY_POSITION_Y = 6


    def test_init(self):
        # Create a new position
        testPosition = Position(5, 6)
        self.assertEqual(testPosition.x, self.ARBITRARY_POSITION_X)
        self.assertEqual(testPosition.y, self.ARBITRARY_POSITION_Y)


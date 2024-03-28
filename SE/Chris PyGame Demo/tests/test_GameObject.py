
import sys, unittest, pygame
from pathlib import Path

# This assumes that 'tests' is a subdirectory of the root directory of the project.
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from objects.GameObject import GameObject

class TestStarObj(unittest.TestCase):

    def test_initialization(self):
        """Test that a StarObj initializes with the correct attributes."""
        # Sets initial values for game object
        x_pos, y_pos, speed, is_player = 100, 150, 200, True
        # Dummy screen for testing (no real output)
        pygame.display.set_mode((100, 100))
        # Creates an instance of the game object
        obj = GameObject("sprites/ship.png", x_pos, y_pos, speed, is_player)
        # Checks if x value was set correctly
        self.assertEqual(obj.x, x_pos)
        # Checks if y value was set correctly
        self.assertEqual(obj.y, y_pos)
        # Checks if speed value was set correctly
        self.assertEqual(obj.speed, speed)
        # Checks if is_player value was set correctly
        self.assertEqual(obj.is_player, is_player)
        # Checks if x_dir defaulted correctly
        self.assertEqual(obj.x_dir, 0)
        # Checks if y_dir defaulted correctly
        self.assertEqual(obj.y_dir, 0)
        # Test other attributes as needed.

    def test_move_left(self):
        """Test the move method updates the position correctly."""
        # Sets initial values for game object
        x_pos, y_pos, speed, is_player = 100, 150, 200, True
        # Dummy screen for testing (no real output)
        pygame.display.set_mode((100, 100))
        # Creates an instance of the game object
        obj = GameObject("sprites/ship.png", x_pos, y_pos, speed, is_player)
        obj.move_left(1000)  # Move left horizontally
        self.assertNotEqual(obj.x_dir, 0)
        self.assertEqual(obj.y_dir, 0)

    def test_move_right(self):
        """Test the move method updates the position correctly."""
        # Sets initial values for game object
        x_pos, y_pos, speed, is_player = 100, 150, 200, True
        # Dummy screen for testing (no real output)
        pygame.display.set_mode((100, 100))
        # Creates an instance of the game object
        obj = GameObject("sprites/ship.png", x_pos, y_pos, speed, is_player)
        obj.move_right(1000) # Move right horizontally
        self.assertNotEqual(obj.x_dir, 0, "Failed to move object right")
        self.assertEqual(obj.y_dir, 0)

    '''
    def test_move(self):
        """Test the move method updates the position correctly."""
        x_pos, y_pos = 100, 150
        star = StarObj(x_pos, y_pos)
        initial_x, initial_y = star.x, star.y
        star.move(1, 0, 1000)  # Move horizontally
        self.assertNotEqual(star.x, initial_x)
        self.assertEqual(star.y, initial_y)

    
    def test_set_flicker(self):
        """Test that the set_flicker method updates the dimness and colour."""
        star = StarObj(100, 150)
        initial_colour = star.colour
        star.set_flicker()
        self.assertNotEqual(star.colour, initial_colour)

    def test_reroll(self):
        """Test that the reroll method updates star attributes."""
        star = StarObj(100, 150)
        star.reroll(200, 300)
        self.assertEqual(star.x, 200)
        self.assertEqual(star.y, 300)
        # You might want to test other attributes that should change with reroll.
    '''
        
if __name__ == '__main__':
    unittest.main()
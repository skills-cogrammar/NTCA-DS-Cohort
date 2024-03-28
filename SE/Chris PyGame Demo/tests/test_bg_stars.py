
import sys, unittest
from pathlib import Path

# This assumes that 'tests' is a subdirectory of the root directory of the project.
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from objects.bg_stars import StarObj

class TestStarObj(unittest.TestCase):

    def test_initialization(self):
        """Test that a StarObj initializes with the correct attributes."""
        x_pos, y_pos = 100, 150
        star = StarObj(x_pos, y_pos)
        self.assertEqual(star.x, x_pos)
        self.assertEqual(star.y, y_pos)
        # Test other attributes as needed.

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

if __name__ == '__main__':
    unittest.main()
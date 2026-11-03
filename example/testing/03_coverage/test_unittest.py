
import unittest
from app import Shape


class TestShape(unittest.TestCase):

    def test_triangle_angles(self):
        shape = Shape("triangle")
        self.assertEqual(shape.get_angles, (60, 60, 60))

    def test_square_angles(self):
        shape = Shape("square")
        self.assertEqual(shape.get_angles, (90, 90, 90, 90))

    def test_rectangle_angles(self):
        shape = Shape("rectangle")
        self.assertEqual(shape.get_angles, (90, 90, 90, 90))

    def test_invalid_shape(self):
        shape = Shape("circle")
        with self.assertRaises(ValueError):
            shape.get_angles


if __name__ == "__main__":
    unittest.main()

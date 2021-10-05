import unittest
from numpy import pi
from geometry import Circle
from geometry import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.center = (1,1,1)
        self.l1, self.l2 = 2,3

    def create_rectangle(self) -> Rectangle:
        return Rectangle(self.center, self.l1, self.l2)

    # tetsing starts here -all tests must start with the word test_

    # test creating rectangles
    def test_create_rectangle(self) -> None:
        rec = self.create_rectangle()
        self.assertEqual(rec._center,  (self.center))
        self.assertEqual(rec._l1,  self.l1)
        self.assertEqual(rec._l2,  self.l2)

    def test_no_tuple_origin_rectangle(self) -> None:
        with self.assertRaises(TypeError):
            rec = Rectangle((0),2,3)

    def test_not_valid_rectangle(self) -> None:
        with self.assertRaises(TypeError):
            rec = Rectangle((0,0,0),1)

    # test __eq__ ==

    def test_2_rec_equal_not_equal(self):
        rec1 = self.create_rectangle()
        rec2 = Rectangle((1,1,1), 3, 2)
        rec3 = Rectangle((1,1,1), 3, 3)
        self.assertEqual (rec1, rec2)
        self.assertNotEqual (rec1, rec3)

class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.center = (0,0,0)
        self.radius = 4
    
    def create_circle(self):
        return Circle(self.center, self.radius)

    def test_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle((0,0,0), -1)
        with self.assertRaises(TypeError):
            circle = Circle((0,0,0), "one")

if __name__ == "__main__":
    unittest.main()
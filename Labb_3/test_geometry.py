import unittest
from numpy import pi
from geometry import Circle, Rectangle, Cube, Sphere


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
        self.radius = 1
    
    def create_circle(self) -> "Circle":
        return Circle(self.center, self.radius)

    def test_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle((0,0,0), -1)
        with self.assertRaises(TypeError):
            circle = Circle((0,0,0), "one")

    def test_area(self):
        circle1 = self.create_circle()
        self.assertAlmostEqual(circle1.area(), pi)
        circle2 = Circle((0,0,0),2)
        self.assertAlmostEqual(circle2.area(), 4 * pi)
    
    def test_adding_circles(self):
        circle1 = self.create_circle()
        circle2 = Circle((0,0,0),2)
        self.assertEqual(circle1 + circle2, Circle((0,0,0),3))
    
    def test_adding_circle_with_rect(self):# Usefull test, had forgotten error raise on Circle __add__ . Nothing happened, test did not finish.
        circle1 = self.create_circle()
        rect1 = Rectangle((1,1,1),2,3)
        with self.assertRaises(TypeError):
            no_shape = circle1 + rect1

class TestCube(unittest.TestCase):

    def setUp(self) -> None:
        self.center = (0,0,0)
        self.lenght = 3
    
    def create_cube(self)-> "Cube":
        return Cube(self.center, self.lenght)

    def test_cube_translate(self):
        cube1 = self.create_cube()
        cube1.translate(1,1,1)
        self.assertEqual(cube1._center, (1,1,1))

    def test_return_corner_coordinate(self):
            cube1 = self.create_cube()
            self.assertEqual(type(cube1._A), tuple)

class TestSphere(unittest.TestCase):

    def setUp(self) -> None:
        self.center = (0,0,0)
        self.radius = 1

    def create_sphere(self)-> "Sphere":
        return Sphere(self.center, self.radius)

    def test_volume(self):
        sphere1 = self.create_sphere()
        self.assertAlmostEqual(sphere1.volume(), (pi * 4)/3)



    

if __name__ == "__main__":
    unittest.main()
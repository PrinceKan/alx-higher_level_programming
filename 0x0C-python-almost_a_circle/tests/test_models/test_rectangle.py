#!/usr/bin/python3
""" Unittest for Rectangle class """
import unittest
from models.rectangle import Rectangle


class testclass(unittest.TestCase):
    """ This class contains unittests for Rectangle class """

    def test_instantiation(self):
        """ method that holds the tests related to __init__ method """
        r1 = Rectangle(5, 7)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(0, 2, 0, 0, None)
        self.assertNotEqual(r2.id, None)

    def test_private_attributes(self):
        """ checks if attributes are private """
        r1 = Rectangle(5, 5)
        with self.assertRaises(AttributeError):
            print(r1.__width)
        with self.assertRaises(AttributeError):
            print(r1.__height)
        with self.assertRaises(AttributeError):
            print(r1.__x)
        with self.assertRaises(AttributeError):
            print(r1.__y)

    def test_wrong_arguments_number(self):
        """ checks the number of arguments """
        with self.assertRaises(TypeError):
            r3 = Rectangle()
        with self.assertRaises(TypeError):
            r3 = Rectangle(15)
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 11, 21, 4, 7 , 23, 3, 5, 61)

    def test_validation(self):
        """ method to test validation of width, height, x and y """
        with self.assertRaises(TypeError):
            r3 = Rectangle("h", "j")
        with self.assertRaises(TypeError):
            r3 = Rectangle(5, "j")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "a", 8)
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, 3, "j")
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            r3 = Rectangle(-1, 16)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(6, 0)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, 5, -1, 7)
        with self.assertRaises(ValueError):
            r3 = Rectangle(5, 5, 7, -2)

    def test_area(self):
        """ test area method """
        r3 = Rectangle(5, 7)
        self.assertEqual(r3.area(), 35)

    def test_str(self):
        """ test str method """
        r3 = Rectangle(4, 6, 2, 1, 12)
        r4 = Rectangle(4, 9)
        s = str(r3)
        s2 = str(r4)
        self.assertEqual(s, "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(s2, "[Rectangle] (7) 0/0 - 4/9")

    def test_update(self):
        """ test update method """
        r3 = Rectangle(5, 3, 7, 2, 5)
        r3.update(1)
        s = str(r3)
        self.assertEqual(s, "[Rectangle] (1) 7/2 - 5/3")
        r3.update(1, 1, 6, 3, 6)
        s = str(r3)
        self.assertEqual(s, "[Rectangle] (1) 7/6 - 5/3")

    def test_updatek(self):
        """ test update method (*args and **kwargs) """
        r3 = Rectangle(5, 5, 5, 5, 5)
        r3.update(1, height=1)
        s = str(r3)
        self.assertEqual(s, "[Rectangle] (1) 5/5 - 5/5")
        r3.update(height=7, x=4, y=12, id=10, width=5)
        s = str(r3)
        self.assertEqual(s, "[Rectangle] (10) 4/12 - 5/7")

#!/usr/bin/python3

""" Unittest for Base class """
import unittest
from models.base import Base


class testclass(unittest.TestCase):
    """ This class contains unittests for Base class """
    def test_id(self):
        """ method that holds the tests related to id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(14)
        self.assertEqual(b2.id, 14)
        b3 = Base()
        self.assertEqual(b3.id, 2)

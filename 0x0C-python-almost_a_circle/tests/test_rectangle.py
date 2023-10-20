#!/usr/bin/python3
import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(8, 3), Base)

        
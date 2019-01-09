import unittest
import main

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

import unittest
from unittest.mock import patch
import io
import schoolsearch

class TestClass(unittest.TestCase):
   def runTest(self, given_answer, expected_out):
        with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=io.StringIO()) as fake_out:
            schoolsearch.main()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)
            
   def test_last_name_search(self):
       self.runTest("S: CORONADO\nQ", "CORONADO, DIMPLE, 6, 102, KERBS, BENITO")

   def test_last_name_search_bus(self):
       self.runTest("S: CORONADO B\nQ", "CORONADO, DIMPLE, 52")

   def test_last_name_search_bus(self):
       self.runTest("I\nQ", "1: 2\n" +
            "2: 13\n" +
            "3: 9\n" +
            "4: 15\n" +
            "5: 0\n" +
            "6: 21\n")

if __name__ == '__main__':
   unittest.main()
                 


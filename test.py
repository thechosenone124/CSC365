import unittest
from unittest.mock import patch
import io
import schoolsearch
      
prompt = ("S[tudent]: <lastname> [B[us]]\n" + "T[eacher]: <lastname>\n" 
         + "B[us]: <number>\n" + "G[rade]: <number> [H[igh]|L[ow]]\n" 
         + "A[verage]: <number>\n" + "I[nfo]\n" + "NR1: <number>\n" + "NR2: <number>\n" 
         + "NR3: <number>\n" + "NR4\n" + "NR5: [A[ll]|B[us]|G[rade]|T[eacher]\n" + "Q[uit]\n")
         
class TestClass(unittest.TestCase):
   def runTest(self, given_answer, expected_out):
        with patch('sys.stdin', io.StringIO(given_answer)), patch('sys.stdout', new=io.StringIO()) as fake_out:
            schoolsearch.main()
            self.assertEqual(fake_out.getvalue().strip(), (prompt + expected_out).strip())
   
   def test_quit(self):
      self.runTest("Q", "")
   def test_last_name_search(self):
       input = "S: CORONADO\nQ"
       self.runTest(input, "CORONADO DIMPLE 6 102 KERBS BENITO\n" + prompt)

   def test_last_name_search_bus(self):
       self.runTest("S: CORONADO B\nQ", "CORONADO DIMPLE 52\n" + prompt)

   def test_info(self):
       self.runTest("I\nQ", "0: 0\n" +
            "1: 2\n" +
            "2: 13\n" +
            "3: 9\n" +
            "4: 15\n" +
            "5: 0\n" +
            "6: 21\n" + prompt)
   def test_teacher(self):
      self.runTest("T: KERBS\nQ", "RACANELLO NOEL\n" + 
         "CORONADO DIMPLE\n" + 
         "BOYTER WAN\n" + 
         "KEMERER ROSETTA\n" +
         "DEMARTINI DEWAYNE\n" + prompt)
   def test_grade(self):
      self.runTest("G: 1\nQ", "SAELEE DANILO\n" + "GARTH JOHN\n" + prompt)
   def test_bus(self):
      self.runTest("B: 53\nQ", "CIGANEK MANIE 3 107\n" +
         "LINHART LELA 3 107\n" + 
         "CLECKLER FLOY 6 109\n" +          
         "CORKER CARTER 4 105\n" + 
         "WICINSKY TERESE 2 108\n" + 
         "WORBINGTON DEEDRA 4 112\n" + 
         "SPANICEK KENDRA 4 112\n" + 
         "DELUNA KRYSTAL 4 112\n" + 
         "COMO ZANDRA 4 112\n" + prompt)
   def test_grade_h(self):
      self.runTest("G: 2 H\nQ", "WICINSKY TERESE 3.22 HAMER GAVIN 53\n" + prompt)
   def test_grade_l(self):
      self.runTest("G: 2 L\nQ", "KOZOLA BUSTER 2.76 HAMER GAVIN 55\n" + prompt)
   def test_average(self):
      self.runTest("A: 2\nQ", "2: 2.946153846153846\n" + prompt)
      
   def test_class_teacher(self):
      self.runTest("NR1: 101\nQ", "DURAND CARLEE\n" + prompt)
   def test_class_student(self):
      self.runTest("NR2: 108\nQ", "HAMER GAVIN\n" + prompt)
   def test_grade_teacher(self):
      self.runTest("NR3: 1\nQ", "FALKER ADOLPH\n" + prompt)
   def test_grade_teacher(self):
      self.runTest("NR4\nQ", "101 : 1\n" +
      "102 : 5\n" +
      "103 : 2\n" +
      "104 : 2\n" +
      "105 : 6\n" +
      "106 : 2\n" +
      "107 : 7\n" +
      "108 : 11\n" +
      "109 : 5\n" +
      "110 : 2\n" +
      "111 : 9\n" +
      "112 : 8\n" + prompt)
      
   def test_error_student(self):
      self.runTest("S: B C D\nQ", prompt)
   def test_error_teacher(self):
      self.runTest("T: B C\nQ", prompt)

if __name__ == '__main__':
   suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
   unittest.TextTestRunner(verbosity=2).run(suite)

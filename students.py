grades = ["kindergarten", "1st grade", "2nd grade", "3rd grade", "4th grade", "5th grade", "6th grade"]
def printStudent (StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName) : 
   return (StFirstName + " " + StLastName + " who takes bus route " + 
      Bus + ", is a " + grades[Grade] + " student assigned to the class of "
      + TFirstName + " " + TLastName + " in the classroom " + Classroom 
      + ". He has a GPA of " + GPA + ".")
   
def main():
   instr = ""

   while True:
      instr = input("S[tudent]: <lastname> [B[us]]\n" + "T[eacher]: <lastname>\n" + 
         "B[us]: <number>\n" + "G[rade]: <number> [H[igh]|L[ow]]\n" + 
         "A[verage]: <number>\n" + "I[nfo]\n" + "Q[uit]\n")

      instrs = instr.split(" ")

      if instrs[0] == "S:" or instrs[0] == "Student:":
         print("S")
      elif instrs[0] == "T:" or instrs[0] == "Teacher:":
         print("T")
      elif instrs[0] == "B:" or instrs[0] == "Bus:":
         print("B")
      elif instrs[0] == "G:" or instrs[0] == "Grade:":
         print("G")
      elif instrs[0] == "A:" or instrs[0] == "Average:":
         print("A")
      elif instrs[0] == "I" or instrs[0] == "Info":
         print("I")
      elif instrs[0] == "Q" or instrs[0] == "Quit":
         exit(0)
      
main()
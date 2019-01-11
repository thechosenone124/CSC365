import reader
gradeNames = ["kindergarten", "1st grade", "2nd grade", "3rd grade", "4th grade", "5th grade", "6th grade"]
studentList = reader.getStudents()

#these take in an array of arguments, if the args are bad they just return
def studentSearch(args):
   if len(args == 1):
      return;
   print("S")

def teacherSearch(args):
   if len(args == 1):
      return
   print("T")

def busSearch(args):
   if len(args == 1):
      return
   print("B")

def gradeSearch(args):
   if len(args == 1):
      return
   print("G")

def average(args):
   if len(args == 1):
      return
   print("A")

def info():
   grades = [0,0,0,0,0,0,0]
   for row in studentList:
      i = int(row[reader.Grade])
      grades[i - 1]+=1
   for x in range(7):
      print(gradeNames[x] + ": " + str(grades[x]))

def main():
   instr = ""
   while True:
      instr = input("S[tudent]: <lastname> [B[us]]\n" + "T[eacher]: <lastname>\n" + 
         "B[us]: <number>\n" + "G[rade]: <number> [H[igh]|L[ow]]\n" + 
         "A[verage]: <number>\n" + "I[nfo]\n" + "Q[uit]\n")

      instrs = instr.split(" ")
      if len(instrs) == 0:
         continue
      if instrs[0] == "Q" or instrs[0] == "Quit":
         exit(0)
      if instrs[0] == "S:" or instrs[0] == "Student:":
         studentSearch(instrs)
      elif instrs[0] == "T:" or instrs[0] == "Teacher:":
         teacherSearch(instrs)
      elif instrs[0] == "B:" or instrs[0] == "Bus:":
         busSearch(instrs)
      elif instrs[0] == "G:" or instrs[0] == "Grade:":
         gradeSearch(instrs)
      elif instrs[0] == "A:" or instrs[0] == "Average:":
         average(instrs)
      elif instrs[0] == "I" or instrs[0] == "Info":
         info()
      
main()
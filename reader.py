import csv

StLastName = 0
StFirstName = 1
Grade = 2
Classroom = 3
Bus = 4
GPA = 5
TLastName = 6
TFirstName = 7

def getStudents():
   try:
      with open('students.txt', 'rb') as csvfile:
         output = list()
         reader = csv.reader(csvfile, delimiter=',')
         for row in reader:
            output.append(row)
         return output
   except:
      exit(1)


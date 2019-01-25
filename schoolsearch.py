import csv
import reader

# Given a student's last name, print the last name, first name, grade, and classroom
# assignment for each student found and the name of their teacher (first and last name)
# 
# Bus option: Given a student's last name, print the last name, first name, and bus route
def student_query(student_name, bus_option, csv_reader):
   for row in csv_reader:
      if row['StLastName'] == student_name:
         if bus_option:
            print(row['StLastName'], row['StFirstName'], row['Bus'])
         else:
            print(row['StLastName'], row['StFirstName'], row['Grade'], row['Classroom'],
               row['TLastName'], row['TFirstName'])

# Given a teacher's last name, print the last and the first name of each student in that
# teacher's class
def teacher_query(teacher_name, csv_reader):
   for row in csv_reader:
      if row['TLastName'] == teacher_name:
         print(row['StLastName'], row['StFirstName'])

# Given a bus route, print the last name and the first name of each student on that route
# and their grade and classroom
def bus_query(bus_route, csv_reader):
   for row in csv_reader:
      if row['Bus'] == bus_route:
         print(row['StLastName'], row['StFirstName'], row['Grade'], row['Classroom'])

# Given a grade, print the last name and first name of each student in that grade
def grade_query(grade, csv_reader):
   for row in csv_reader:
      if row['Grade'] == grade:
         print(row['StLastName'], row['StFirstName'])

# Given a grade, print the student, GPA, teacher, and bus route of the student with the
# highest GPA in that grade
#
# Low option: Given a grade, print the student, GPA, teacher, and bus route of the
# student with the lowest GPA in that grade
def grade_option_query(grade, high_option, csv_reader):
   max_gpa = None
   min_gpa = None
   max_row = None
   min_row = None

   if high_option:
      for row in csv_reader:
         if row['Grade'] == grade:
            if max_gpa is None or row['GPA'] > max_gpa:
               max_gpa = row['GPA']
               max_row = row
      print(max_row['StLastName'], max_row['StFirstName'], max_row['GPA'], 
         max_row['TLastName'], max_row['TFirstName'], max_row['Bus'])
   else:
      for row in csv_reader:
         if row['Grade'] == grade:
            if min_gpa is None or row['GPA'] < min_gpa:
               min_gpa = row['GPA']
               min_row = row
      print(min_row['StLastName'], min_row['StFirstName'], min_row['GPA'],
         min_row['TLastName'], min_row['TFirstName'], min_row['Bus'])

# Given a grade, calculate and print the average GPA score for the students in that grade
def average_query(grade, csv_reader):
   total_gpa = 0
   num_students = 0

   for row in csv_reader:
      if row['Grade'] == grade:
         total_gpa += float(row['GPA'])
         num_students += 1

   print(grade + ":", total_gpa / num_students if num_students > 0 else 0)
   
# For each grade (0 to 6) compute and report the total number of students in that grade   
def info_query(csv_reader):
   info = [0, 0, 0, 0, 0, 0, 0]
   
   for row in csv_reader:
      info[int(row['Grade'])] += 1

   for i in range(len(info)):
      print(str(i) + ":", info[i])

# Given a classroom number, list all students assigned to it
def nr_1(classroom, csv_reader):
   for row in csv_reader:
      if row['Classroom'] == classroom:
         print(row['StLastName'], row['StFirstName'])

# Given a classroom number, find the teach (or teachers) teaching in it
def nr_2(classroom, csv_reader):
   teachers = set()

   for row in csv_reader:
      if row['Classroom'] == classroom:
         teachers.add(row['TLastName'] + ' ' + row['TFirstName'])

   for teacher in teachers:
      print(teacher)

# Given a grade, find all teachers who teach it
def nr_3(grade, csv_reader):
   teachers = set()

   for row in csv_reader:
      if row['Grade'] == grade:
         teachers.add(row['TLastName'] + ' ' + row['TFirstName'])

   for teacher in teachers:
      print(teacher)

# Print a list of classrooms ordered by classroom number, with a total number of students
# in each of the classrooms
def nr_4(csv_reader):
   classes = {}

   for row in csv_reader:
      if row['Classroom'] in classes:
         classes[row['Classroom']] += 1
      else:
         classes[row['Classroom']] = 1

   for key, value in sorted(classes.items(), key=lambda kv: kv[0]):
      print(key, ':', value)
   
def main():
   reader.createCSV()

   try:
      with open('final.txt') as csv_file:
         pass
   except IOError as e:
      print("Unable to open final.txt")
      exit(0)

   csv_file = open("final.txt", "r")
   csv_reader = csv.DictReader(csv_file, fieldnames=['StLastName', 'StFirstName', 
      'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName'])
   instr = ""

   while True:
      instr = input("S[tudent]: <lastname> [B[us]]\n" + "T[eacher]: <lastname>\n" 
         + "B[us]: <number>\n" + "G[rade]: <number> [H[igh]|L[ow]]\n" 
         + "A[verage]: <number>\n" + "I[nfo]\n" + "NR1: <number>\n" + "NR2: <number>\n" 
         + "NR3: <number>\n" + "NR4\n" + "NR5: [A[ll]|B[us]|G[rade]|T[eacher]\n" + "Q[uit]\n")

      instrs = instr.split(" ")

      if instrs[0] == "S:" or instrs[0] == "Student:":
         if len(instrs) == 3 and (instrs[2] == "B" or instrs[2] == "Bus"):
            student_query(instrs[1], True, csv_reader)
         else:
            student_query(instrs[1], False, csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "T:" or instrs[0] == "Teacher:":
         teacher_query(instrs[1], csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "B:" or instrs[0] == "Bus:":
         bus_query(instrs[1], csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "G:" or instrs[0] == "Grade:":
         if len(instrs) == 3:
            if instrs[2] == "H" or instrs[2] == "High":
               grade_option_query(instrs[1], True, csv_reader)
            elif instrs[2] == "L" or instrs[2] == "Low":
               grade_option_query(instrs[1], False, csv_reader)
         else:
            grade_query(instrs[1], csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "A:" or instrs[0] == "Average:":
         average_query(instrs[1], csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "I" or instrs[0] == "Info":
         info_query(csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "NR1:":
         nr_1(instrs[1], csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "NR2:":
         nr_2(instrs[1], csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "NR3:":
         nr_3(instrs[1], csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "NR4":
         nr_4(csv_reader)
         csv_file.seek(0)
      elif instrs[0] == "NR5:":
         reader.gradeTeacherBusCSV(instrs[1])
         print("output to analysis.csv!\n")
      elif instrs[0] == "Q" or instrs[0] == "Quit":
         csv_file.close()
         return;

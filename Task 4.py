class Student:
  def __init__(self, name, rollno):
    # Initialize the attributes
    self.name = name
    self.rollno = rollno
    self.courses = [] # A list of courses that the student is enrolled in
    self.grades = [] # A list of grades that the student has received

  def enroll(self, course):
    # Enroll the student in a course
    self.courses.append(course) # Add the course to the list of courses
    course.addStudent(self) # Add the student to the list of students in the course

  def assignGrade(self, course, score):
    # Assign a grade to the student for a course
    grade = Grade(course, self, score) # Create a new grade object with the course, the student, and the score
    self.grades.append(grade) # Add the grade to the list of grades
    course.addGrade(grade) # Add the grade to the list of grades in the course

  def calculateGPA(self):
    # Calculate the GPA of the student
    total = 0 # Initialize the total score
    count = 0 # Initialize the count of courses
    for grade in self.grades: # Loop through the list of grades
      total += grade.score # Add the score of each grade to the total
      count += 10# Increment the count
    if count == 0: # If the count is zero, return zero
      return 0
    else: # Otherwise, return the average of the total and the count
      return total / count

# Define a class for Course
class Course:
  def __init__(self, code, name, instructor):
    # Initialize the attributes
    self.code = code
    self.name = name
    self.instructor = instructor
    self.students = [] # A list of students who are enrolled in the course
    self.grades = [] # A list of grades that have been assigned for the course

  def addStudent(self, student):
    # Add a student to the course
    self.students.append(student) # Add the student to the list of students

  def addGrade(self, grade):
    # Add a grade to the course
    self.grades.append(grade) # Add the grade to the list of grades

# Define a class for Grade
class Grade:
  def __init__(self, course, student, score):
    # Initialize the attributes
    self.course = course
    self.student = student
    self.score = score

  def getCourse(self):
    # Get the course that the grade is for
    return self.course

  def getStudent(self):
    # Get the student that the grade is for
    return self.student

  def getScore(self):
    # Get the score of the grade
    return self.score

# Create a list to store the objects of Student class
students = []

# Create a list to store the objects of Course class
courses = []

# Create some sample courses
c1 = Course("CS111", "Data Mining", "Laha")
c2 = Course("CS112", "Data Structures and Algorithms", "Marri")
c3 = Course("CS113", "Machine Learning", "Chaitanya")

# Add the courses to the list of courses
courses.append(c1)
courses.append(c2)
courses.append(c3)

# Create some sample students
s1 = Student("Lahari", 1)
s2 = Student("Simran", 2)
s3 = Student("Nag", 3)

# Add the students to the list of students
students.append(s1)
students.append(s2)
students.append(s3)

# Enroll some students in some courses
s1.enroll(c1)
s1.enroll(c2)
s2.enroll(c2)
s2.enroll(c3)
s3.enroll(c1)
s3.enroll(c3)

# Assign some grades to some students for some courses
s1.assignGrade(c1, 87)
s1.assignGrade(c2, 78)
s2.assignGrade(c2, 85)
s2.assignGrade(c3, 95)
s3.assignGrade(c1, 96)
s3.assignGrade(c3, 90)

# Display the details of each student
for student in students:
  print("Name:", student.name)
  print("Roll No:", student.rollno)
  print("Courses:")
  for course in student.courses:
    print(course.code, course.name, course.instructor)
  print("Grades:")
  for grade in student.grades:
    print(grade.course.code, grade.course.name, grade.score)
  print("GPA:", student.calculateGPA())
  print()

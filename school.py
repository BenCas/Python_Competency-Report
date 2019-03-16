class School:
    Faculty =[]

    def addProfessor(self, professor):
        self.Faculty.append(professor)

    def removeProfessor(self, professor):
        self.Faculty.remove(professor)

class Professor:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

class Course:
    def __init__(self, name, id):
        self.name = name
        self.id = id
          
class Class:
    Professor = Professor
    Students =[]
    Subject = Course

    def __init__(self, name, professor):
        self.name = name
        self.professor = professor
    
    def addStudent(self, student):
        self.Students.append(student)

    def removeStudent(self, student):
        self.Students.remove(student)


class Student: 
    def __init__(self, name, year, grade):        
        self.name = name 
        self.year = year
        self.grade = grade


stu1 = Student("james", "sophmore", "A")
prof1= Professor("Jim", "Math", "1234")

print(stu1.name)





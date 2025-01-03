# class variables

class Student:

    class_year = 2025
    num_students = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1

s1 = Student("Spooder", 21)
s2 = Student("Patrick", 11)

print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)
# print(s1.class_year)
print(Student.class_year) # good practice is to access class variables using class name and not an object of the class
print(Student.num_students)
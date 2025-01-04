# class methods

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance / object method
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    
    # class method
    @classmethod
    def get_count(cls):
        return f"{cls.count} students in class"
    
    @classmethod
    def avg_gpa(cls):
        if cls.count == 0:
            return 0
        return f"{cls.total_gpa/cls.count:.2f} = average GPA"

s1 = Student("Jay",3.5)
s2 = Student("SKILLF",3.0)
s3 = Student("BROSKI",3.2)

print(s1.get_info())
print(Student.get_count())
print(Student.avg_gpa())
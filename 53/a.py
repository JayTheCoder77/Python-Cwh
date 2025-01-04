# static methods

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is at position {self.position}"
    
    @staticmethod # no need to create an object to call this method
    def is_valid_position(position):
        valid_positions = ["Manager", "Assistant", "Employee"]
        return position in valid_positions
    
print(Employee.is_valid_position("Manager"))
# no object is created to call this method

employee1 = Employee("Jay" , "Manager")
employee2 = Employee("Patrick" , "Employee")

print(employee2.get_info())

   
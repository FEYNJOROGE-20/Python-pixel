#class Student:
    #name="Erick"
    #age=22
#Object
#Student1=Student()
#print(f"Name of student: {Student1.name} ")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating objects
Student1 = Student("Eric", 22)
Student2 = Student("Cherop", 19)

# Displaying student details
print("Name:", Student1.name)
print("Age:", Student1.age)

print("Name:", Student2.name)
print("Age:", Student2.age)
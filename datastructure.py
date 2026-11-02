# LIST DATA STRUCTURE

students = ["Erick", "Cherop", "Mary", "John"]

# Display all students
print(students)

# Access one student
print(students[0])

# Add a new student
students.append("Rose")

# Remove a student
students.remove("John")

# Change a student name
students[1] = "Peter"

print(students)


# TUPLE DATA STRUCTURE

students = ("Erick", "Cherop", "Mary", "John")

# Display all students
print(students)

# Access an item
print(students[1])

# Count items
print(len(students))



# SET DATA STRUCTURE

students = {"Erick", "Cherop", "Mary", "Erick"}

# Display students
print(students)

# Add a new student
students.add("John")

# Remove a student
students.remove("Mary")

print(students)

# DICTIONARY DATA STRUCTURE

student = {
    "name": "Erick",
    "age": 22,
    "course": "Python",
    "county": "Nairobi"
}

# Access information
print(student["name"])
print(student["age"])

# Add new information
student["gender"] = "Male"

# Change information
student["age"] = 23

# Display all information
print(student)
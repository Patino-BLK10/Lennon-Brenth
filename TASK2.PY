
# Define the Student class
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to introduce the student
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Create three student objects
student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Mechanical Engineering")
student3 = Student("Charlie", 21, "Mathematics")

# Call their introduce() method
student1.introduce()
student2.introduce()
student3.introduce()

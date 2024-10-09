
class Student:
    def __init__(self, name, age, course, student_id):
        self.name = name
        self.age = age
        self.course = course
        self.student_id = student_id

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Course: {self.course}\n"
                f"Student ID: {self.student_id}")

def create_student():
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")

    while not age.isdigit() or int(age) < 0:
        age = input("Please enter a valid age (positive number): ")
    age = int(age)

    course = input("Enter the student's course: ")
    student_id = input("Enter the student's ID number: ")

    return Student(name, age, course, student_id)

def display_students_info(students):
    if not students:
        print("No students registered.")
    else:
        for i, student in enumerate(students, start=1):
            print(f"\nStudent {i}:")
            print(student)

def main():
    students = []

    while True:
        print("\nChoose an option:")
        print("1. Create a new student")
        print("2. Display student information")
        print("3. Exit")

        option = input("Enter the number of the desired option: ")

        if option == "1":
            student = create_student()
            students.append(student)
            print("Student created successfully!")

        elif option == "2":
            display_students_info(students)

        elif option == "3":
            print("Exiting the program...")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()

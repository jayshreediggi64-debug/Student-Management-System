class Student:

    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\nStudent ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Marks      :", self.marks)


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = int(input("Enter Student ID : "))
        name = input("Enter Student Name : ")
        age = int(input("Enter Age : "))
        marks = float(input("Enter Marks : "))

        student = Student(student_id, name, age, marks)
        self.students.append(student)

        print("Student Added Successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No Students Found!")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        student_id = int(input("Enter Student ID to Search : "))

        for student in self.students:
            if student.student_id == student_id:
                print("Student Found!")
                student.display()
                return

        print("Student Not Found!")

    def update_marks(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("Enter New Marks : "))
                student.marks = new_marks
                print("Marks Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_topper(self):
        if len(self.students) == 0:
            print("No Students Available!")
        else:
            topper = self.students[0]

            for student in self.students:
                if student.marks > topper.marks:
                    topper = student

            print("\nTopper Details")
            topper.display()


sms = StudentManagementSystem()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        sms.add_student()

    elif choice == 2:
        sms.view_students()

    elif choice == 3:
        sms.search_student()

    elif choice == 4:
        sms.update_marks()

    elif choice == 5:
        sms.delete_student()

    elif choice == 6:
        sms.display_topper()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
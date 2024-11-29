class Student():
    def __init__(self, name, age,roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

class School:
    def __init__(self):
        self.students =[]
    def add_student(self,name, age,roll_nummber):
        student = Student(name, age, roll_number)
        self.students.append(student)

    def display_student(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll_number: {student.roll_number}")
            print(f"...........................")
    def edit_student(self,roll_number, new_name,new_age):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name =new_name
                student.age = new_age
                print((f"Student {student.name} successfully updated"))
                return

    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully")
                return
        print("Student not found")

school = School()
while True:
    choice = input("Enter your Choice \n 1. Add student\n 2. Display list of  student\n 3.Edit student data\n 4. Delete Student\n 5. quit \n")
    if choice == "1":
        name = input("Enter the name of student: ")
        age = input("Enter Age: ")
        roll_number = input("Enter roll number: ")
        school.add_student(name, age, roll_number)
    elif choice == "2":
        school.display_student()
    elif choice =="3":
        roll_number = input("Enter roll number which you want to edit: ")
        new_name = input("Enter new name for student: ")
        new_age = input("Enter new age for student: ")
        school.edit_student(roll_number,new_name,new_age)
    elif choice =="4":
        roll_number = input("Enter roll number you want to delete:  ")
        school.delete_student(roll_number)
    elif choice=="5":
        break
    else:
          print("Invalid choice. Please enter a number from 1 to 5.")




# class Student:
#     def __init__(self, name, age, roll_number):
#         self.name = name
#         self.age = age
#         self.roll_number = roll_number
#
# class School:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self, name, age, roll_number):
#         student = Student(name, age, roll_number)
#         self.students.append(student)
#
#     def display_students(self):
#         for student in self.students:
#             print(f"Name: {student.name}")
#             print(f"Age: {student.age}")
#             print(f"Roll Number: {student.roll_number}")
#             print(f"...........................")
#
#     def edit_student(self, roll_number, new_name, new_age):
#         for student in self.students:
#             if student.roll_number == roll_number:
#                 student.name = new_name
#                 student.age = new_age
#                 print(f"Student {student.name} successfully updated")
#                 return
#         print("Student not found")
#
#     def delete_student(self, roll_number):
#         for student in self.students:
#             if student.roll_number == roll_number:
#                 self.students.remove(student)
#                 print(f"Student {student.name} deleted successfully")
#                 return
#         print("Student not found")
#
# school = School()
# while True:
#     choice = input("Enter your choice: \n 1. Add student\n 2. Display list of students\n 3. Edit student data\n 4. Delete student\n 5. Quit\n")
#     if choice == "1":
#         name = input("Enter the name of student: ")
#         age = input("Enter age: ")
#         roll_number = input("Enter roll number: ")
#         try:
#             age = int(age)
#             school.add_student(name, age, roll_number)
#         except ValueError:
#             print("Invalid age. Please enter a number.")
#     elif choice == "2":
#         school.display_students()
#     elif choice == "3":
#         roll_number = input("Enter roll number you want to edit: ")
#         new_name = input("Enter new name for student: ")
#         new_age = input("Enter new age for student: ")
#         try:
#             new_age = int(new_age)
#             school.edit_student(roll_number, new_name, new_age)
#         except ValueError:
#             print("Invalid age. Please enter a number.")
#     elif choice == "4":
#         roll_number = input("Enter roll number you want to delete: ")
#         school.delete_student(roll_number)
#     elif choice == "5":
#         break
#     else:
#         print("Invalid choice. Please enter a number from 1 to 5.")

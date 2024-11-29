# Sample student data (list of dictionaries)
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "C"},
    {"name": "David", "age": 19, "grade": "A"},
    {"name": "Emma", "age": 20, "grade": "B"},
]

filtered_student =list(filter(lambda s: s['age']>=18 and s["grade"]=="A",students))
print(filtered_student)

# Function to filter students by name
# def filter_by_name(student_data, name):
#     return [student for student in student_data if student["name"] == name]
#
# # Function to filter students by age
# def filter_by_age(student_data, age):
#     return [student for student in student_data if student["age"] == age]
#
# # Function to filter students by grade
# def filter_by_grade(student_data, grade):
#     return [student for student in student_data if student["grade"] == grade]
#
# # Example usage
# filtered_students_by_name = filter_by_name(students, "Alice")
# filtered_students_by_age = filter_by_age(students, 20)
# filtered_students_by_grade = filter_by_grade(students, "A")
#
# print("Students filtered by name:", filtered_students_by_name)
# print("Students filtered by age:", filtered_students_by_age)
# print("Students filtered by grade:", filtered_students_by_grade)

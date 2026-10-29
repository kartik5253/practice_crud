# In-memory list to store students
students = []

def create_student(student):
    students.append(student)
    return student

def get_all_students():
    return students

def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    return None

def update_student(student_id: int, student_data):
    for student in students:
        if student.id == student_id:
            student.name = student_data.name
            student.email = student_data.email
            student.course = student_data.course
            student.semester = student_data.semester
            return student
    return None

def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return True
    return False
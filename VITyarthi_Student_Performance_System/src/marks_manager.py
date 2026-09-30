from database import execute, fetch_all
from student_manager import find_student

def add_marks(reg_no, subject, marks):
    student = find_student(reg_no)
    if not student:
        raise ValueError("Student not found.")
    marks = float(marks)
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    if not subject.strip():
        raise ValueError("Subject is required.")

    return execute(
        "INSERT INTO marks(student_id,subject,marks) VALUES(?,?,?)",
        (student["student_id"], subject.strip(), marks)
    )

def get_marks(reg_no):
    student = find_student(reg_no)
    if not student:
        raise ValueError("Student not found.")
    return fetch_all(
        "SELECT subject, marks FROM marks WHERE student_id=? ORDER BY subject",
        (student["student_id"],)
    )

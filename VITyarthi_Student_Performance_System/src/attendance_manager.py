from database import execute, fetch_all
from student_manager import find_student

def add_attendance(reg_no, subject, attended, total):
    student = find_student(reg_no)
    if not student:
        raise ValueError("Student not found.")

    attended, total = int(attended), int(total)
    if total <= 0:
        raise ValueError("Total classes must be positive.")
    if attended < 0 or attended > total:
        raise ValueError("Attended classes must be between 0 and total classes.")
    if not subject.strip():
        raise ValueError("Subject is required.")

    return execute(
        "INSERT INTO attendance(student_id,subject,attended,total) VALUES(?,?,?,?)",
        (student["student_id"], subject.strip(), attended, total)
    )

def get_attendance(reg_no):
    student = find_student(reg_no)
    if not student:
        raise ValueError("Student not found.")
    return fetch_all(
        "SELECT subject, attended, total, ROUND(attended * 100.0 / total, 2) AS percentage "
        "FROM attendance WHERE student_id=? ORDER BY subject",
        (student["student_id"],)
    )

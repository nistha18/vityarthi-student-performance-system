from database import initialize_database
from student_manager import add_student
from marks_manager import add_marks
from attendance_manager import add_attendance

def load_demo_data():
    initialize_database()
    students = [
        ("24CSE001", "Aarav Sharma", "CSE", 1),
        ("24CSE002", "Diya Verma", "CSE", 1),
        ("24CSE003", "Riya Singh", "CSE", 1),
    ]
    for student in students:
        try:
            add_student(*student)
        except ValueError:
            pass

    records = {
        "24CSE001": [("Python", 86), ("Maths", 78), ("English", 82)],
        "24CSE002": [("Python", 72), ("Maths", 68), ("English", 76)],
        "24CSE003": [("Python", 55), ("Maths", 61), ("English", 58)],
    }
    for reg, subjects in records.items():
        for subject, marks in subjects:
            try:
                add_marks(reg, subject, marks)
            except Exception:
                pass

    attendance = {
        "24CSE001": [("Python", 19, 20), ("Maths", 18, 20), ("English", 20, 20)],
        "24CSE002": [("Python", 17, 20), ("Maths", 16, 20), ("English", 18, 20)],
        "24CSE003": [("Python", 14, 20), ("Maths", 15, 20), ("English", 16, 20)],
    }
    for reg, subjects in attendance.items():
        for subject, attended, total in subjects:
            try:
                add_attendance(reg, subject, attended, total)
            except Exception:
                pass

    print("Demo data loaded. Run main.py to explore the system.")

if __name__ == "__main__":
    load_demo_data()

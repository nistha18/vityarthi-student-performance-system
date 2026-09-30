from database import fetch_all
from student_manager import find_student

def performance_summary(reg_no):
    student = find_student(reg_no)
    if not student:
        raise ValueError("Student not found.")

    marks = fetch_all(
        "SELECT marks FROM marks WHERE student_id=?", (student["student_id"],)
    )
    attendance = fetch_all(
        "SELECT attended, total FROM attendance WHERE student_id=?",
        (student["student_id"],)
    )

    avg_marks = sum(row["marks"] for row in marks) / len(marks) if marks else 0
    att_pct = (
        sum(row["attended"] for row in attendance) * 100 /
        sum(row["total"] for row in attendance)
        if attendance and sum(row["total"] for row in attendance) else 0
    )

    if avg_marks >= 75 and att_pct >= 75:
        status = "Excellent"
    elif avg_marks >= 60 and att_pct >= 75:
        status = "Good"
    elif avg_marks >= 50:
        status = "Needs Improvement"
    else:
        status = "At Risk"

    return {
        "reg_no": student["reg_no"],
        "name": student["name"],
        "branch": student["branch"],
        "semester": student["semester"],
        "average_marks": round(avg_marks, 2),
        "attendance_percentage": round(att_pct, 2),
        "status": status,
        "subjects_with_marks": len(marks),
        "subjects_with_attendance": len(attendance),
    }

def class_report():
    rows = fetch_all("""
        SELECT s.reg_no, s.name,
               ROUND(AVG(m.marks), 2) AS average_marks
        FROM students s
        LEFT JOIN marks m ON s.student_id = m.student_id
        GROUP BY s.student_id
        ORDER BY average_marks DESC
    """)
    return rows

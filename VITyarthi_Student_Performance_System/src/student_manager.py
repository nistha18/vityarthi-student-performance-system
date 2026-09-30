from database import execute, fetch_all

def add_student(reg_no, name, branch, semester):
    reg_no = reg_no.strip()
    name = name.strip()
    branch = branch.strip()

    if not reg_no or not name or not branch:
        raise ValueError("Registration number, name and branch are required.")
    if int(semester) <= 0:
        raise ValueError("Semester must be positive.")

    try:
        return execute(
            "INSERT INTO students(reg_no,name,branch,semester) VALUES(?,?,?,?)",
            (reg_no, name, branch, int(semester))
        )
    except Exception as exc:
        if "UNIQUE" in str(exc).upper():
            raise ValueError("Registration number already exists.")
        raise

def list_students():
    return fetch_all(
        "SELECT student_id, reg_no, name, branch, semester "
        "FROM students ORDER BY reg_no"
    )

def find_student(reg_no):
    rows = fetch_all("SELECT * FROM students WHERE reg_no=?", (reg_no.strip(),))
    return rows[0] if rows else None

def delete_student(reg_no):
    student = find_student(reg_no)
    if not student:
        raise ValueError("Student not found.")
    execute("DELETE FROM students WHERE reg_no=?", (reg_no.strip(),))

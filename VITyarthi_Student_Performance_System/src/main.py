from database import initialize_database
from student_manager import add_student, list_students, delete_student
from marks_manager import add_marks, get_marks
from attendance_manager import add_attendance, get_attendance
from report_generator import print_student_report, print_class_report

def show_students():
    rows = list_students()
    if not rows:
        print("No students found.")
        return
    print(f"\n{'Reg No':<15}{'Name':<25}{'Branch':<15}{'Sem':>5}")
    print("-" * 60)
    for r in rows:
        print(f"{r['reg_no']:<15}{r['name']:<25}{r['branch']:<15}{r['semester']:>5}")

def student_menu():
    while True:
        print("\n=== STUDENT MANAGEMENT ===")
        print("1. Add student")
        print("2. View students")
        print("3. Delete student")
        print("4. Back")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                reg = input("Registration no: ")
                name = input("Name: ")
                branch = input("Branch: ")
                sem = input("Semester: ")
                add_student(reg, name, branch, sem)
                print("Student added.")
            elif choice == "2":
                show_students()
            elif choice == "3":
                delete_student(input("Registration no: "))
                print("Student deleted.")
            elif choice == "4":
                return
            else:
                print("Invalid choice.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")

def marks_menu():
    while True:
        print("\n=== MARKS MANAGEMENT ===")
        print("1. Add marks")
        print("2. View marks")
        print("3. Back")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                add_marks(input("Registration no: "), input("Subject: "), input("Marks: "))
                print("Marks saved.")
            elif choice == "2":
                rows = get_marks(input("Registration no: "))
                for r in rows:
                    print(f"{r['subject']}: {r['marks']}")
            elif choice == "3":
                return
            else:
                print("Invalid choice.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")

def attendance_menu():
    while True:
        print("\n=== ATTENDANCE MANAGEMENT ===")
        print("1. Add attendance")
        print("2. View attendance")
        print("3. Back")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                add_attendance(
                    input("Registration no: "),
                    input("Subject: "),
                    input("Classes attended: "),
                    input("Total classes: ")
                )
                print("Attendance saved.")
            elif choice == "2":
                rows = get_attendance(input("Registration no: "))
                for r in rows:
                    print(f"{r['subject']}: {r['attended']}/{r['total']} ({r['percentage']}%)")
            elif choice == "3":
                return
            else:
                print("Invalid choice.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")

def main():
    initialize_database()
    while True:
        print("\n" + "=" * 50)
        print(" STUDENT PERFORMANCE & ATTENDANCE SYSTEM")
        print("=" * 50)
        print("1. Student Management")
        print("2. Marks Management")
        print("3. Attendance Management")
        print("4. Student Performance Report")
        print("5. Class Performance Report")
        print("6. Exit")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                student_menu()
            elif choice == "2":
                marks_menu()
            elif choice == "3":
                attendance_menu()
            elif choice == "4":
                print_student_report(input("Registration no: "))
            elif choice == "5":
                print_class_report()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

from analytics import performance_summary, class_report

def print_student_report(reg_no):
    summary = performance_summary(reg_no)
    print("\n--- STUDENT PERFORMANCE REPORT ---")
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

def print_class_report():
    print("\n--- CLASS PERFORMANCE REPORT ---")
    rows = class_report()
    if not rows:
        print("No students available.")
        return
    print(f"{'Reg No':<15}{'Name':<25}{'Average Marks':>15}")
    print("-" * 55)
    for row in rows:
        avg = "N/A" if row["average_marks"] is None else row["average_marks"]
        print(f"{row['reg_no']:<15}{row['name']:<25}{str(avg):>15}")

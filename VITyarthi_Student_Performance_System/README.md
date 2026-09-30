# Student Performance & Attendance Management System

## VITyarthi Build Your Own Project

### 1. Overview
A Python-based academic management system that stores student details, marks and attendance in SQLite and generates individual and class-level performance reports.

### 2. Problem Statement
Students and faculty often need a simple way to maintain academic records and understand performance without manually calculating averages and attendance percentages.

### 3. Objectives
- Manage student records.
- Store and retrieve subject-wise marks.
- Store and retrieve attendance.
- Automatically calculate performance indicators.
- Generate student and class reports.
- Demonstrate modular Python programming, validation and database handling.

### 4. Major Functional Modules
1. Student Management
2. Marks Management
3. Attendance Management
4. Analytics & Reporting

### 5. Technologies
- Python 3
- SQLite
- Python unittest
- Git/GitHub

No external packages are required.

### 6. Folder Structure
```text
VITyarthi_Student_Performance_System/
├── src/
│   ├── main.py
│   ├── database.py
│   ├── student_manager.py
│   ├── marks_manager.py
│   ├── attendance_manager.py
│   ├── analytics.py
│   └── report_generator.py
├── tests/
│   └── test_system.py
├── docs/
│   └── diagrams.md
├── README.md
└── statement.md
```

### 7. How to Run
```bash
cd src
python main.py
```

A SQLite database named `student_performance.db` is created automatically.

### 8. Testing
From the project root:
```bash
python -m unittest discover -s tests -v
```

### 9. Input Validation
- Marks must be 0–100.
- Attendance cannot exceed total classes.
- Semester must be positive.
- Registration number must be unique.
- Required text fields cannot be empty.

### 10. Future Enhancements
- GUI using Tkinter.
- Login and role-based access.
- Export reports to CSV/PDF.
- Charts for marks and attendance.
- Cloud database integration.

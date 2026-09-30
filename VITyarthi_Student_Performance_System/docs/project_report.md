# PROJECT REPORT
## Student Performance & Attendance Management System

### 1. Cover Page
**VITyarthi – Build Your Own Project**

**Project Title:** Student Performance & Attendance Management System  
**Technology:** Python + SQLite  
**Student Name:** ____________________  
**Registration Number:** ____________________  
**Course/Subject:** ____________________  
**Faculty Name:** ____________________  
**Academic Year:** 2026–27  

### 2. Introduction
The Student Performance & Attendance Management System is a modular Python application designed to maintain basic academic records. It stores student details, marks and attendance and provides automatically calculated performance summaries.

### 3. Problem Statement
Manual calculation of academic averages and attendance can be repetitive and error-prone. A small database-backed application can centralize these records and provide consistent calculations.

### 4. Objectives
- Develop a real-world Python application.
- Apply modular programming.
- Use SQLite for persistent storage.
- Implement validation and error handling.
- Generate useful academic reports.
- Demonstrate testing and documentation.

### 5. Functional Requirements
FR1: Add student records.  
FR2: View student records.  
FR3: Delete student records.  
FR4: Add subject-wise marks.  
FR5: View marks.  
FR6: Add subject-wise attendance.  
FR7: View attendance percentages.  
FR8: Generate individual performance reports.  
FR9: Generate class performance reports.

### 6. Non-Functional Requirements
- **Usability:** Menu-driven interface with clear prompts.
- **Reliability:** Validation prevents invalid marks and attendance.
- **Maintainability:** Separate modules for each responsibility.
- **Performance:** SQLite queries are lightweight for a small academic dataset.
- **Error Handling:** User-facing errors are caught and displayed without crashing the main menu.
- **Resource Efficiency:** Uses Python standard library and SQLite; no external package is required.

### 7. System Architecture
The system uses a layered modular structure:
1. User Interface layer – `main.py`
2. Business modules – student, marks and attendance managers
3. Analytics/reporting layer
4. Persistence layer – SQLite

See `docs/diagrams.md` for architecture and workflow diagrams.

### 8. Design Diagrams
The project includes:
- System architecture diagram
- Workflow diagram
- Use case diagram
- Sequence diagram
- Class/component diagram
- ER diagram

### 9. Design Decisions & Rationale
Python was selected because the course focuses on programming concepts and Python provides a clear standard library. SQLite was selected because it provides persistent relational storage without requiring a separate database server. The application is divided into modules so that each component has a focused responsibility.

### 10. Implementation Details
The project contains seven source modules:
- `database.py`
- `student_manager.py`
- `marks_manager.py`
- `attendance_manager.py`
- `analytics.py`
- `report_generator.py`
- `main.py`

The system uses SQL constraints and Python validation to maintain valid data.

### 11. Screenshots / Results
Insert screenshots of:
1. Main menu
2. Student added successfully
3. Marks entry
4. Attendance entry
5. Student performance report
6. Class performance report

### 12. Testing Approach
Unit tests are provided using Python's `unittest` framework. Tests cover:
- Student creation.
- Invalid marks rejection.
- Correct average and attendance calculations.
- Performance status generation.

Command:
`python -m unittest discover -s tests -v`

### 13. Challenges Faced
- Designing related database tables.
- Handling invalid user input.
- Connecting multiple modules cleanly.
- Calculating aggregate performance metrics.
- Maintaining a simple user interface while keeping code modular.

### 14. Learnings & Key Takeaways
- Modular Python design improves maintainability.
- SQLite can provide simple persistent storage.
- Input validation is important in real-world applications.
- SQL relationships help organize related academic records.
- Automated tests can detect errors before demonstration.

### 15. Future Enhancements
- Tkinter graphical interface.
- Login and role-based permissions.
- CSV/PDF report export.
- Graphical dashboards.
- More detailed subject analytics.
- Cloud deployment.

### 16. References
- Python documentation
- SQLite documentation
- VITyarthi project requirements supplied for this project

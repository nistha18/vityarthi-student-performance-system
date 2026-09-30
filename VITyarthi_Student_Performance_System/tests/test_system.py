import sys
from pathlib import Path
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import database
import student_manager
import marks_manager
import attendance_manager
import analytics

class TestStudentPerformanceSystem(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.tmp.close()
        database.DB_PATH = Path(self.tmp.name)
        database.initialize_database()

    def test_add_student(self):
        student_manager.add_student("24ABC001", "Aarav", "CSE", 1)
        self.assertIsNotNone(student_manager.find_student("24ABC001"))

    def test_invalid_marks(self):
        student_manager.add_student("24ABC001", "Aarav", "CSE", 1)
        with self.assertRaises(ValueError):
            marks_manager.add_marks("24ABC001", "Python", 120)

    def test_performance_summary(self):
        student_manager.add_student("24ABC001", "Aarav", "CSE", 1)
        marks_manager.add_marks("24ABC001", "Python", 80)
        attendance_manager.add_attendance("24ABC001", "Python", 18, 20)
        report = analytics.performance_summary("24ABC001")
        self.assertEqual(report["average_marks"], 80.0)
        self.assertEqual(report["attendance_percentage"], 90.0)
        self.assertEqual(report["status"], "Excellent")

if __name__ == "__main__":
    unittest.main()

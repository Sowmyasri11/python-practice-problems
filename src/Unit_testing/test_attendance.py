import unittest
from attendance import calculate_attendance_percentage

class TestAttendance(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_attendance_percentage(5, 10), 50)

    def test_zero_total(self):
        with self.assertRaises(ValueError):
            calculate_attendance_percentage(5, 0)

if __name__ == "__main__":
    unittest.main()

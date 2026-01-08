import unittest
from .employee import Employee
from .exceptions import InvalidEmailError, InvalidPhoneError

class TestEmployeeValidation(unittest.TestCase):

    def test_valid_employee(self):

        emp=Employee(1,"Sowmya","sowmya@gmail.com","7894561238")
        self.assertEqual(emp.name,"Sowmya")

    def test_invalid_employee(self):
        with self.assertRaises(InvalidEmailError):
            Employee(2,"Suji","suji@com","9876543541")

    def test_invalid_phone(self):
        with self.assertRaises(InvalidPhoneError):
            Employee(3,"Anu","anu@gmail.com","12345")


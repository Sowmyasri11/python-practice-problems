from .validator import validate_email, validate_phone


class Employee:
    def __init__(self, emp_id, name, email, phone):
        self.id = emp_id
        self.name = name
        self.email = email
        self.phone = phone

        self.validate_details()

    def validate_details(self):
        validate_email(self.email)
        validate_phone(self.phone)

import re

date = "25-12-2025"
if re.fullmatch(r"\d{2}-\d{2}-\d{4}", date):
    print("Valid Date Format")
else:
    print("Invalid Date Format")

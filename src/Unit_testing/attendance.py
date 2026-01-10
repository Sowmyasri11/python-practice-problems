def calculate_attendance_percentage(present, total):
    if total == 0:
        raise ValueError("Total days cannot be zero")
    return (present / total) * 100

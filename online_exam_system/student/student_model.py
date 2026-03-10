"""
student/student_model.py — Student entity class
"""


class Student:
    def __init__(self, student_id: str, name: str, password: str, email: str):
        self.student_id = student_id
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return f"Student(id={self.student_id}, name={self.name})"

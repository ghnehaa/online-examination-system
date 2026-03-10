"""
exam/exam_model.py — Exam entity class
"""
from typing import List


class Exam:
    def __init__(self, exam_id: str, title: str, subject: str,
                 duration: int, total_marks: int,
                 question_ids: List[str], status: str = "active"):
        self.exam_id = exam_id
        self.title = title
        self.subject = subject
        self.duration = duration
        self.total_marks = total_marks
        self.question_ids = question_ids
        self.status = status

    def __repr__(self):
        return f"Exam(id={self.exam_id}, title={self.title}, status={self.status})"

"""
questions/question_model.py — Question entity class
"""
from typing import List


class Question:
    def __init__(self, question_id: str, subject: str, text: str,
                 options: List[str], correct_answer: str):
        self.question_id = question_id
        self.subject = subject
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def __repr__(self):
        return f"Question(id={self.question_id}, subject={self.subject})"

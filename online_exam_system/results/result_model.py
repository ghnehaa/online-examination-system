"""
results/result_model.py — Result entity class
"""


class Result:
    def __init__(self, result_id: str, student_id: str, student_name: str,
                 exam_id: str, exam_title: str, score: int,
                 total_marks: int, percentage: float, grade: str):
        self.result_id = result_id
        self.student_id = student_id
        self.student_name = student_name
        self.exam_id = exam_id
        self.exam_title = exam_title
        self.score = score
        self.total_marks = total_marks
        self.percentage = percentage
        self.grade = grade

    def __repr__(self):
        return (f"Result(student={self.student_name}, exam={self.exam_title}, "
                f"score={self.score}/{self.total_marks}, grade={self.grade})")

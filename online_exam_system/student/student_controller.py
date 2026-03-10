"""
student/student_controller.py — Student login and exam flow
"""
import time
from utils.display import clear_screen, print_header, print_success, print_error, print_info, divider
from utils.file_handler import read_json, write_json
from student.student_model import Student
from results.result_controller import ResultController


class StudentController:

    def login(self):
        clear_screen()
        print_header("Student Login")

        student_id = input("\n  Student ID : ").strip()
        password   = input("  Password   : ").strip()

        data = read_json("students.json")
        for s in data.get("students", []):
            if s["studentID"] == student_id and s["password"] == password:
                student = Student(s["studentID"], s["name"], s["password"], s["email"])
                print_success(f"Welcome, {student.name}!")
                self._dashboard(student)
                return

        print_error("Invalid credentials.")

    def _dashboard(self, student: Student):
        while True:
            clear_screen()
            print_header(f"Student Portal  [{student.name}]")
            print()
            print("  [1] View Available Exams")
            print("  [2] Attempt Exam")
            print("  [3] View My Results")
            print("  [0] Logout")
            divider()

            choice = input("\n  Choice: ").strip()

            if choice == "1":
                self._view_exams()
            elif choice == "2":
                self._attempt_exam(student)
            elif choice == "3":
                rc = ResultController()
                rc.view_student_results(student.student_id)
            elif choice == "0":
                print_info("Logged out.")
                break
            else:
                print_error("Invalid choice.")
                input("\n  Press Enter to continue...")

    def _view_exams(self):
        clear_screen()
        print_header("Available Exams")
        exams = read_json("exams.json").get("exams", [])
        active = [e for e in exams if e["status"] == "active"]

        if not active:
            print_info("No active exams at the moment.")
        else:
            print()
            for i, e in enumerate(active, 1):
                print(f"  [{i}] {e['title']}")
                print(f"       Subject: {e['subject']}  |  Duration: {e['duration']} min  |  Marks: {e['totalMarks']}")
                divider()

        input("\n  Press Enter to go back...")

    def _attempt_exam(self, student: Student):
        clear_screen()
        print_header("Select Exam to Attempt")
        exams = read_json("exams.json").get("exams", [])
        active = [e for e in exams if e["status"] == "active"]

        if not active:
            print_info("No active exams.")
            input("\n  Press Enter...")
            return

        for i, e in enumerate(active, 1):
            print(f"  [{i}] {e['title']}  ({e['duration']} min)")

        try:
            choice = int(input("\n  Select exam number: ")) - 1
            if choice < 0 or choice >= len(active):
                raise ValueError
        except ValueError:
            print_error("Invalid selection.")
            input("\n  Press Enter...")
            return

        selected_exam = active[choice]
        self._run_exam(student, selected_exam)

    def _run_exam(self, student: Student, exam: dict):
        clear_screen()
        print_header(f"Exam: {exam['title']}")
        print_info(f"Duration: {exam['duration']} minutes  |  Total Marks: {exam['totalMarks']}")
        print_info("Answer each question by entering the option letter (A/B/C/D).")
        input("\n  Press Enter to START the exam...")

        all_questions = read_json("questions.json").get("questions", [])
        exam_questions = [q for q in all_questions if q["questionID"] in exam["questionIDs"]]

        student_answers = {}
        marks_per_q = exam["totalMarks"] // len(exam_questions)

        for idx, q in enumerate(exam_questions, 1):
            clear_screen()
            print(f"\n  Question {idx} of {len(exam_questions)}")
            divider()
            print(f"\n  {q['text']}\n")
            for opt in q["options"]:
                print(f"    {opt}")
            print()

            while True:
                ans = input("  Your Answer (A/B/C/D): ").strip().upper()
                if ans in ["A", "B", "C", "D"]:
                    student_answers[q["questionID"]] = ans
                    break
                print_error("Please enter A, B, C, or D.")

        # Auto evaluate
        score = 0
        for q in exam_questions:
            if student_answers.get(q["questionID"]) == q["correctAnswer"]:
                score += marks_per_q

        percentage = round((score / exam["totalMarks"]) * 100, 2)
        grade = self._get_grade(percentage)

        # Save result
        result_entry = {
            "resultID": f"R{student.student_id}{exam['examID']}",
            "studentID": student.student_id,
            "studentName": student.name,
            "examID": exam["examID"],
            "examTitle": exam["title"],
            "score": score,
            "totalMarks": exam["totalMarks"],
            "percentage": percentage,
            "grade": grade
        }
        results_data = read_json("results.json")
        results_data["results"].append(result_entry)
        write_json("results.json", results_data)

        # Show result
        clear_screen()
        print_header("Exam Completed — Your Result")
        print(f"\n  Exam     : {exam['title']}")
        print(f"  Score    : {score} / {exam['totalMarks']}")
        print(f"  Percent  : {percentage}%")
        print(f"  Grade    : {grade}")
        divider()
        print_success("Result saved successfully!")
        input("\n  Press Enter to continue...")

    @staticmethod
    def _get_grade(percentage: float) -> str:
        if percentage >= 90: return "A+"
        if percentage >= 80: return "A"
        if percentage >= 70: return "B"
        if percentage >= 60: return "C"
        if percentage >= 50: return "D"
        return "F"

"""
results/result_controller.py — View and display results
"""
from utils.display import clear_screen, print_header, print_info, divider
from utils.file_handler import read_json


class ResultController:

    def view_all(self):
        clear_screen()
        print_header("All Student Results")
        results = read_json("results.json").get("results", [])

        if not results:
            print_info("No results recorded yet.")
        else:
            print()
            for r in results:
                print(f"  Student  : {r['studentName']} ({r['studentID']})")
                print(f"  Exam     : {r['examTitle']} ({r['examID']})")
                print(f"  Score    : {r['score']} / {r['totalMarks']}")
                print(f"  Percent  : {r['percentage']}%   Grade: {r['grade']}")
                divider()

        input("\n  Press Enter to go back...")

    def view_student_results(self, student_id: str):
        clear_screen()
        print_header("My Results")
        results = read_json("results.json").get("results", [])
        my_results = [r for r in results if r["studentID"] == student_id]

        if not my_results:
            print_info("You have not attempted any exams yet.")
        else:
            print()
            for r in my_results:
                print(f"  Exam     : {r['examTitle']}")
                print(f"  Score    : {r['score']} / {r['totalMarks']}")
                print(f"  Percent  : {r['percentage']}%   Grade: {r['grade']}")
                divider()

        input("\n  Press Enter to go back...")

"""
questions/question_controller.py — Admin: manage question bank
"""
from utils.display import clear_screen, print_header, print_success, print_error, print_info, divider
from utils.file_handler import read_json, write_json


class QuestionController:

    def menu(self):
        while True:
            clear_screen()
            print_header("Question Bank")
            print()
            print("  [1] View All Questions")
            print("  [2] Add Question")
            print("  [3] Delete Question")
            print("  [0] Back")
            divider()

            choice = input("\n  Choice: ").strip()

            if choice == "1":
                self._view_all()
            elif choice == "2":
                self._add_question()
            elif choice == "3":
                self._delete_question()
            elif choice == "0":
                break
            else:
                print_error("Invalid choice.")
                input("\n  Press Enter...")

    def _view_all(self):
        clear_screen()
        print_header("All Questions")
        questions = read_json("questions.json").get("questions", [])

        if not questions:
            print_info("No questions in the bank.")
        else:
            print()
            for q in questions:
                print(f"  ID: {q['questionID']}  |  Subject: {q['subject']}")
                print(f"  Q : {q['text']}")
                for opt in q["options"]:
                    print(f"       {opt}")
                print(f"  ✓  Correct: {q['correctAnswer']}")
                divider()

        input("\n  Press Enter to go back...")

    def _add_question(self):
        clear_screen()
        print_header("Add New Question")
        print()

        subject = input("  Subject        : ").strip()
        text    = input("  Question Text  : ").strip()

        print("\n  Enter 4 options (e.g.  A) Paris ):")
        options = []
        for letter in ["A", "B", "C", "D"]:
            opt = input(f"    {letter}) ").strip()
            options.append(f"{letter}) {opt}")

        correct = input("\n  Correct Answer (A/B/C/D): ").strip().upper()
        if correct not in ["A", "B", "C", "D"]:
            print_error("Invalid answer. Must be A, B, C, or D.")
            input("\n  Press Enter...")
            return

        data = read_json("questions.json")
        new_id = f"Q{str(len(data['questions']) + 1).zfill(3)}"

        data["questions"].append({
            "questionID": new_id,
            "subject": subject,
            "text": text,
            "options": options,
            "correctAnswer": correct
        })
        write_json("questions.json", data)
        print_success(f"Question added with ID: {new_id}")
        input("\n  Press Enter...")

    def _delete_question(self):
        clear_screen()
        print_header("Delete Question")

        qid = input("\n  Enter Question ID to delete: ").strip()
        data = read_json("questions.json")
        original = len(data["questions"])
        data["questions"] = [q for q in data["questions"] if q["questionID"] != qid]

        if len(data["questions"]) < original:
            write_json("questions.json", data)
            print_success(f"Question {qid} deleted.")
        else:
            print_error("Question ID not found.")

        input("\n  Press Enter...")

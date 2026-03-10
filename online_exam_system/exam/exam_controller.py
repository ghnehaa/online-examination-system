"""
exam/exam_controller.py — Admin: manage exams
"""
from utils.display import clear_screen, print_header, print_success, print_error, print_info, divider
from utils.file_handler import read_json, write_json


class ExamController:

    def menu(self):
        while True:
            clear_screen()
            print_header("Exam Management")
            print()
            print("  [1] View All Exams")
            print("  [2] Create New Exam")
            print("  [3] Toggle Exam Status (active/inactive)")
            print("  [4] Delete Exam")
            print("  [0] Back")
            divider()

            choice = input("\n  Choice: ").strip()

            if choice == "1":
                self._view_all()
            elif choice == "2":
                self._create_exam()
            elif choice == "3":
                self._toggle_status()
            elif choice == "4":
                self._delete_exam()
            elif choice == "0":
                break
            else:
                print_error("Invalid choice.")
                input("\n  Press Enter...")

    def _view_all(self):
        clear_screen()
        print_header("All Exams")
        exams = read_json("exams.json").get("exams", [])

        if not exams:
            print_info("No exams created yet.")
        else:
            print()
            for e in exams:
                status_tag = "[ACTIVE]" if e["status"] == "active" else "[INACTIVE]"
                print(f"  {status_tag}  {e['examID']} — {e['title']}")
                print(f"           Subject: {e['subject']}  |  Duration: {e['duration']} min  |  Marks: {e['totalMarks']}")
                print(f"           Questions: {', '.join(e['questionIDs'])}")
                divider()

        input("\n  Press Enter to go back...")

    def _create_exam(self):
        clear_screen()
        print_header("Create New Exam")
        print()

        title    = input("  Exam Title   : ").strip()
        subject  = input("  Subject      : ").strip()

        try:
            duration = int(input("  Duration (min): ").strip())
            marks    = int(input("  Total Marks  : ").strip())
        except ValueError:
            print_error("Duration and marks must be numbers.")
            input("\n  Press Enter...")
            return

        # Show available questions for the subject
        all_q = read_json("questions.json").get("questions", [])
        subject_q = [q for q in all_q if q["subject"].lower() == subject.lower()]

        if not subject_q:
            print_info(f"No questions found for subject: {subject}")
            input("\n  Press Enter...")
            return

        print(f"\n  Available Questions for '{subject}':")
        for q in subject_q:
            print(f"    [{q['questionID']}] {q['text'][:60]}...")

        raw_ids = input("\n  Enter Question IDs (comma-separated, e.g. Q001,Q002): ").strip()
        question_ids = [qid.strip() for qid in raw_ids.split(",")]

        valid_ids = [q["questionID"] for q in all_q]
        invalid = [qid for qid in question_ids if qid not in valid_ids]
        if invalid:
            print_error(f"Invalid Question IDs: {', '.join(invalid)}")
            input("\n  Press Enter...")
            return

        data = read_json("exams.json")
        new_id = f"EX{str(len(data['exams']) + 1).zfill(3)}"

        data["exams"].append({
            "examID": new_id,
            "title": title,
            "subject": subject,
            "duration": duration,
            "totalMarks": marks,
            "questionIDs": question_ids,
            "status": "active"
        })
        write_json("exams.json", data)
        print_success(f"Exam created with ID: {new_id}")
        input("\n  Press Enter...")

    def _toggle_status(self):
        clear_screen()
        print_header("Toggle Exam Status")

        eid = input("\n  Enter Exam ID: ").strip()
        data = read_json("exams.json")

        for exam in data["exams"]:
            if exam["examID"] == eid:
                exam["status"] = "inactive" if exam["status"] == "active" else "active"
                write_json("exams.json", data)
                print_success(f"Exam {eid} is now '{exam['status']}'.")
                input("\n  Press Enter...")
                return

        print_error("Exam ID not found.")
        input("\n  Press Enter...")

    def _delete_exam(self):
        clear_screen()
        print_header("Delete Exam")

        eid = input("\n  Enter Exam ID to delete: ").strip()
        data = read_json("exams.json")
        original = len(data["exams"])
        data["exams"] = [e for e in data["exams"] if e["examID"] != eid]

        if len(data["exams"]) < original:
            write_json("exams.json", data)
            print_success(f"Exam {eid} deleted.")
        else:
            print_error("Exam ID not found.")

        input("\n  Press Enter...")

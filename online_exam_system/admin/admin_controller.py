"""
admin/admin_controller.py — Admin login and dashboard
"""
from utils.display import clear_screen, print_header, print_success, print_error, print_info, divider
from utils.file_handler import read_json, write_json
from admin.admin_model import Admin
from questions.question_controller import QuestionController
from exam.exam_controller import ExamController
from results.result_controller import ResultController
from student.student_manager import StudentManager


class AdminController:

    def login(self):
        clear_screen()
        print_header("Admin Login")

        admin_id = input("\n  Admin ID   : ").strip()
        password  = input("  Password   : ").strip()

        data = read_json("admins.json")
        for a in data.get("admins", []):
            if a["adminID"] == admin_id and a["password"] == password:
                admin = Admin(a["adminID"], a["name"], a["password"])
                print_success(f"Welcome, {admin.name}!")
                self._dashboard(admin)
                return

        print_error("Invalid credentials.")

    def _dashboard(self, admin: Admin):
        while True:
            clear_screen()
            print_header(f"Admin Dashboard  [{admin.name}]")
            print()
            print("  [1] Manage Students")
            print("  [2] Manage Questions")
            print("  [3] Manage Exams")
            print("  [4] View All Results")
            print("  [0] Logout")
            divider()

            choice = input("\n  Choice: ").strip()

            if choice == "1":
                sm = StudentManager()
                sm.menu()
            elif choice == "2":
                qc = QuestionController()
                qc.menu()
            elif choice == "3":
                ec = ExamController()
                ec.menu()
            elif choice == "4":
                rc = ResultController()
                rc.view_all()
            elif choice == "0":
                print_info("Logged out.")
                break
            else:
                print_error("Invalid choice.")
                input("\n  Press Enter to continue...")

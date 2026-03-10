"""
student/student_manager.py — Admin: manage student accounts
"""
import uuid
from utils.display import clear_screen, print_header, print_success, print_error, print_info, divider
from utils.file_handler import read_json, write_json


class StudentManager:

    def menu(self):
        while True:
            clear_screen()
            print_header("Manage Students")
            print()
            print("  [1] View All Students")
            print("  [2] Add New Student")
            print("  [3] Delete Student")
            print("  [0] Back")
            divider()

            choice = input("\n  Choice: ").strip()

            if choice == "1":
                self._view_all()
            elif choice == "2":
                self._add_student()
            elif choice == "3":
                self._delete_student()
            elif choice == "0":
                break
            else:
                print_error("Invalid choice.")
                input("\n  Press Enter...")

    def _view_all(self):
        clear_screen()
        print_header("All Students")
        students = read_json("students.json").get("students", [])
        if not students:
            print_info("No students registered.")
        else:
            print()
            for s in students:
                print(f"  ID: {s['studentID']}  |  Name: {s['name']}  |  Email: {s['email']}")
                divider()
        input("\n  Press Enter to go back...")

    def _add_student(self):
        clear_screen()
        print_header("Add New Student")
        print()

        name     = input("  Full Name  : ").strip()
        email    = input("  Email      : ").strip()
        password = input("  Password   : ").strip()

        if not name or not email or not password:
            print_error("All fields are required.")
            input("\n  Press Enter...")
            return

        data = read_json("students.json")
        new_id = f"STU{str(len(data['students']) + 1).zfill(3)}"

        data["students"].append({
            "studentID": new_id,
            "name": name,
            "email": email,
            "password": password
        })
        write_json("students.json", data)
        print_success(f"Student added! ID: {new_id}")
        input("\n  Press Enter...")

    def _delete_student(self):
        clear_screen()
        print_header("Delete Student")

        sid = input("\n  Enter Student ID to delete: ").strip()
        data = read_json("students.json")
        original = len(data["students"])
        data["students"] = [s for s in data["students"] if s["studentID"] != sid]

        if len(data["students"]) < original:
            write_json("students.json", data)
            print_success(f"Student {sid} deleted.")
        else:
            print_error("Student ID not found.")

        input("\n  Press Enter...")

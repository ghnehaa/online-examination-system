"""
Online Examination & Evaluation System
Entry point - Run this file to start the application
"""
from utils.display import clear_screen, print_banner
from admin.admin_controller import AdminController
from student.student_controller import StudentController


def main():
    clear_screen()
    print_banner()

    while True:
        print("\n" + "="*50)
        print("         MAIN MENU")
        print("="*50)
        print("  [1] Admin Login")
        print("  [2] Student Login")
        print("  [0] Exit")
        print("="*50)

        choice = input("\n  Enter your choice: ").strip()

        if choice == "1":
            admin = AdminController()
            admin.login()
        elif choice == "2":
            student = StudentController()
            student.login()
        elif choice == "0":
            print("\n  Goodbye!\n")
            break
        else:
            print("\n  [!] Invalid choice. Try again.")


if __name__ == "__main__":
    main()

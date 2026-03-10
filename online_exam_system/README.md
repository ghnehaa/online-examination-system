# Online Examination & Evaluation System
**Version 1.0 | Academic CLI Edition**

A command-line based examination system built in Python as a Software Engineering project.

---

## How to Run

```bash
python main.py
```

> Requires Python 3.7+. No external libraries needed.

---

## Default Login Credentials

| Role    | ID      | Password  |
|---------|---------|-----------|
| Admin   | ADM001  | admin123  |
| Student | STU001  | alice123  |
| Student | STU002  | bob456    |

---

## Project Structure

```
online_exam_system/
│
├── main.py                    # Entry point
│
├── admin/
│   ├── admin_model.py         # Admin class
│   └── admin_controller.py    # Login + dashboard
│
├── student/
│   ├── student_model.py       # Student class
│   ├── student_controller.py  # Login + exam flow
│   └── student_manager.py     # Admin: manage students
│
├── exam/
│   ├── exam_model.py          # Exam class
│   └── exam_controller.py     # Create/manage exams
│
├── questions/
│   ├── question_model.py      # Question class
│   └── question_controller.py # Add/view/delete questions
│
├── results/
│   ├── result_model.py        # Result class
│   └── result_controller.py  # View results
│
├── utils/
│   ├── display.py             # Terminal helpers
│   └── file_handler.py        # JSON read/write
│
└── data/
    ├── admins.json            # Admin accounts
    ├── students.json          # Student accounts
    ├── questions.json         # Question bank
    ├── exams.json             # Exam definitions
    └── results.json           # Stored results
```

---

## Features

### Admin
- Secure login
- Add / view / delete students
- Add / view / delete questions (MCQ)
- Create exams by picking questions
- Toggle exam active/inactive
- View all student results

### Student
- Secure login
- View available exams
- Attempt MCQ exams
- Auto-evaluated score + grade
- View personal results

---

## Data Storage
All data is stored in JSON files inside `/data/`. No database is required.

---

## Grading Scale

| Percentage | Grade |
|-----------|-------|
| 90–100    | A+    |
| 80–89     | A     |
| 70–79     | B     |
| 60–69     | C     |
| 50–59     | D     |
| Below 50  | F     |

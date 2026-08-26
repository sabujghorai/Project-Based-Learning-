students = []
stack = []

def add_student():
    name = input("Student name: ")
    students.append({"name": name, "attendance": []})
    print("Student added.")

def mark_attendance():
    if not students:
        print("No students!")
        return

    for i, s in enumerate(students, 1):
        print(i, s["name"])

    try:
        n = int(input("Student number: ")) - 1
        if n < 0 or n >= len(students):
            print("Invalid number!")
            return

        status = input("P = Present, A = Absent: ").upper()

        if status not in ("P", "A"):
            print("Invalid status!")
            return

        students[n]["attendance"].append(status)
        stack.append((n, status))
        print("Attendance marked.")

    except ValueError:
        print("Enter a valid number!")


def show_attendance():
    for s in students:
        total = len(s["attendance"])
        present = s["attendance"].count("P")
        percentage = (present / total * 100) if total else 0
        print(
            f"{s['name']}: {s['attendance']} | "
            f"{percentage:.1f}%"
        )


def undo():
    if not stack:
        print("Nothing to undo!")
        return

    n, status = stack.pop()
    students[n]["attendance"].pop()
    print(f"Undone: {students[n]['name']} -> {status}")


while True:
    print("\n1.Add Student  2.Mark Attendance  3.Show Attendance")
    print("4.Undo  5.Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        show_attendance()
    elif choice == "4":
        undo()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

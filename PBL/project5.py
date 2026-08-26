student = []
attendance = []

while True:

    print("1. Add Student")
    print("2. View Student")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Search Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Name: ")
        student.append({
            "Name": name
        })
        print("Student added successfully.")

    elif choice == 2:
        print("\nStudents:")
        for i in student:
            print(i["Name"])

    elif choice == 3:
        name = input("Enter Student Name: ")
        Attendence = input("Enter P/A: ").upper()

        if Attendence == "P":
            print("Present")

        elif Attendence == "A":
            print("Absent")
        else:
            print("Wrong Attendence")
        attendance.append({
            "Name": name,
            "Attendance": Attendence
        })
    elif choice == 4:
        print("\nAttendance:")
        for i in attendance:
            print(
                i["Name"],
                "->",
                i["Attendance"]
            )

    elif choice == 5:
        name = input("Enter student name to search: ")
        found = False
        for i in student:
            if i["Name"].lower() == name.lower():
                print("Student Found:", i["Name"])
                found = True
        if found == False:
            print("Student not found.")
    elif choice == 6:
        print("Exit")
        break
    else:
        print("You have entered a wrong choice")
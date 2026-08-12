# Student Record Management System

students = []

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        branch = input("Enter Student Branch: ")

        student = {
            "Name": name,
            "Age": age,
            "Branch": branch
        }

        students.append(student)
        print("\nStudent record added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("\nNo student records found.")
        else:
            print("\n----- Student Records -----")
            for student in students:
                print("Name   :", student["Name"])
                print("Age    :", student["Age"])
                print("Branch :", student["Branch"])
                print("---------------------------")

    elif choice == "3":
        search_name = input("Enter student name to search: ")
        found = False

        for student in students:
            if student["Name"].lower() == search_name.lower():
                print("\nStudent Found")
                print("Name   :", student["Name"])
                print("Age    :", student["Age"])
                print("Branch :", student["Branch"])
                found = True
                break

        if not found:
            print("\nStudent not found.")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")
        found = False

        for student in students:
            if student["Name"].lower() == delete_name.lower():
                students.remove(student)
                print("\nStudent record deleted successfully!")
                found = True
                break

        if not found:
            print("\nStudent not found.")

    elif choice == "5":
        print("\nThank You! Exiting Student Record Management System.")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")
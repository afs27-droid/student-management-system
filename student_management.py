students = []

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student = {"ID": student_id, "Name": name, "Age": age}
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nStudent List:")
        for student in students:
            print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}")

def search_student():
    search_id = input("Enter student ID to search: ")
    found = False
    for student in students:
        if student['ID'] == search_id:
            print(f"Found Student - ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}")
            found = True
            break
    if not found:
        print("Student not found.")

def main_menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

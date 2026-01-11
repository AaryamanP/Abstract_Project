students = [] 
courses = set()

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    info = (roll, name) 
    student = {
        "info": info,
        "course": course,
        "marks": marks
    }

    students.append(student)
    courses.add(course)
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return

    for s in students:
        roll, name = s["info"]
        print("Roll:", roll)
        print("Name:", name)
        print("Course:", s["course"])
        print("Marks:", s["marks"])

        print("-" * 20)

def search_student():
    roll_no = int(input("Enter roll number to search: "))
    found = False

    for s in students:
        roll, name = s["info"]
        if roll == roll_no:
            print("Student Found!")
            print("Name:", name)
            print("Course:", s["course"])
            print("Marks:", s["marks"])
            found = True
            break

    if not found:
        print("Student not found.\n")

def display_courses():
    print("Available Courses:", courses, "\n")

while True:
    print("Student Course Management System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll Number")
    print("4. Display Unique Courses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_courses()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice. Try again.\n")
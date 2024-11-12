'''def main():
    try:
        # Initialize student list
        studentsList = []
        with open("studentsList.txt", "r") as infile:
            line = infile.readline()
            while line:
                studentsList.append(line.rstrip("\n").split(","))
                line = infile.readline()

    except FileNotFoundError:
        print("The 'studentsList.txt' file is not found.")
        print("Starting a new students list!")
        studentsList = []
    
    choice = 0
    while choice != 5:
        print("\n*** Student Manager ***")
        print("1. Add a Student")
        print("2. Get Student information")
        print("3. Display Students")
        print("4. Delete a Student")
        print("5. Quit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            print("Adding a student...")
            name = input("Enter the student's name: ")
            student_id = input("Enter the student's ID: ")
            major = input("Enter the student's major: ")
            gpa = input("Enter the student's GPA: ")

            studentsList.append([name, student_id, major, gpa])

        elif choice == 2:
            print("Looking up a student...")
            keyword = input("Enter the name of the student: ")
            found = False
            for student in studentsList:
                if keyword.lower() in student[0].lower():  # case-insensitive search for student name
                    print(student)
                    found = True
            if not found:
                print("No student found with that name.")

        elif choice == 3:
            print("Displaying all students...")
            if studentsList:
                for i, student in enumerate(studentsList):
                    print(f"{i+1}. Name: {student[0]}, ID: {student[1]}, Major: {student[2]}, GPA: {student[3]}")
            else:
                print("No students in the list.")

        elif choice == 4:
            print("Deleting a student...")
            delete_name = input("Enter the name of the student to delete: ")
            found = False
            for i, student in enumerate(studentsList):
                if delete_name.lower() == student[0].lower():  # case-insensitive comparison
                    del studentsList[i]
                    print(f"Deleted student: {student[0]}")
                    found = True
                    break
            if not found:
                print(f"No student found with the name '{delete_name}'.")

        elif choice == 5:
            print("Quitting Program")

    print("Program Terminated")

    # Saving the students to the external file
    with open("studentsList.txt", "w") as outfile:
        for student in studentsList:
            outfile.write(",".join(student) + "\n")

if __name__ == "__main__":
    main()
'''
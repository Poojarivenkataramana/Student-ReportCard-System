student_grades = []
highest_marks = float("-inf")
lowest_marks = float("inf")
higher_ranker = ""
lower_ranker = ""

menu = """
1. Add Student
2. Show Students
3. Highest Marks
4. Lowest Marks
5. Exit
"""

print("Students Report Card:- ")
print("=" * 40)

while True:
    print(menu)
    admin_choice = input("Choose the option: ").strip()

    if admin_choice == "1":
        student = input("Enter the student name: ").lower().strip()
        marks = input("Enter the student marks: ").strip()
        if marks.isdigit():
            student_details = student, int(marks)
            student_grades.append(student_details)
            print(f"Student '{student}' added successfully!")
        else:
            print("Marks must be numeric!..")
            continue

    elif admin_choice == "2":
        if len(student_grades) > 0:
            print("\n")
            print("=" * 60)
            print(f"{'Student':<8}   {'Marks':<8}   {'Grade':<8}")
            print("=" * 60)
            for student, marks in student_grades:
                if marks > 90:
                    grade = "A+"
                elif 80 <= marks <= 90:
                    grade = "A"
                elif 71 <= marks <= 79:
                    grade = "B+"
                elif 66 <= marks <= 70:
                    grade = "B"
                elif 51 <= marks <= 65:
                    grade = "C"
                elif 35 <= marks <= 50:
                    grade = "D"
                else:
                    grade = "F"
                status = "Fail" if marks < 35 else "Pass"
                print(f"{'Student':<8}: {student} {'|':>5} {'Marks':<8}: {marks} {'|':>2} {'Grade':<8}: {grade} | {status}")
            print("=" * 60)
        else:
            print("No students added yet!..")

    elif admin_choice == "3":
        if len(student_grades) > 0:
            highest_marks = float("-inf")
            higher_ranker = ""
            for student, marks in student_grades:
                if marks > highest_marks:
                    highest_marks = marks
                    higher_ranker = student
            if highest_marks > 90:
                grade = "A+"
            elif 80 <= highest_marks <= 90:
                grade = "A"
            elif 71 <= highest_marks <= 79:
                grade = "B+"
            elif 66 <= highest_marks <= 70:
                grade = "B"
            elif 51 <= highest_marks <= 65:
                grade = "C"
            elif 35 <= highest_marks <= 50:
                grade = "D"
            else:
                grade = "F"
            print("\n")
            print("=" * 40)
            print("🏆 Highest Marks Student")
            print("=" * 40)
            print(f"{'Student':<8}: {higher_ranker}")
            print(f"{'Marks':<8}: {highest_marks}")
            print(f"{'Grade':<8}: {grade}")
            print("=" * 40)
        else:
            print("No students added yet!..")

    elif admin_choice == "4":
        if len(student_grades) > 0:
            lowest_marks = float("inf")
            lower_ranker = ""
            for student, marks in student_grades:
                if marks < lowest_marks:
                    lowest_marks = marks
                    lower_ranker = student
            if lowest_marks > 90:
                grade = "A+"
            elif 80 <= lowest_marks <= 90:
                grade = "A"
            elif 71 <= lowest_marks <= 79:
                grade = "B+"
            elif 66 <= lowest_marks <= 70:
                grade = "B"
            elif 51 <= lowest_marks <= 65:
                grade = "C"
            elif 35 <= lowest_marks <= 50:
                grade = "D"
            else:
                grade = "F"
            print("\n")
            print("=" * 40)
            print("📉 Lowest Marks Student")
            print("=" * 40)
            print(f"{'Student':<8}: {lower_ranker}")
            print(f"{'Marks':<8}: {lowest_marks}")
            print(f"{'Grade':<8}: {grade}")
            print("=" * 40)
        else:
            print("No students added yet!..")

    elif admin_choice == "5" or admin_choice.lower() == "exit":
        print("=" * 40)
        print("Exiting the program... Goodbye!")
        print("=" * 40)
        break

    else:
        print("Invalid option! Please choose between 1-5..")
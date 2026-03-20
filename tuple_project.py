# Student Record management system:-
print("Student Record management system:- ")
menu = """[ MENU ]
1. Add Student
2. Display All Students
3. Search Student
4. Delete Student
5. Find Topper
6. Exit """

student_details = []
while True:
    print("=" * 40)
    print(menu)
    print("=" * 40)
    admin_choice = input("Choose the options: ").strip()
    if admin_choice == "1":
        student_id = input("Enter the Student Id: ").strip()
        if student_id.isdigit():
            student_int_id = int(student_id)
        else:
            print("Student Id Must Contain Digits!..")
            continue
        student_name = input("Enter the Student name: ").strip().lower()

        student_age = input("Enter the Student age: ").strip()
        if student_age.isdigit():
            student_int_age = int(student_age)
        else:
            print("Student Age Must Contain Digits!..")
            continue

        student_marks = input("Enter the Student Marks: ").strip()
        if student_marks.isdigit():
            student_float_marks = float(student_marks)
        else:
            print("Student Marks Must Contain Digits!..")
            continue

        student_info = student_int_id,student_name,student_int_age,student_float_marks
        # Stores student details into the list inside tuples
        student_details.append(student_info)
        print("Student Added Successfully..")

    elif admin_choice == "2":
        print(f"{'No':<5}{'ID':<8}{'Name':<12}{'Age':<6}{'Marks':<8}")
        print("-" * 45)
        if len(student_details) > 0:
            for i, student in enumerate(student_details, start=1):
                student_id, name, age, marks = student
                print(f"{i:<5}{student_id:<8}{name:<12}{age:<6}{marks:<8}")

        else:
            print("No Student Record found!..")
        print('-' * 70)
    elif admin_choice == "3":
        admin_choice3 = input("Chose you want search name/id?: ").strip()
        student_id = None
        student_name = None
        if admin_choice3 == "id":
            student_id = int(input("Enter Student Id: "))
        elif admin_choice3 == "name":
            student_name = input("Enter Student Name: ").strip().lower()
        # initially NO Student found Yet
        found = False
        for student in student_details:
            if admin_choice3 == "id":
                if student[0] == student_id:
                    print("Student Details: ",student)
                    found = True
            elif admin_choice3 == "name":
                if student[1] == student_name:
                    print("Student Details: ",student)
                    found = True
        if not found:
            print("No Student  Record found ..")
                #else:
                   # print("No Student found by that name!..")
    elif admin_choice == "4":

        admin_choice4 = input("Enter Student id to delete: ").strip()
        if admin_choice4.isdigit():
            student_id = int(admin_choice4)
        else:
            print("Invalid")
            continue
        found = False
        for student in student_details:
            if student[0] == student_id:
                found = True
                student_details.remove(student)
                print("Student deleted Successfully....")
                break
        if not found:
            print("No Student found ")

    elif admin_choice == "5":
        if not student_details:
            print("No Student Data Found!..")
        else:
            topper = student_details[0]
            for student in student_details:

                if student[3] > topper[3]:
                    topper = student
            print(f"🏆Topper: {topper[1]} With {topper[3]} Marks")

    elif admin_choice == "6":
        break
    else:
        print("Invalid choice! Please choose 1 to 6 only!")






































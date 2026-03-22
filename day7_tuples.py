# tuple:- tuple is a built-in data structure and  used to store multiple values in a single variable similar to lists but only difference is it is immutable

# Features:-
# ordered
# immutable -> (Cannot modified after its creation )
# allows duplicate values
# faster than lists
# can store different datatypes

# Syntax:- variable_name(value1,value2,value3)

# Creating a Tuple(Methods):-
"""value = (2) # this is not tuple a tuple must contain comma after a value
print(type(value)) # This is int """
"""value = (2,)
print(type(value)) # commas are plays important to create a tuple not parentheses"""


# Example:- creating a tuple in multiple ways
# using parentheses:-

"""numbers = (10,20,30,40,50)
print(numbers)"""

# using without parentheses:-

"""numbers = 10,20,30,40
print(type(numbers))"""

# using tuple key word:-

"""values = ['Ramana',1,1.2,True]
print(tuple(values))"""



# Tuple with different values:-

"""values = (10,"20",1+2j,True)
print(values)"""
# creating tuple using empty brackets:-

"""t = ()
print(type(t))"""


# Tuple Accessing:-

"""numbers = (1,2,3,4,5,6,7,8)
print(numbers[1])
print(numbers[0])
print(numbers[-1])
print(numbers[-3])"""

# Tuple immutability:-
# These doesn't work because tuple is immutability once tuple is created we do not modify(create or remove or updated).

"""numbers[0] =20 
numbers[1] = 10"""


# Reversing tuple:-

"""print(numbers[::-1])"""
"""numbers = 10,20,30,40
print(numbers[::-3])"""


# Tuple slicing:- slicing means extracting some portion of a tuple using indexes in current. it doesnt modify original tuple it created new tuple instead

# using (start: stop: step):-
"""numbers = 10,20,30,40,50,60,70,80,90
print(numbers[0:2]) # if we specify the starting and ending point python includes starting value and it stops before ending value means it doesnt include ending value
print(numbers[0:]) #if we do not specify ending point  python by default goes upto end of a tuple
print(numbers[:11]) # if we do not specify starting point python by default takes first value as starting point
print(numbers[:]) # if we do not specify  the starting and ending python goes starting to ending of a tuple
print(numbers[0: 10: 2])""" # prints every 2nd value of a tuple




# tuple methods:- tuple have only two methods
# 1.count():- count how many times occurrence of a value
"""numbers = 1,2,3,4,5,6
print(numbers.count(1))
print(numbers.count(2))"""
# 2.index():- returns the first appearance of value index

"""numbers = (1,2,3,4,5,2)
print(numbers.index(2))
print(numbers.index(0))""" # it raises an error if value doesnt in the tuple


"""values = ("Ramanalikivenkat")
print(values.index("liki"))"""


# nested tuple: a tuple inside tuples

"""numbers = (
    (1,2),(1,3), #0(1,2), 1(1,3), #(2,2), #(3,4)
    (2,2),(3,4)
)
print(numbers)
print(numbers[1:][::-2])""" # it prints (3,4),(1,3) and skips(2,2)


# Tuple Packing:-  means storing multiple values in a tuple
"""data = "Ramana","harish","Hemanth","prasanth","Ravi teja"
name1, name2, name3, name4,name5 = data
print((name1,name2))"""




# Scenario 1 — Storing a Student Record
# A school system stores one student's
# complete information in a single tuple.
#
# Console Output:
# ───────────────────────────────────────
# Student Record: ('Venkataramana', 21, 'ECE', 7.2)
# Name   : Venkataramana
# Age    : 21
# Branch : ECE
# CGPA   : 7.2
# ───────────────────────────────────────


"""print("Student Information")
print('-'*40)
student_details = ("venkataramana", 21, "ECE", 7.2)
name,age,branch,cgpa = student_details
print(f"{'Name':<10}: {name}")
print(f"{'Age':<10}: {age}")
print(f"{'Branch':<10}: {branch}")
print(f"{'CGPA':<10}: {cgpa}")
print('-'*40)
"""



# Tuple Concatenation:- combines the multiple tuples into one.
# Example:-

"""t1 = (1,2,3)
t2 = 1,2,3,1,2,3
t3 = t1 + t2
print(t3)
print(type(t2))"""


# Extended tuple unpacking:-

"""values = 10,20,30,40
first,second,*remaining = values
print(values)
remaining[0] = 10
print(remaining)"""


# Tuple can be a dictionary keys:-
"""location = {
    "Ramana": (1,2),
    "Venkata": (3,4)

}

print(location["Ramana"])
"""


# 🔹 1️⃣ Student Record System
# 👉 Imagine each student has:
#
# ID
# Name
# Marks
# Instead of a dictionary, you store:
# 👉 (101, "Ravi", 85)
#
# Now think:
#
# Position 0 → ID
#
# Position 1 → Name
#
# Position 2 → Marks
#
# 📌 Tuple is acting like a fixed structure (like a row in a table)

"""student_record_system = (101,"Ravi",85)
Id,Name,Marks = student_record_system
print("Student Record System:-")
print('-' * 40)
print(f"{'Student ID':<15}: {Id}")
print(f"{'Student Name':<15}: {Name}")
print(f"{'Student Marks':<15}: {Marks}")

print('-' * 40)
"""
#Tuple contain mutable objects that can be changed:-
"""data = (["Ramana",22,7.2],10)
data[0][0] = "Venkat"
print(data[1])"""

#Tuple swapping:-
# Behind the scene python creates a temporary tuple

"""a,b = 10,20
a,b = b,a
print(a,b)"""

# Student Roll number formatting:- left align with right side zeros
"""print("Student roll numbers:-")
print('-' * 40)
print(f"Student1: {'001':0<8}")
print(f"Student2: {'002':0<8}")
print(f"Student3: {'003':0<8}")
print(f"Student4: {'004':0<8}")
print(f"Student5: {'005':0<8}")
print(f"Student6: {'006':0<8}")
print(f"Student7: {'007':0<8}")
print(f"Student8: {'008':0<8}")

print('-' * 40)
"""




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
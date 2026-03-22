# Lists :- A list is a collection of multiple values stored in a single variable
# Lists are Order
# Mutable
# Allows duplicates
# Can store different datatypes


# Syntax :-
# list_name or variable name = [value1,value2,value3]
# Basic Code
"""my_details = ['Ramana', 21, 'Male' ,'4D0',7.2,True]
print(type(my_details))
print(len(my_details))"""

# Accessing Elements :-
"""values = [10,20,30,40,50,60,70]
print(values[0])
print(values[6])"""
# From negative indexes:
"""print(values[-1])
print(values[-2])
print(values[-7])"""
# Printing all items
"""print(values[0:7])
# or
print(values[0:])
# or
print(values[:])
# or
print(values[::])
# or
print(values[::1])"""


# Slicing:-
"""print(values[0:2])
print(values[:3])
print(values[:-1])"""
# For reversing list:-

"""print(values[::-1])
# or
print(values[-1:-8:-1])"""

# Changing items in a list:-
"""values[0] = "one"
print(values)"""

# Adding items in a list:-
# 1. append() :- adds one item at the end
# -----------
"""values.append(2)
print(values)
values.append([2,3]) # it makes inner list inside list
print(values)
values.append([1])
print(values)"""

# insert :- it adds the item at specific index position
# ----------
"""values.insert(1,21)
print(values)
values.insert(0,1)
print(values)"""


# Extend :- it adds multiple elements
# ----------
"""values.extend(["Ravi teja",21,22])
print(values)
values.extend([1,2,3,4,5])
print(values)"""

# Removing elements:-
# .remove() :- removes by value; if item not found output will be value error item not in list.
# .pop() :- removes by index
# .clear():- delete all values return empty lists


"""values.remove('one')
print(values)
"""
"""values.remove(0)    # Error because item not in list
print(values)"""


# pop():- removes by index and return it if we give specific position it will pop that item otherwise removes by default  last item in the list
"""print(values.pop())""" # it returns the popped value


# Clear():- removes all list items returns empty list
"""values.clear()
print(values)"""

# List Functions:-
# min(),max(),sum()
"""numbers = [10,20,30,40,40,50,60]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
"""
# Sorting:-
# sort() :- is a List method that modifies the original list and returns None
"""num = [5,6,3,4,9,7,1]
print(num)
num.reverse()
print(num)
num.sort()
print(num)
num.sort(reverse = True)
print(num)
"""




# Sorted():- it is a python built in function and creates a new list and safes original list it works on any iterable :-
"""numbers = ['One',"two",'three','four','five']
print(sorted(numbers,key = len , reverse = True))
print(numbers)"""





# looping through list:-
"""numbers = [20,10,10,30,40,50,60]
for i in numbers:
    print(i,end = " ")
print()
"""
# using indexing:-
"""for i in range(len(numbers)):
    print(numbers[i],end = " ")
print()

print(10 and 20 in numbers)"""


# 2D lists:-

"""matrix = [
    [1, 2, 3],
    [4, 5 ,6]
]
print(matrix)"""


# 1️⃣ Student Marks
#
# A teacher stores marks of 10 students in a list and wants to create another list containing only marks greater than 50.



"""student_marks = [55,45,30,35,77,72,65,70,89,90]
higher_marks = []
lower_marks = []
for marks in student_marks:
    if marks > 50:
        higher_marks.append(marks)
    else:
        lower_marks.append(marks)
print("Number Of Higher Score Students Is: ",len(higher_marks))
print("Their Marks: ",higher_marks)
print("Number Of Low Score Students Is: ",len(lower_marks))
print("Their Marks: ",lower_marks)"""
# list comprehension method:-

"""student_marks = [55,45,30,35,77,72,65,70,89,90]
higher_marks = [mark
                for mark in student_marks
                if mark > 50 ]
print(f"The {len(higher_marks)} Students got above 50 marks \nand their marks:{higher_marks}")"""

# 2️⃣ Even Numbers
#
# You have a list of numbers from a class attendance sheet and want a new list containing only even roll numbers.
"""attendance = list(map(int,input("Enter the list of roll numbers:").split()))
even_roll_numbers = []
for roll_number in attendance:
    if roll_number % 2 == 0:
        even_roll_numbers.append(roll_number)
print("The even roll numbers are ",even_roll_numbers)"""



"""attendance = list(map(int,input("Enter the list of roll numbers:").split()))
even_roll_numbers = [roll_number for roll_number in attendance if roll_number % 2 == 0 and roll_number != 0]
print(even_roll_numbers)"""







"""name = "Ramana"
if name == "Tony" or "Stark": # this is not correct way we can write name == "Tony" or name == "stark"
    print("Iron man")
else:
    print("Noman")"""




# 3️⃣ Square Numbers
#
# You have a list of numbers and want a new list where each number becomes its square.
#
# Example idea:
#
# 2 → 4
# 3 → 9
# 4 → 16


"""numbers = list(map(int,input("Enter the numbers: ").split()))
squares =[]
for item in numbers:
    squares.append(item ** 2)
print(numbers)
print(squares)"""


"""
numbers = list(map(int,input("Enter the numbers: ").split()))
squares = [item ** 2 for item in numbers ]
print(squares)"""

# 4️⃣ Names in Uppercase
#
# A list contains student names and you want another list where all names are converted to uppercase.
"""names = list(input("Enter the names: ").split())
upper_case = []
for item in names:
    upper_case.append(item.upper())
print(upper_case)

names = list(input("Enter the names: ").split())
upper_case = [item.upper() for item in names]
print(upper_case)"""


# 5️⃣ Remove Negative Numbers
#
# A list contains positive and negative temperatures.
# Create a new list that keeps only positive temperatures.

"""temperature = list(map(int,input("Enter the temperatures: ").split()))
positive_temperatures = []
negative_temperatures = []
for i in range(len(temperature)):
    if temperature[i] < 0 :
        negative_temp.append(temperature[i])
    else:
        positive_temperatures.append(temperature[i])
print("Positive Temperatures are: ",positive_temperatures)
print("Negative Temperatures are: ",negative_temp)"""


"""temperature = list(map(int,input("Enter the temperatures: ").split()))
positive_temperatures = []
for i in temperature:
    if i > 0:
        positive_temperatures.append(i)

print("Positive Temperatures are: ",positive_temperatures)"""




# 🔹 1️⃣ Student Marks
#
# You want to store marks of 5 subjects.
#
# 👉 Use a list because:
#
# Order matters
#
# You may update marks later
#
# You may calculate total / average
#
# Example scenario:
#
# Math, English, Physics, Chemistry, Biology marks
# explain whai i do tell me no code
"""student_name = input("Enter the student name: ")
Total_subjects = int(input("Enter the total subjects: "))
student_marks = list(map(int,input("Enter the marks: ").split()))

total_marks = 0
average_marks = 0

for marks in student_marks:
    total_marks += marks

average_marks = total_marks / len(student_marks)
print("     Student Marks Card     ")
print("-" * 40)
print("Student Name: ",student_name)
print("Total Marks: ",total_marks)
print("Average Marks: ",average_marks)
print("Highest Marks:",max(student_marks))
print("lowest marks: ",min(student_marks))"""


# 🔹 2️⃣ Shopping Cart Items
#
# In an e-commerce app:
#
# 👉 Store items added to cart in a list.
#
# Because:
#
# Items can be added
#
# Items can be removed
#
# Order matters


# enumerate():- is a built in function that allows you to loop through a list and get the both index and value at the same time
# syntax:- enumerate(iterable)
# loop syntax:-

# for index , value in enumerate(iterable):-

"""names = input("Enter the names: ").lower().split()
for i , values in enumerate(names,start = 1):
    print(i,values)"""



# normal way for indexing and values printing:-

"""names = input("Enter the names: ").lower().split()
for i in range(len(names)):
    print(f"Index{i}: Value {names[i]}")
else:
    print("Done!")"""


"""values = [10,20,30,40]
for i, items in enumerate(values):
    print(f"index{i}: values {items}")
"""

"""names = ["Ramana","likitha","sai"]
for index, value in enumerate(names, start = 1):
    print(f"Student{index}: {value}")"""


# how enumerate internally works:-

"""names = ["Ramana","likitha","sai"]
print(list(enumerate(names)))"""


# 1️⃣ Showing Numbered Menu Items
#
# Scenario
# You are building a small program that shows a menu:
#
# Pizza
# Burger
# Sandwich
# Pasta
#
# Instead of manually numbering them, enumerate() automatically gives:
# 1 → Pizza
# 2 → Burger
# 3 → Sandwich
# 4 → Pasta


"""items = input("Enter the names: ").lower().split()
for index, values in enumerate(items, start = 1):
    print(f"{index} -> {values}")"""

# 2️⃣ Showing Student Rank List
#
# Scenario
#
# You have a list of student names:
#
# Rahul
#
# Priya
#
# Kiran
#
# Ananya
#
# You want to print:
#
# Rank 1 → Rahul
#
# Rank 2 → Priya
#
# Rank 3 → Kiran
#
# Rank 4 → Ananya

"""names = input("Enter the names:").lower().split()
for index,items in enumerate(names,start = 1):
    print(f"Rank{index} -> {items}")"""

# 3️⃣ Tracking Errors in Data
#
# Scenario
#
# You are checking a list of temperatures:
#
# 32
#
# -5
#
# 28
#
# -3
#
# If a temperature is invalid (negative), you want to say:
#
# Error at index 1
#
# Error at index 3

"""temperatures = list(map(int,input("Enter the temperatures: ").split()))
for i,value in enumerate(temperatures):
    if value >= 0:
        print(f"{value}")
    else:
        print(f"Error at the index {i}")"""


# 4️⃣ Displaying Question Numbers in Quiz Apps
#
# Scenario
#
# You have a list of quiz questions.
#
# You want to display:
#
# Question 1: What is Python?
#
# Question 2: What is SQL?
#
# Question 3: What is a list?

"""questions = input("Enter the questions: ").split(",")
for index,item in enumerate(questions,start = 1):
    print(f"Question {index}: {item}")"""


# Find sum of all elements

"""numbers = list(map(int,input("Enter the numbers: ").split()))
sum_numbers = 0

for num in numbers:
    sum_numbers += num
print("The sum is: ",sum_numbers)"""

# Find maximum and minimum
"""numbers = list(map(int,input("Enter the numbers:").split()))
maximum = numbers[0]
minimum = numbers[0]
for num in numbers[1:]:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum number is:",maximum)
print("Minimum number is:",minimum)"""


# finding largest element in the list:
"""numbers = list(map(int,input("Enter the numbers: ").split()))
largest = numbers[0]
for num in numbers[1:]:
    if num > largest:
        largest = num
print("The largest element is:",largest)"""


"""numbers = list(map(int,input("Enter the numbers: ").split()))
largest = float('-inf')
second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("The first largest is:",largest)
print("The second_largest is:",second_largest)"""

"""numbers = list(map(int,input("Enter the numbers: ").split()))
smallest = float('inf')
for num in numbers:
    if num < smallest:
        smallest = num
print("The smallest number is:",smallest)"""
# Remove duplicates from list
"""original = [1,2,1,2,3,4,3,4,5,6,7,8,7,6]
number_list = []
for num in original:
    if num not in number_list:
        number_list.append(num)
print(number_list)"""

# Find common elements between two lists
"""l1 = [1,2,3,4,6,7,8]
l2 = [7,6,5,2,3,9]
for num in l1:
    if num in l2:
        print(num,end = " ")"""

# 1️⃣ Comparing Elements Between Two Lists
#
# Scenario:
#
# You have two lists of numbers.
#
# List A → 1, 2, 3
# List B → 3, 4, 5
"""l1 = list(map(int,input("Enter the numbers: ").split()))
l2 = list(map(int,input("Enter the numbers: ").split()))
common_elements = []
for num1 in l1:
    for num2 in l2:
        if num1 == num2:
            if num1 not in common_elements:
                common_elements.append(num1)

print(common_elements)
"""

# 2️⃣ Multiplication Table
#
# Scenario:
#
# You want to print multiplication tables like:
#
# 1 × 1
# 1 × 2
# 1 × 3
# ...
# 2 × 1
# 2 × 2
# 2 × 3
"""table = int(input("Enter the table number: "))
for i in range(1,table + 1):
    for j in range(1,4):
        print(f"{i} * {j} = {i * j}")
    print()
"""
# 3️⃣ Matrix / Grid Traversal
#
# Scenario:
#
# You have a grid or matrix.
#
# Example:
#
# 1 2 3
# 4 5 6
# 7 8 9


"""n = int(input("Enter the number of rows: "))
number = 1
for rows in range(1,n+1):
    for columns in range(1,n+1):
        print(number,end = " ")
        number += 1

    print()"""

# 5️⃣ Pair Combinations
#
# Scenario:
#
# You want to create all possible pairs of numbers.
#
# Example list:
#
# [1,2,3]
#
# Pairs:
#
# 1,1
# 1,2
# 1,3
# 2,1
# 2,2
# 2,3
# 3,1
# 3,2
# 3,3

"""numbers = [5,7,9]
for i in numbers:
    for j in numbers:
        print(i,j)"""

# Create list of squares

"""numbers = list(map(int,input("Enter the numbers:").split()))
squares = [num ** 2 for num in numbers]
print(squares)"""


# Count vowels in a sentence:

"""text = input("Enter the sentence: ").strip()
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O','u', 'U']
count = 0
for char in text:
    if char in vowels:
        print(char,end = " ")
        count += 1

print("\nThe Vowel Count is:",count)"""


# Find longest word in a list:-

"""sentence = input("Enter the text: ").lower().split()
longest = sentence[0]
for i in range(len(sentence)):
    if len(sentence[i]) > len(longest):
        longest = sentence[i]
print("The longest Word is:",longest)"""

# Reverse each word in a sentence

"""sentence = input("Enter the text:").split()
reverse =""
for word in sentence:
    for j in range(len(word)-1,-1,-1):
        reverse += word[j]
    reverse += " "

print(reverse.strip())"""


# 5️⃣ Count Frequency of Each Character in a Sentence

"""sentence = input("Enter the text:").replace(" ","")
processed = []
for char in sentence:
    if char not in processed:
        freq = sentence.count(char)
        print(f"{char}:{freq}")
        processed.append(char)
"""

















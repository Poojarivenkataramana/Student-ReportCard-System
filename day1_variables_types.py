"""# local_variables
def local_variable():
    x = 10
    y = 20
    print("The sum is:", x + y)


local_variable()"""

# global_variable
"""x = "Ramana"


def global_variable():
    print(x)


global_variable()
print(x)"""

"""x = "Ramana"
def global_variable():
    global x
    x = "Venkata"
    print(" Inside My name is:",x)
global_variable()
print("Outside My name is:",x)"""

#nonlocal variable():- without using the keyword nonlocal variable
"""def outer_function():
    x = 10
    def inner_function():
        x = 20
        print("The inner x is:",x)
    inner_function()
    print("The Outer x is:",x)
outer_function()"""


"""def outer_function(): # using keyword nonlocal variable
    x = 10
    def inner_function():
        nonlocal x
        x = 20
        print("The inner x is:",x)
    inner_function()
    print("The Outer x is:",x)
outer_function()"""


#data types:- text,numeric,sequence,set,mapping,boolean
# Type conversions:- is referring to changing the datatype of a variable / value
#implicit conversion:- pyhon automatically converts when its needed
"""a = 5
b = 2.5
c = a + b
print(c)
print(type(c))
"""

"""a = 20
b = 10
c = a / b
print(c)
c = a // b # integer division
print(c)"""


# Explict conversion:-manually converted from one data type to another
"""a = 3.5
b = 1.5
f = int("10")
print(type(f))
c = str(a)
print(type(c))
print(type(a))
d = bool(0)
e = bool(1)
print(d)
print(e)"""

# comparison operators:- with strings
"""a = "car"
b = "banana"
print(a>b) # True because of it compares the ascii values each characters have its own ascii values c ascii value is 99 b ascii value is 98
print(a<b) # False because 99 not less than 98
# Note :- it compares only first characters
"""

# logical operator:-
"""x = 10
print(not (x > 5))   # False   (because x > 5 is True)
print(not (x < 5)) """

# identity operators:-is , is not
"""a = 10
b = a
print(a is b) # True because both are in same memory
print(a is not b) # True when the values are in different memory
"""
# Ex2:- same values but different memory
"""a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(a == b) # True because same values
print(a is b)""" # False because of different memory

# Note:-
# == -> compares values
# is -> compares memory address

# EX3:- python uses interning
"""a = 'hello'
b = 'hello'
print(a is b)""" # True because if small strings are repeated  python stores only one copy


"""a = "hello, world Python"
b = "hello, world Python"
print(a is b) """# sometimes False because large strings may not interned

"""a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(a == b) # True because same values
print(a is b) # False because different memories

print(id(a)) # it show the memory address
print(id(b))"""




# 1. Check if "apple" is in the list
# ["apple", "banana", "cherry"]
"""fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)"""
"""m = (1, 2)
n = m
print(m is n)
print(id(m))
print(id(n))"""




# interning in identity operators:-
"""a = 10
b = a
print(a is b)
print(a is not b)"""

# Ex same values but different memory
"""x = [1,2,3,4,5]
y = [1,2,3,4,5]
print(id(x))
print(id(y))
print(x is y)
print(x is not y)
print(x == y)"""


"""a = 2572
b = 2572
print(id(a))
print(id(b))
print(a is b)
"""

"""

a = "hello world is not interning"
b = "hello world is not interning"
print(a is b)"""

# formatting strings:- used to insert values inside a string it looks clean
"""Boy = "Ramana"
Girl = "LSG"
print(f"{Girl} Secrectly observes {Boy} Loves me.")"""

# percentage Formatting:-
"""name = "Ramana"
age = 21
salary = 7200000
print("My name is %s and my age is %d year old and my salary is %f. "%(name,age,salary))"""


# .format() method:- Without positions
"""name = "Ramana"
age = 22
print("my name is {} and iam {} old".format(name,age))"""


# With positions:-
"""
name = "Ramana"
age = 22
print("my name is {0} and iam {1} old".format(name,age))"""

"""# formatting numbers:-
pi_value = 3.1459
print("Value is: {:.2f}".format(pi_value))
#               (or)
print("Value is: {:.2f}".format( 3.1459))
#               (0r)
print(f"The rounded value is:{pi_value:.2f}")



#padding:-adding characters(usually spaces or Zeros) Right side or Left side of a String
# Left Padding:-
print(f"{'Hi':>10}")
print(f"{'Hi':<10}")#Right Padding
print(f"{'Hi':^20}")#center padding

# Zeros Padding:-
print(f"{5:05}") # width is 5 but four zeros only prints because already 5 present."""


# 🔵 1. Formatting (f-strings, placeholders) – Scenarios
# Scenario 1

# You are creating an invoice message where you must insert:

# customer name
# product name
# final amount
# You want to generate a message using formatting.
"""customer_name = "Ramana"
Product_name = "Samsung galaxy"
final_amount = 77000
print(f"The customer name is: {customer_name}\nProduct name is:{Product_name}\nFinal price is:{final_amount}")"""

# Scenario 2
# You are writing a student report where you need to place:
# student name
# roll number
# subject
# marks
# All inside one sentence using formatting.

"""student_name = "Venkataramana"
Roll_number = "22G01A04D0"
Subject = "NPTL"
Marks = 70
print(f"Student Name: {student_name}\nRollNumber: {Roll_number}\nSubject: {Subject}\nMarks: {Marks}")"""

# Scenario 3
# You are sending a welcome message for a new user:
# username
# the app name
# You must build the message using formatted placeholders.

"""user_name = "Venkataramana"
app_name = "Netflix"
print("Welcome {}!\nThank you for joining {}.".format(user_name,app_name))"""


# 🔵 2. Padding Scenarios (left, right, center spacing)
# Scenario 4

# You are printing a list of product names in aligned columns, so each name must occupy 15 characters, with extra spaces added automatically.
"""Product_name1 = "Laptop"
Product_name2 = "Mobile"
Product_name3 = "apple airpods"
print(f"1.{Product_name1:<15}|\n2.{Product_name2:<15}|\n3.{Product_name3:<15}|")"""

# Scenario 5
# You want to display a scoreboard where all scores must be right-aligned in a 5-character width.
"""
Score1 = 5
Score2 = 20
Score3 = 299
print(f"1.Score:{Score1:>5}\n2.Score:{Score2:>5}\n3.Score3{Score3:>5}")"""


# Scenario 6
# You’re generating an ID card where the employee name must be centered inside a fixed-width box.
"""Emp_Id = "Ramana"
print(f"|{Emp_Id:^20}|")"""

# 🔵 3. Percentage Formatting Scenarios
# Scenario 7

# You’re building a result sheet where you calculate:

# pass percentage

# attendance percentage

# And display it with a % sign.

"""Total_students = int(input("Enter Total no.of students: "))
passed_students = int(input("Enter the how many students are passed: "))

Total_Days = int(input("Enter the no.of days: "))
present_days = int(input("Enter the how many days present: "))
Pass_percentage = passed_students /Total_students  * 100
Attendance =  present_days/Total_Days  * 100
print(f"pass Percentage:{Pass_percentage:.2f}%\nAttendance percentage is:{Attendance:.2f}%".format(Pass_percentage,Attendance))"""
"""print("The pass Percentage is:%.2f%%"%Pass_percentage)
print("Total attendance Percentage is: %.2f%%"%Attendance)"""


# Scenario 8

# A discount calculator app must display:
# original price
# discount percentage
# final discounted price
# Percentage formatting is needed for the discount

"""original_price = int(input("Enter the Original Price: "))
discount_percentage = int(input("Enter the discount percentage: "))

discount_amount = (original_price * discount_percentage) / 100
final_price = original_price - discount_amount

print("Discount is : %.2f" % discount_amount)
print("Final price is: %.2f rs" % final_price)"""

# You want to show CPU usage: “CPU Load: 78%” The percentage value must be formatted properly. give me output not code
"""CPU_Load = 78
print("The CPU Load is:%d%"%CPU_Load)"""


# 🔵 4. Number Formatting (decimal places, commas) Scenarios
# Scenario 10

# You are showing a price like 2500.5 but you need to format it into:

# 2 decimal places
# (example: 2500.50)

"""price = int(input("Enter the price: "))
print(f"The Price is: {price:.2f}₹")
#               (or)
print("The price is: {:.2f}₹".format(price))"""

# Scenario 11

# You want to display large numbers with commas for readability
# example: 1000000 → 1,000,000
"""price = int(input("Enter the price: "))
print("The Price is: ₹{:,.2f}".format(price))
#              (or)
print(f"The Price is:₹{price:,.2f}")"""


# Scenario 12
# You are calculating the average of marks and want to show the result with exactly 3 decimal places.
"""WSN = 79
CMC = 71
DDTV = 77
OS = 81
Ml = 85
Total_marks = WSN + CMC + DDTV + OS + Ml
Average = Total_marks / 5
print("The Total Marks is: {:.2f} ".format(Total_marks))
print(f"The Average Marks is: {Average:.3f}")"""



# 🔵 5. Combined Scenarios (formatting + padding + numbers)
# Scenario 13

# You are printing a table where each row contains:

# Product name (left padded)

# Quantity (right padded)

# Price (formatted with 2 decimals)

# Everything must align neatly.

# show me output not code

"""
print(f"{'Product Name':<15}{'Quantity':>10}{'Price':>10}")
print("-" * 40)

print(f"{'Apple':<15}{5:>10}{120.50:>10.2f}")
print(f"{'Banana':<15}{12:>10}{60.00:>10.2f}")
print(f"{'Mango':<15}{3:>10}{150.75:>10.2f}")"""



# You are displaying a bank balance:

# padded to look neat in a box

# formatted with commas

# fixed to 2 decimal points
"""balance = 10000000
print("-"*30)
print(f"|   Balance: {balance:>15,.2f}  |")
print("-"*30)"""


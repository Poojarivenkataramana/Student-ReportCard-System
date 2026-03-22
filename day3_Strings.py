#String methods:-  1.types()
"""value = 21
print("The Value is:",value)
print("The Value type is: ",type(value))

value = 1.200
print("The Value is:",value)
print("The Value type is: ",type(value))

value = "Ramana"
print("The Value is:",value)
print("The Value type is: ",type(value))

value = 1+2j
print("The Value is:",value)
print("The Value type is: ",type(value))

value = True
print("The Value is:",value)
print("The Value type is: ",type(value))"""

#Str():-
"""num = 21
print("before converting:",num)
print(type(num))
str_value = str(num)
print("after converting:",str_value)
print(type(str_value))
"""

"""age = 21
print("My age is:"+ str(age)) # without str we got error because we can only concatenate strings not string + integer
"""

# math function() len():- builtin function output:- integer
# -> len is returns how many items present in a value
# Note:- it counts everything even spaces.

"""password = input("Enter the password: ")

if len(password) < 8:
    print("Your password is too short..")
else:
    print("Your password successfully created.")"""


"""
name = input("Enter the name: ")
print(f"Your name contains {len(name)} characters")"""


# count():- syntax:- count(substring):- str method : output:- integer
# -> returns how often a word repeated in the string


# text = """currently ramana learning python programming
#  he loves to solve problems and gain patterns from it
#  and he loves python a lot
#  """
# print(text.count(input("Enter the word:")))


# Transformations:- 1. replace()
# syntax: (old,new)
# 1️⃣ Correcting typing mistakes

# Scenario:
# A user types:
# I luv progrmming

"""text = input("Enter the text: ").lower().replace(input("Enter old value:"),input("Enter new value:")).replace(input("Enter old value:"),input("Enter new value:"))
print(text)"""

"""text = input("Enter the text: ").lower()
old = input("Enter the value: ")
new = input("Enter the value: ")
old1 = input("Enter the value: ")
new1 = input("Enter the value: ")
print(text.replace(old,new).replace(old1,new1))"""

# NOTE :- we can use multiple replaces
# replace() method is a one of powerful method in python

# 2️⃣ Censoring bad or unwanted words

# Scenario:
# A comment contains abusive words.
# You want to hide them using ****.

# Use case:

# Social media moderation

# Chat filters

# Online forums
"""Badword_data = ["mad","stupid","bitch","idoit","dumb"]

user_input = input("Enter the text: ").split(" ")
for word in user_input:
    if word not in Badword_data:
        print(word,end = " ")
    else:
        print("***")
"""

# 3️⃣ Formatting phone numbers

# Scenario:
# Input:

# 987-654-3210
# Required:

# 9876543210

"""phone_number = input("Enter the number: ").replace("-","")
print("+91",phone_number)"""


# 4️⃣ Converting text format

# Scenario:
# Text:

# 2026/01/26

# Required:

# 2026-01-26

"""date = "2026/01/26"
print(date.replace("/","-"))"""

# 5️⃣ Removing extra spaces

# Scenario:
# Text:

# Hello    World

# Required:

# Hello World
"""entry = "Hello    world"
print(entry.replace("Hello    ","Hello "))"""

# Scenario:
# Email text:

# Hello @user, welcome!


# You want:

# Hello user, welcome!

"""email_text = "Hello @user, welcome".replace("@","")
print(email_text)"""



# 7️⃣ Masking sensitive data

# Scenario:
# Card number:

# 1234 5678 9012 3456


# Display:

# **** **** **** 3456

"""num = "1234 5678 9098 7654".replace(" ","")
extracted = num[12:]
print(f"**** **** **** {extracted}")"""


# 8️⃣ Word customization (dynamic content)

# Scenario:
# Template:

# Hello NAME, welcome to COMPANY


# Replace with:

# Hello Venkat, welcome to Google

"""content = input("Enter the content: ").replace(input("Enter the old:"),input("Enter the new:"))
print(content)"""




# 9️⃣ Cleaning copied text

# Scenario:
# Text copied from website has:

# \n \t extra spaces and breaks
"""text = "Hello\n\t     world".replace("\n","").replace("\t","").replace("Hello     ","Hello ")
print(text)"""


"""text = "Hello\n\t     world"

text = text.replace("\n", " ").replace("\t", " ")

# Now normalize multiple spaces into one
text = " ".join(text.split())

print(text)
"""



# join():-  operator output:- string

# Syntax:- seperator.join(iterable)

# seperator:- String placed between two elements
# iterable :- list,tuple,set etc.(must contain only strings)

"""words = ["I","Love","Python"]
result = " ".join(words)
print(result)
"""

# Example2:- Using different separators
"""data = ['2026','01','26']
print("-".join(data))
print("/".join(data))"""

# Example3:- Joining characters
"""name = "Ramana"
print("-".join(name))
"""
# NOTE:- join() works only strings
# -> if you work on integers or some different data type other than string it shows
# TypeError:- Sequence item0: expected str instance int found
"""t = ("Apple", "Banana","Mango","Orange")
s = {"Red","Green","Yellow","Pink"}
print(",".join(t))
print("/".join(s))
"""
# 1️⃣ Joining individual characters to form a word

# Scenario:
# User types characters one by one:
# P y t h o n
# Need:
# Convert into:
# Python

"""language = input("Enter the type: ")
print("".join(language.split()))"""

"""name = "P y t h o n"
print(name.split())"""




# 2️⃣ Cleaning copied text (removing extra spaces, tabs, newlines)

# Scenario:
# Copied text contains:

# Hello
#      world


# Required clean output:

# Hello world


# Why join?
# To rebuild the sentence with exactly one space between words.

"""text = "Hello\n\tworld".split()
print(" ".join(text))
"""


# """text = """  My name is poojari  venkataramana
# iam studying svpcet college
# b.tech final year
# """
# print(" ".join(text.split()))
# """



# 3️⃣ Formatting a sentence neatly
#
# Scenario:
# Text:
#
# I   love     Python
#
#
# Need:
#
# I love Python

"""text = input("Enter the text: ")
# print(" ".join(text.split()))
print(" ".join(text.split()))"""

# 🔟 Password or key formatting
#
# Scenario:
# User enters:
#
# P y 7 @ x 9
#
#
# Need:
#
# Py7@x9
#
#
# Why join?
# To combine characters into final password string.


"""text = input("Enter the text: ")
print("".join(text.split()))"""



# 9️⃣ Creating CSV-style output
#
# Scenario:
# Words:
#
# apple banana mango
#
#
# Need:
#
# apple,banana,mango
#
#
# Why join?
# To combine words using comma separator.

"""basket = "apple banana    mango"
print(",".join(basket.split()))"""


# 7️⃣ Formatting a phone number
#
# Scenario:
# Digits:
#
# 9 8 7 6 5 4 3 2 1 0
#
#
# Need:
#
# 9876543210

"""digit = input("Enter the numbers: ")
print("".join(digit.split()))"""


# 6️⃣ Making hashtags or tags from text
#
# Scenario:
# Input:
#
# learn python fast
#
#
# Required output:
#
# #learn#python#fast
#
#
# Why join?
# To combine words using a custom separator.
"""text = input("Enter the text: ")
print("#".join(text.split()))"""

# 5️⃣ Creating clean output from messy input
#
# Scenario:
# Input:
#
#    Python     is     awesome
#
#
# Output:
#
# Python is awesome
#
#
# Why join?
# To remove extra spaces and format properly.

"""text = input("Enter the text: ")
print(" ".join(text))"""




#Split method:-

# 1️⃣ Extracting words from a sentence

# Scenario:
# Input:

# Python is very powerful


# Task:
# Get each word separately.

# 👉 Use split to break sentence into words.

"""sentence = input("Enter the text: ").lower().strip()
print("\n".join(sentence.split()))"""




# 2️⃣ Removing extra spaces from copied text

# Scenario:
# Input has random spaces:

# Hello     world     Python


# Task:
# Clean text so words are properly separated.


"""text = input("Enter the text: ").strip().lower()
print(" ".join(text.split()))"""


# 3️⃣ Joining spaced characters into a word

# Scenario:
# Input:

# P   Y   T   H   O   N


# Task:
# Form:

# PYTHON

"""wtotext = input("Enter the Words: ").strip().lower()
print("".join(wtotext.split()))"""



# 4️⃣ Extracting first and last name

# Scenario:
# Input:

# Venkat Ramana


# Task:
# Separate first name and last name.

"""full_name = input("Enter the full name: ").lower().strip()
List = full_name.split()
print(f"First Name:{List[0]}\nLast Name:{List[1]}")"""

# 5️⃣ Cleaning newline and tab polluted text

# Scenario:
# Text copied from website:

# Hello
#      Python


# Task:
# Extract clean words.

# 👉 split treats newline & tab as separators.


# greeting = """ Hello
#     world
#
# """
# print(" ".join(greeting.split()))


# 6️⃣ Counting number of words in text
#
# Scenario:
# Sentence:
#
# Learning Python is fun
#
#
# Task:
# Find how many words exist.
#
# 👉 split gives list of words.

"""words = input("Enter the words: ").lower()
print("The count is:",len(words.split()))"""


# 8️⃣ Parsing comma-separated values
#
# Scenario:
# Input:
#
# apple,banana,mango
#
#
# Task:
# Extract individual items.
#
# 👉 split using comma as separator.

"""items = input("Enter the items: ").lower().split(",")
print(items)
print("\n".join(items))"""




# string repetition:-

# 1️⃣ Creating separators or dividers
#
# Scenario:
# You want a line like:
#
# --------------------
#
#
# Used in:
#
# Reports
#
# Console menus
#
# Section separators
#
# 👉 Repeat - multiple times.

"""print('-' * 20)"""

# 2️⃣ Masking sensitive data
#
# Scenario:
# Credit card:
#
# 1234 5678 9012 3456
#
#
# Required:
#
# **** **** **** 3456
#
#
# 👉 Repeat * to hide digits.

"""n = input("Enter the Credit Card number: ")

print(f"**** **** **** {n[15:]}")"""

# 3️⃣ Creating loading or progress indicators
#
# Scenario:
# Show:
#
# Loading.....
#
#
# 👉 Repeat . dynamically based on progress.
"""
user_input = input("Enter the input: ")
print(f"Your Name is: {user_input + '.'* 5}")"""

#
# 5️⃣ Emphasizing text
#
# Scenario:
# Output:
#
# !!! WARNING !!!
#
#
# 👉 Repeat ! for emphasis.
"""name = input("Enter your name: ")
print(f"{'!'*3 +  name  + '!'* 3}")"""

# String Slicing:-
# 1️⃣ Extracting username from email
#
# Scenario:
# Email:
#
# venkat@gmail.com
#
#
# Need:
#
# venkat
#
#
# 👉 Slice the string before @.

"""mail = input("Enter your mail: ").lower().strip()
for ch in mail:
    if ch == '@':
        break
    print(ch,end = "")"""

# 4️⃣ Extracting last N characters
#
# Scenario:
# Text:
#
# ABCDEFGHIJ
#
#
# Need last 3 characters:
#
# HIJ
#
#
# 👉 Slice from the end.

"""alphabets = "ABCDEFGHIJ"
print(alphabets[-3:])"""


# 5️⃣ Extracting first N characters
#
# Scenario:
# Text:
#
# PythonProgramming
#
#
# Need first 6 characters:
#
# Python

"""program = "PythonProgramming"
print(program[0:6])"""

# 6️⃣ Removing file extension
#
# Scenario:
# Filename:
#
# resume.pdf
#
#
# Need:
#
# resume
#
#
# 👉 Slice before the dot.
"""dot_format = input("Enter the filename:").lower().strip()
# print(dot_format[0:dot_format.find('.')])
pos = dot_format.find('.')

if pos != -1:
    print(dot_format[:pos])
else:
    print(dot_format)
"""


# 9️⃣ Reversing a string
#
# Scenario:
# Text:
#
# Python
#
#
# Need:
#
# nohtyP
#
#
# 👉 Slice with reverse direction.

"""slicing = input("Enter:").strip()
print(slicing[::-1])"""

# 🔟 Extracting middle part of text
#
# Scenario:
# Text:
#
# [ERROR] File not found
#
#
# Need:
#
# ERROR
#
#
# 👉 Slice between brackets.

"""text = input("Enter the text: ").strip().lower()
start = text.index("[") + 1
end = text.index("]")
print(text[start:end])"""

# 7️⃣ Extracting file extension
#
# Scenario:
# Filename:
#
# photo.png
#
#
# Need:
#
# png
#
#
# 👉 Slice after the dot.

"""extension = input("Enter the file: ").lower().strip()
file = extension.find('.')
if file != -1:
    print(extension[file+1:])
else:
    print(extension)"""

# 8️⃣ Formatting phone number
#
# Scenario:
# Number:
#
# 9876543210
#
#
# Need:
#
# 987-654-3210
#
#
# 👉 Slice into parts and format.
"""phone_number = input("Enter the number: ").strip()
sliced = phone_number[:3] + '-' + phone_number[3:6] + '-' + phone_number[6:]
print(sliced)
"""
# Startswith and endswith:-

# Email validation
# Check if an email starts with "admin@" to give admin access.
"""mail = input("Enter the mail: ")
print(mail.startswith("https"))"""

# Endswith:-🔹 endswith() – Scenarios
#
# File extension check
# Check if a file ends with .pdf before allowing upload.
"""extension = input("Enter the extensions: ").lower().strip()
print(extension.endswith("pdf"))"""

# Image filtering
# Confirm image files end with .png or .jpg.

"""Format = input("Enter the format: ").lower().strip()
# print(Format.endswith(".png") or Format.endswith(".jpg"))
if Format.endswith(".png") or (Format.endswith(".jpg")):
    print(f"Format is True")
else:
    print("Format is False")"""



# Slicing():-
# 🔹 1. Extracting First Name
#
# You have a full name:
# "Venkat Ramana"
# You need only "Venkat" for a certificate.

"""name = input("Enter the name: ").lower()
print("Your name is:",name[0:7])
"""
# Showing last four digits:-
# 987654321234

"""number = input("Enter the number: ")
print(f"**** **** {number[8:]}")"""

# 🔹 9. Reversing a String
#
# Word:
# "PYTHON"
# You want it as "NOHTYP"

"""name = input("Enter the name: ")
print(name[::-1])"""

# 🔹 13. Skipping Characters
#
# ID:
# "A1B2C3D4"
# You want only letters → "ABCD

"""character = input("Enter the name: ")
print(character[0:8:2])"""

# 🔹 16. Shortening Long Text for Preview
#
# Message:
# "Welcome to the Python Developer Community"
# Show only first 15 characters in preview

"""message = input("Enter the message:").lower()
print("Your message is :",message[0:15],"****")"""


# Validations():-

# 🔹 1. isalpha() – Only Letters Check
#
# 👉 Used when input must contain only alphabets (A–Z, a–z).
#
# ✅ Scenarios:
#
# Name validation
# While creating a LinkedIn profile, the Name field should contain only letters.
"""user_name = input("Enter the name:").lower()
if user_name.isalpha():
    print(user_name)
else:
    print("User name contains only letters from A-Z & a-z not numbers(0-9)")"""



"""user_name = input("Enter the name:").lower()
valid = ""
for char in user_name:
    valid += char
if valid.isalpha():
    print("Your name is:",valid)
else:
    print("User name only contains letters")"""

# City name validation
# User enters “Chennai” — valid.
# “Chennai123” — invalid.

"""city = input("Enter the city name: ")
if city.isalpha():
    print("City name is:",city)
else:
    print("Invalid city name")"""


# School section field
# Section should be like “A” or “B” — not “A1”.

"""section = input("Enter the section:")
if len(section) == 1:
    if section.isalpha():
        print(section,"Accepted")
    else:
        print(section,"Invalid")
else:
    print("section must contains only single character:")"""

# Mathematical input validation
# User enters “½” (fraction) — still numeric.

"""numeric = input("Enter the number: ")
if numeric.isnumeric():
    print("Your entered:",numeric,"This is numeric")
else:
    print("only numerics allowed")"""

# SO isnumeric allows numbers form (0-9) and fractions and special number systems like Roman numbers
# SO isnumeric do not allows Decimal point → .
#
# Minus sign → -
#
# Slash → /
#
# Comma → ,
#
# Currency symbols → ₹ $ €
#
# Letters → a b c

"""salary = input("Enter the salary: ")
if salary.isnumeric():
    print(f"Your salary is:{salary}")
else:
    print("Invalid Salary")"""

# 3. isalnum() – Letters + Numbers Only
# Username validation
# "Venkat123" → valid
# "Venkat_123" → invalid (underscore not allowed)

"""username = input("Enter Your name: ").lower()
if username.isalnum():
    print("User name is created")
else:
    print("Invalid user_name special symbols are not allowed")"""



# .4 isdigit():-
# Coupon code input
# “SAVE50” → valid
# “SAVE-50” → invalid

"""cupon_code = input("Enter the cupon code:")
if cupon_code.isalnum():
    print("You Have 50% discount..")
else:
    print("Invalid Cupon")"""

# ✅ Scenarios:
#
# OTP verification
# OTP must be digits only.

"""otp = input("Enter the otp:")
if otp.isdigit():
    print("Your otp:",otp)
else:
    print("Invalid")"""

"""space = input("Enter the char: ")
if space.isspace():
    print("True")
else:
    print("False")"""



# 1️⃣ Password Strength Checker
#
# Check if password contains:
#
# At least one uppercase letter
#
# At least one lowercase letter
#
# At least one digit
#
# Behind the scenes → character ranges are compared using ASCII values.

"""Password = input("Enter the Password: ").strip()
Upper_Case = False
Lower_Case = False
Digit = False

for ch in Password:
    if 65 <= ord(ch) <= 90:
        Upper_Case = True
    elif 97 <= ord(ch) <= 122:
        Lower_Case = True
    elif 48 <= ord(ch) <= 57:
        Digit = True
if Upper_Case and Lower_Case and Digit:
    print(f"Your Password is strong:{Password}")
else:
    print("Your Password is weak")"""


# Counting Characters UPPER LOWER DIGITS:-

"""Password = input("Enter the Password: ").strip()
Upper_Case = 0
Lower_Case = 0
Digit = 0

for ch in Password:
    if 65 <= ord(ch) <= 90:
        Upper_Case += 1
    elif 97 <= ord(ch) <= 122:
        Lower_Case += 1
    elif 48 <= ord(ch) <= 57:
        Digit += 1
print(f"Upper_case Count:{Upper_Case}\nLower_Case Count:{Lower_Case}\nDigit Count:{Digit}")"""

"""password = input("Create your password: ").strip()
Upper_Case = False
Lower_Case = False
Digit = False
Special_Char = False
i = 0

while i < len(password):
    ch = password[i]

    if 65 <= ord(ch) <= 90:
        Upper_Case = True
    elif 97 <= ord(ch) <= 122:
        Lower_Case = True
    elif 48 <= ord(ch) <= 57:
        Digit = True
    elif 33 <= ord(ch) <= 47 or 58 <= ord(ch) <= 64 or 91 <= ord(ch) <= 96 or 123 <= ord(ch) <= 126:
        Special_Char = True


    i += 1
if Upper_Case and Lower_Case and Digit and Special_Char:
    
    print(f"Your Password is strong:{password}")
else:
    print("Your Password is weak")
"""

"""old_text = input("Enter the Text: ").strip()
converted_text = ""
for ch in old_text:
    if ch.islower():
        value = ord(ch) - 32
        converted_text += chr(value)
        # print(converted_text,end = "")
    else:
        converted_text += ch

print(converted_text,end = "")"""

"""3️⃣ Caesar Cipher (Basic Encryption)

Shift each letter by 3 positions:
A → D
B → E

Used in:

Basic cryptography logic

Security interview questions"""


# 3️⃣ Caesar Cipher (Basic Encryption)
#
# Shift each letter by 3 positions:
# A → D
# B → E
#
# Used in:
#
# Basic cryptography logic
#
# Security interview questions

"""message = input("Enter the message:").strip().upper()
Encrypt =""
for ch in message:
    if 65 <= ord(ch) <= 90:
        shift = ord(ch) + 3
        if shift > 90:
            Encrypt += chr(shift - 26)
        else:
            Encrypt += chr(shift)
print(Encrypt)"""



"""password = input("Create your password: ").strip()
Upper_Case = False
Lower_Case = False
Digit = False
Special_Char = False
i = 0

while i < len(password):
    ch = password[i]

    if 65 <= ord(ch) <= 90:
        Upper_Case = True
    elif 97 <= ord(ch) <= 122:
        Lower_Case = True
    elif 48 <= ord(ch) <= 57:
        Digit = True
    elif 33 <= ord(ch) <= 47 or 58 <= ord(ch) <= 64 or 91 <= ord(ch) <= 96 or 123 <= ord(ch) <= 126:
        Special_Char = True

    if Upper_Case and Lower_Case and Digit and Special_Char:
        break

    i += 1

if len(password) >= 8:
    if Upper_Case and Lower_Case and Digit and Special_Char:

        print(f"Your Password is strong:{password}")

    else:
        print("Your Password is weak")
else:
    print("Password must contain at least 8 characters")
"""


# 4️⃣ Checking If Character Is Uppercase or Lowercase
#
# When user enters a character:
#
# If it lies in uppercase ASCII range → treat as capital
#
# If in lowercase range → treat as small
#
# Used in:
#
# Text format validation
#
# Compiler logic
#
# Form validation


"""character = input("Enter the character:").strip()
if len(character) != 1:
    print("please enter exactly one character!")
else:
    if 65 <= ord(character) <= 90:
        print(f"{character}:--> is Upper ")
    elif 97 <= ord(character) <= 122:
        print(f"{character}:--> is Lower ")
    elif 48 <= ord(character) <= 57:
        print(f"{character}:--> is Digit ")
    else:
        print(f"{character}:--> is Special")"""



# 5️⃣ Sorting Characters Alphabetically
#
# Given:
# "dbca"
#
# Sorting happens based on ASCII values internally.
#
# Used in:
#
# Dictionary ordering
#
# Search engines
#
# Word games






# 6️⃣ Comparing Characters
#
# Check:
# Is 'a' greater than 'Z'?
#
# This works because each has numeric representation.
#
# Important in:
#
# Interview tricky questions
#
# Logical comparisons

"""Ch1 = input("Enter the character: ")
Ch2 = input("Enter the character: ")
if len(Ch1) != 1 or len(Ch2) != 1:
    print("Please enter only single character each")
else:
    if Ch1 > Ch2:
        print(f"{Ch1} is Greater")
    elif Ch1 < Ch2:
        print(f"{Ch2} is Greater")
    else:
        print("Both are equal")"""



# 9️⃣ Converting Character to Number
#
# Input:
# '7'
#
# Convert to numeric value 7 (for calculations).
#
# Used in:
#
# Calculator apps
#
# OTP verification
#
# Form processing




"""c1 = input("Enter the character: ").strip()
c2 = input("Enter the character: ").strip()
if c1.isdigit() and c2.isdigit():
    num1 = int(c1)
    num2 = int(c2)
    print("Please select operators: + - * % //")
    operator = input("Enter the operator: ")
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '%':
        print(num1 % num2)
    elif operator == '//':
        if operator == '//' and num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 // num2)

    else:
        print("Please existing valid operator")
else:
    print("Only digits are allowed")"""

"""
# 7️⃣ Generate Next Character
#
# If user enters:
# 'A'
#
# System generates next letter:
# 'B'
#
# Used in:
#
# Pattern printing
#
# Alphabet series questions
#
# Exam logical problems

system_out = ""
while True:
    user_input = input("Enter the input: ").strip()
    if len(user_input) != 1:

        print("Please enter only single character")
    else:

        if user_input.isupper():
            system_out = ord(user_input) + 1
            if system_out > 90:
                system_out = system_out - 26
                print(chr(system_out))
            else:
                print(chr(system_out))
        elif user_input.islower():
            system_out = ord(user_input) + 1
            if system_out > 122:
                system_out = system_out - 26
                print(chr(system_out))
            else:
                print(chr(system_out))
        else:
            print("Please enter only Alphabets")
    if user_input == "exit":
        break"""

# 6️⃣ Comparing Characters
#
# Check:
# Is 'a' greater than 'Z'?
#
# This works because each has numeric representation.
#
# Important in:
#
# Interview tricky questions
#
# Logical comparisons




"""inp1 = input("Enter the character: ")
inp2 = input("Enter the character: ")
if len(inp1) != 1 or len(inp2) != 1:
    print("Please enter only single characters: ")
else:
    if inp1.isalpha() and inp2.isalpha():
        if ord(inp1) > ord(inp2):
            print(f"{inp1} is Greater than {inp2}")
        elif ord(inp1) < ord(inp2):
            print(f"{inp2} is Greater than {inp1}")
        else:
            print("Both Characters are Equal!!")
    else:
        print("Please enter alphabets only")"""


# 8️⃣ Checking Special Characters
#
# Detect if character is:
#
# Between A–Z
#
# Between a–z
#
# Between 0–9
#
# Anything else → special symbol
#
# Used in:
#
# Password validation
#
# Username restriction
#
# Data cleaning


"""character = input("Enter the character: ")
if len(character) != 1:
    print("Please enter only single character ")
else:
    if 65 <= ord(character) <= 90:
        print(f"{character} It is a Upper character")
    elif 97 <= ord(character) <= 122:
        print(f"{character} It is a Lower character")
    elif 48 <= ord(character) <= 57:
        print(f"{character} It is a Digit")
    else:
        print(f"{character} It is a Special character")
"""

# 1️⃣2️⃣ Creating Alphabet Patterns
#
# Generate:
# A
# B C
# D E F
#
# This works by incrementing character values step by step.
# Used in:
# Placement coding rounds
# Pattern-based aptitude

"""rows = int(input("Enter the rows: ").strip())
char = 65
for i in range(1,rows+1):
    for j in range(i):
        print(chr(char), end = " ")
        char = char + 1
    print()
"""


# 🔥 Pattern 1 — Reverse Character Triangle
# A B C D
# E F G
# H I
# J


"""chars = int(input("Enter the no.of rows:").strip())
var = 'A'
for i in range(chars):
    for j in range(chars - i):
        print(var,end = " ")
        var = chr(ord(var) + 1)
    print()"""

"""chars = int(input("Enter the no.of rows:").strip())
uniq  =  65
for i in range(chars):
    for j in range(chars - i):
        print(chr(uniq),end = " ")
        uniq = uniq + 1
    print()
    """

# 🔥 Slightly Harder Version
#       A
#     B C
#   D E F
# G H I J
#
"""n = int(input("Enter the no.of rows: ").strip())
current_char = 65
for rows in range(1,n+1):
    for spaces in range(2 *(n - rows)):
        print(" ",end = "")
    for char in range(rows):
        print(chr(current_char),end = " ")
        current_char = current_char + 1
    print()
"""

# Repeating pattern:
# A
# A B
# A B C
# A B C D

"""n = int(input("Enter the no.of rows: ").strip())
for rows in range(1,n+1):
    for cols in range(rows):
        char = chr(ord('A') + cols)
        print(char,end = " ")
    print()"""



# print(len("123"))


"""print("1234".isdigit())


print("apple".replace('p',"P",1))

print("abc".join("123"))
"""

# 🟢 3️⃣ Reverse Each Word (Sentence Reverse Logic)
#
# Input:
# "I am Venkat"
#
# Expected Output:
# "I ma takneV"
#
# 👉 Reverse characters inside each word
# 👉 Word positions stay same

"""inp = input("Enter he sentence: ").split()
reverse = ""
for c in inp:
    reverse += c[::-1] + " "
print(reverse)
"""

# Reversing a string without using builtin functions

"""
original = input("Enter the sentence: ").lower()
reverse = ""
for char in range(len(original) - 1,-1,-1):
    reverse += original[char]
print(reverse)
"""

# 🟢 🔟 Reverse a Number Stored as String Without Losing Leading Zeros
#
# Input:
# "00123"
#
# Expected Output:
# "32100"
#
# 👉 Many students lose leading zeros accidentally.

"""number = input("Enter the digits: ").strip()
reverse = ""
for i in range(len(number) -1,-1,-1):
   reverse += number[i]
print(reverse)
"""
# Above code for logical thinking

# Below code for less occupation better readability to prefer this

"""number = input("Enter the digits: ").strip()
print(number[::-1])"""


# Palindrome Checking:-

"""word = input("Enter the word: ").lower().strip().replace(" ","")
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")"""








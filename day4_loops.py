# Loops concepts:-
# Print numbers from 1 to 10.
"""for i in range(10):
    print(i)"""
# Print numbers from 10 to 1.
"""for i in range(10,0,-1):
    print(i)"""

# Print all even numbers between 1 and 50.

"""for i in range(2,50,2): # if want to o also then we add starting point is 0 
    print(i)
    """
# Print all odd numbers between 1 and 50.

"""for i in range(1,50,2):
    print(i)
"""
# print all numbers between 1 to 20 that are divisible by 3

"""for i in range(3,20+1,3):
    print(i,end = " ")"""
# Print the multiplication table of a given number.
"""n = int(input("Enter a number: "))
for i in range(1,11):
    print(n,"*" ,i ,"=" ,n * i)"""
# using formatting strings:-optional but useful and clean in exams and interviews
#     print(f"{n} * {i} = {n * i}")

# 🔹 FOR Loop with Conditions

# Count how many numbers between 1 and 100 are divisible by 5.
"""count = 0
for i in range(1,51): # or (using step  )
    if i % 5 == 0:
        print(i,end = " ")
        count +=1
print("The count is: ",count)"""

# Print numbers between 1 and 50 that are divisible by 3 and 5.
"""for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i,end = " ")"""

# Count how many positive numbers are in a given list.
"""count = 0
numbers = [-1,-2,3,1,0,-5,7,-2,-1,6,7,8]
for item in numbers:
    if item > 0:
        print(item,end = " ")
        count +=1
print("The negative count is: ",count)"""

# Print PASS or FAIL for each student based on marks (pass ≥ 40).
"""for _ in range(5):
    student = input("Enter the student name: ").lower().strip()
    marks = int(input("Enter the marks: "))
    if marks >= 40:
        print(f"{student} : {marks} Marks\nPass")

    else:
        print(f"{student} : {marks} Marks\nFail")"""


# Find the sum of first N natural numbers.

"""n = int(input("Enter the number: "))
sum1 = 0
for i in range(1,n+1):
    sum1 += i
print("The sum of natural numbers is: ",sum1)
"""
# Print numbers from 1 to N (N given by user).

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(i,end = " ")"""

# Count how many numbers are greater than 50 in a list.
"""numbers = [49,50,51,75,77,91,76,89,98]
count = 0
for item in numbers:
    if item > 50:
        count += 1
        print(item,end = " ")
print()
print("The count is: ",count)"""

# Check whether a number is prime or not
"""number = int(input("Enter the number: "))
if number == 0 or number == 1:
    print("Not Prime")
else:
    for i in range(2,number):
        if number % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime.")"""

# Check prime by counting how many times the number is divisible
"""number = int(input("Enter the number: "))
count = 0
if number == 0:
    print("Not a Prime")
else:
    for i in range(1, number + 1):
        if number % i == 0:
            count +=1
    if count == 2:
        print(f"The count is: {count} It IS a  Prime")
    else:
        print(f"The count is: {count} It IS Not a Prime")"""

# Check prime using loop from 2 to n-1

"""n = int(input("Enter the number: "))
if n == 0 or n == 1:
    print("Not a prime")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not a Prime")
            break
    else:
        print("Prime")"""

# Find the sum of numbers from 1 to N

"""n = int(input("Enter the number: "))
total = 0
for i in range(1, n+1):
    total = total + i
print("The sum is: ",total)"""

# Print numbers divisible by 3
"""n = int(input("Enter the number: "))
for i in range(3,n+1,3):
    print(i,end = " ")"""

# Interview Tip 💡
#
# If interviewer asks:
#
# “Why didn’t you use if condition?”
#
# You can confidently say:
#
# “Using step 3 avoids unnecessary checks and makes the loop more efficient.”
#
# That’s a strong answer.



# Print numbers divisible by 5
"""n = int(input("Enter the number: "))
for i in range(5,n+1,5):
    print(i,end = " ")"""

# Print numbers divisible by both 3 and 5

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
    print(i,end = " ")"""

"""n = int(input("Enter the number: "))
for i in range(15,n+1,15):
    print(i,end = " ")
    """


# Check whether a given number is prime

"""n = int(input("Enter the number: "))
if n == 0 or n==1:
    print("Not a Prime")
else:
    for i in range(2,n):
        if n % i == 0:
            print("Not a Prime!")
            break
    else:
        print("Prime..")"""


# 1️⃣ Print numbers in a table form

# Scenario:
# Print numbers from 1 to 3 in 3 rows, each row containing numbers from 1 to 3.
"""n = int(input("Enter the number: "))
for i in range(n):
    for j in range(1,n+1):
        print(j,end = " ")
    print()"""

# 2️⃣ Star square pattern

# Scenario:
# Print stars in a 3 × 3 square shape.

# 👉 Outer loop → rows
# 👉 Inner loop → stars in each row


"""n = int(input("Enter the how many rowe: "))
for i in range(n):
    for j in range(n):
        print('*',end = " ")
    print()"""


# 3️⃣ Repeating numbers per row

# Scenario:
# Row 1 → print 1 1 1
# Row 2 → print 2 2 2
# Row 3 → print 3 3 3
"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(n):
        print(i ,end = " ")
    print()
"""

# 4️⃣ Counting pattern

# Scenario:
# Print this pattern:
# Row 1 → 1 2 3
# Row 2 → 1 2 3
# Row 3 → 1 2 3


"""n = int(input("Enter the numbers: "))
for i in range(n):
    for j in range(1,n+1):
        print(j,end = " ")
    print()
"""

# 5️⃣ Simple star triangle (left aligned)

# Scenario:
# Print stars like:

# Row 1 → *
# Row 2 → * *
# Row 3 → * * *

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end = " ")
    print()"""

# Scenario:
# Print numbers like:

# Row 1 → 1

# Row 2 → 1 2

# Row 3 → 1 2 3

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()"""




# 5️⃣ Simple star triangle (left aligned)

# Scenario:
# Print stars like:

# Row 1 → *
# Row 2 → * *
# Row 3 → * * *
"""
n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print('*',end = " ")
    print()"""

# 7️⃣ Repeating row number triangle

# Scenario:
# Print:

# Row 1 → 1
# Row 2 → 2 2
# Row 3 → 3 3 3

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for _ in range(i):
        print(i,end = " ")
    print()"""

# Multiplication table (very basic)
# Scenario: Generate tables from 1 to 3,
# each table from 1 to 5.
# 👉 Outer loop → table number
# 👉 Inner loop → multiplication count what is the question ask

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,6):
        print(i ,'*',j ,'=',i*j)
    print()"""
# if user enters any number of input i will give input based table........

"""n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n * i}")
"""

# Scenario:
# Print all possible pairs of numbers from 1 to 3
# Example idea:
# (1,1), (1,2), (1,3), (2,1), ...
"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"({i},{j})",end = ", ")"""

# 1️⃣ Square star pattern

# Pattern:

# * * * *
# * * * *
# * * * *
# * * * *

"""n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        print('*',end = " ")
    print()
"""

# 2️⃣ Increasing star triangle

# Pattern:

# *
# * *
# * * *
# * * * *

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end = " ")
    print()"""



# 3️⃣ Decreasing star triangle

# Pattern:

# * * * *
# * * *
# * *
# *

"""n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n-i): # alternate (range(i,n))
        print('*',end = " ")
    print()"""

# 4️⃣ Number triangle

# Pattern:

# 1
# 1 2
# 1 2 3
# 1 2 3 4

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()"""



# 5️⃣ Repeating row number triangle

# Pattern:

# 1
# 2 2
# 3 3 3
# 4 4 4 4

"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print(i,end = " ")
    print()"""



# 8️⃣ Continuous number pattern

# Pattern:

# 1
# 2 3
# 4 5 6
# 7 8 9 10

"""n = int(input("Enter the number: "))
count = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        count += 1
        print(count,end = ' ')
    print()"""


# 9️⃣ Star + number mix

# Pattern:

# 1 *
# 2 2 *
# 3 3 3 *
"""n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end = " ")
    print('*')"""
    #print()


# 🔥 Interview Tip (VERY IMPORTANT)

# If interviewer asks:

# “Explain pattern logic”

# Say this 👇 (memorize):

# “The outer loop controls the number of rows.
# The inner loop controls how many elements are printed in each row.
# The range of the inner loop decides the shape of the pattern.”


# 1️⃣ Count factors of a number

# Scenario:
# Given a number n, count how many numbers divide n completely.

"""n = int(input("Enter the number: "))
count = 0
print("The factors are:",end = " ")

for i in range(1,n+1):
    if n % i == 0:
        count += 1
        print(i,end = " ")
print("The count is: ",count)"""

# 2️⃣ Check perfect number

# Scenario:
# A number is perfect if the sum of its proper divisors equals the number.
# Check whether a given number is perfect.

"""n = int(input("Enter the number: "))
total = 0
for i in range(1,n):
    if n % i == 0:
        total += i
print("The sum is: ",total)
if total == n:
    print(f"{n} is Perfect number")
else:
    print(f"\n{n} is not perfect")"""


# 3️⃣ Print common factors of two numbers

# Scenario:
# Given two numbers, print all numbers that divide both.

"""n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))
for i in range(1,16):
    if n1 % i == 0 and n2 % i == 0:
        print(i,end = " ")"""

"""
n = int(input("Enter the number: "))
mul = 1
for i in range(1,n+1):
    mul *= i

print(f"The factorial of {n} is:",mul)"""

"""
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for i in range(start,end+1):
    if i <= 1:
        continue
    else:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end = " ")
"""



# While loop:- printing 1 to 5
"""i = 1

while i<=5:
    print(i)
    i +=1
"""
"""password = " "

while password != "Ramana@200309":
    password = input("Enter the password: ").strip().replace(" ","")
print("Access granted")"""




# Print numbers from 1 to N

"""n = int(input("Enter the numer: "))
i = 1
while i <= n:
    print(i)
    i += 1"""

# Print numbers from N to 1

"""n = int(input("Enter the numer: "))

while n:
    print(n)
    n = n-1"""

"""n = int(input("Enter the numer: "))
while n > 0:
    print(n)
    n -= 1"""


# Print all even numbers up to N

"""n = int(input("Enter the number: "))
i = 2
while i <= n:
    print(i,end = " ")
    i += 2
"""


# Print all odd numbers up to N

"""n = int(input("Enter the number: "))
i = 1
while i <= n:
    print(i,end = " ")
    i += 2"""

# Print the square of numbers from 1 to N
"""n = int(input("Enter the number: "))
sqrt = 0
i = 1
while i <= n:
    sqrt = i * i
    i += 1
    print(sqrt,end = " ")"""

# Print numbers divisible by 3 up to N

"""n = int(input("Enter the number: "))
i = 3
while i <= n:
    print(i,end = " ")
    i += 3"""
# Print first N natural numbers

"""n = int(input("Enter the numbers: "))
i = 1
while i <= n:
    print(i,end = " ")
    i += 1
"""



# Print multiplication table of a number
"""n = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i += 1"""


# Count numbers from 1 until a given number

"""n = int(input("Enter the number: "))
i = 1
count = 0
while i <= n:
    print(i,end = " ")
    count += 1
    i += 1

print("\nThe count is:",count)"""

# Print numbers until the user enters 0

"""while True:
    n = int(input("Enter the number: "))
    if n == 0:
        print("stop")
        break
    print(n)"""



"""i = int(input("Enter the number: "))
while i:
    print(i)
    i -= 1"""

# Count how many digits are in a number

"""digits = int(input("Enter the number: "))
count = 0
while digits:
    n = digits % 10
    count += 1
    digits = digits // 10
print("The count is: ",count)"""

# Find the sum of digits of a number

"""number = int(input("Enter the number: "))
total = 0
while number:
    n = number % 10
    total += n
    number = number // 10
print("The total of a number is:",total)"""


# Reverse a number
"""number = int(input("Enter the number: "))
reverse_number = 0
while number:
    current_num = number % 10
    reverse_number  =  (reverse_number * 10) + current_num
    number = number // 10
print(reverse_number)"""

# Count how many even digits are in a number
"""n = int(input("Enter the number: "))
print("The revers number is: ",end = " ")
last_digit = 0
reverse_number = 0
even_count = 0
while n:
    last_digit = n % 10
    if last_digit % 2 == 0:
        even_count += 1
    reverse_number = (reverse_number * 10) + last_digit
    n //= 10
print(reverse_number)
print("The even count is: ",even_count)
print("The even digits are: ",end = " ")
while reverse_number:
    last_digit = reverse_number % 10
    if last_digit % 2 == 0:
        print(last_digit,end = " ")
    reverse_number = reverse_number // 10"""


# Count how many odd digits are in a number
"""n = int(input("Enter the number: "))
print("The reverse_number is: ",end = " ")
odd_count = 0
last_digit = 0
reverse_number = 0
while n:
    last_digit = n % 10
    if last_digit % 2 != 0:
        odd_count += 1
    reverse_number = (reverse_number * 10) + last_digit
    n //= 10
print(reverse_number)
print("The Odd count is: ",odd_count)
print("The Odd digits are:",end = " ")
while reverse_number:
    last_digit = reverse_number % 10
    if last_digit % 2 != 0:
        print(last_digit,end = " ")
    reverse_number //= 10"""

# Find the largest digit in a number
"""n = int(input("Enter the number: "))
print("The largest digit is: ",end = " ")
largest_digit = 0
last_digit = 0

while n:
    last_digit = n % 10

    if largest_digit < last_digit:
        largest_digit = last_digit
    n //= 10
print(largest_digit)"""

# Find the smallest digit in a number
"""n = int(input("Enter the number: "))
small_digit = 9
last_digit = 0

while n:
    last_digit = n % 10
    if small_digit  > last_digit:
        small_digit = last_digit
    n //= 10
print("The smallest digit is: ",small_digit)"""

# Calculate the product of digits of a number

"""n = int(input("Enter the number: "))
product = 1
if n == 0:
    print("The product is: ",n)
else:
    while n:
        last_digit = n % 10
        product *= last_digit
        n //= 10
    print("The Product of a Number is:  ",product)"""

# Check whether a number contains digit 5
"""n = int(input("Enter the number: "))
if n == 0:
    print("The number contains only Zero:",n)
else:
    while n:
        last_digit = n % 10
        if last_digit == 5:
            print("Yes")
            break
        n //= 10
    else:
        print("No")
"""


# Keep taking numbers until user enters a negative number
"""while True:
    number = int(input("Enter the number: "))
    if number < 0:
        print("Loop stops : ",number)
        break
    else:
        print(number)"""



# Print numbers from 1 to 100, skip multiples of 5
"""n = int(input("Enter the number: "))
i = 1
while i <= n:
    if i % 5 == 0:
        i += 1
        continue
    print(i,end = " ")
    i += 1"""


"""n = int(input("Enter the number: "))
i = 1
while i <= n:
    if i % 5 != 0:
        print(i,end = " ")
    i += 1
"""

# Stop printing numbers when number exceeds 50
"""n = int(input("Enter the number: "))
i = 1
while i <= n:
    if i <= 50:
        print(i,end = " ")
        i += 1
    else:
        break
"""

# improved version of above code
"""n = int(input("Enter the number: "))
i = 1
while i <= n and i <= 50:
    print(i,end = " ")
    i += 1"""
# Take input until sum becomes greater than 100
"""total = 0
while total <= 100:
    INPUT = int(input("Enter the number: "))
    total += INPUT
    if total <= 100:
        print("The Sum is: ",total)
    else:
        print("The Total reaches its maximum")"""



# Case conversions:-

"""name = input("Enter the name: ")
print(name.capitalize())
print(name.title())
print(name.swapcase())"""



# Count() :-

# """n = """
# Ramana loves to solve
# problems in python
# """
# print(n.count('Ramana'))"""

# Checking email format
# → Ensuring an email contains exactly one @ symbol.
"""email = input("Enter the  your e-mail: ")
print(email.count('@'))"""

# Joining individual characters to form a word

"""words = ['R','M','A','N','A']
print("".join(words))"""


"""words = ["I","love","Python"]
print(" ".join(words))"""

# using different seperator:-
"""words = ["03","09","2003"]
Date = "/".join(words)
print(f"Date of Birth is: {Date}")"""

# joining characters of a string:-
"""name = "Ramana"
seperator = "-".join(name)
print(seperator)"""

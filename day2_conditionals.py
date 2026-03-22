# Check whether a student is eligible for an exam if attendance is above 75%.
"""
attendance = int(input("Enter the attendance: "))
if attendance >75:
    print("Eligible for exam..")
else:
    print("You should Pay amount to write exam!")"""

# Verify if a number is positive.
"""number = int(input("Enter a number: "))
if number > 0:
    print("Positive.")
else:
    print("Negative.")"""

# Check if a user is logged in before accessing a dashboard.

"""login = input("Enter the login (yes/no)?: ").lower()
if login =='yes':
    print("Your logged in successful.\nWelcome to the Dashboard.")
else:
    print("Your logged in Failed\naccessed denied to Dashboard")"""

# Determine whether a person is eligible to vote based on age.
"""person = int(input("Enter the age: "))
if person >=18:
    print("eligible to vote..")
else:
    print("Not eligible to vote.")"""

# Check if a mobile phone’s battery is below 20% and show a low-battery warning.
"""battery = int(input("Enter the battery percentage: "))
if battery < 20:
    print("Low battery turning on power saving mode!")
else:
    print(" Your battery percentage is goog..")"""

# Check whether a number is even or odd.
"""number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")"""
# Decide if a student passed or failed based on minimum marks.
"""marks = int(input("Enter the Marks: "))
if marks >= 35:
    print("Passed..")
else:
    print("Fail")"""
# Check if a password entered is correct or incorrect.
"""password = input("Enter the password: ")
if password == "200305":
    print("Correct\nLogin successful..")
else:
    print("Incorrect\nTry again!..")"""

# Determine whether a train is on time or delayed.
"""status = input("Enter the Status (ontime / delayed)?: ").lower()
if status == "ontime":
    print("Train arrive the station at scheduled time..")
else:
    print("Train is Delayed..\nSorry for the delay..")"""

# Check if a product is in stock or out of stock.
"""item_status = input("Enter the product status(yes/no): ").lower()
if item_status == 'yes' :
    print("Product in stock..")
else:
    print("Out of Stock.")
    """
# 🔹 IF – ELSE-IF Scenarios (Multiple Conditions)
# Assign grades to a student based on marks:
# Above 90 → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

"""student = input("Enter the student name: ").lower()
marks = int(input("Enter the marks: "))
if marks >= 90:
    print(f"Student Status: {student} Passed with A grade..")
elif 75 <= marks <= 89:
    print(f"Student Status: {student} Passed with B grade.")
elif 50 <= marks <= 74:
    print(f"Student Status: {student} passed with C grade.")
else:
    print(f"Student Status: {student} Fail..")"""

# Calculate electricity bill category based on units consumed.
"""units = int(input("Enter the units: "))
if units >=200:
    print("Category: High rate..")
elif 150 <= units <= 199:
    print("Category: moderate..")
elif 100 <= units <= 149:
    print("Category: budget rate..")
else:
    print("Category: free to use..")"""
# Check if a student passed the exam, and if passed, check whether they are eligible for a scholarship.
"""student = input("Enter the student name: ").lower()
marks = int(input("Enter the marks: "))
if marks >= 35:
    if marks >=75:
        print(f"Student Name: {student} Passed and ✅eligible for scholarship..")
    else:
        print(f"Student Name: {student} Passed but ❌not eligible for scholarship")
else:
    print(f"Student Name: {student} Fail..")"""

# Verify user login:

# First check if username exists

# Then check if password is correct

"""user_name = input("Enter the name exists (yes/no)?: ").lower()
if user_name == 'yes':
    password = (input("Enter the password: ")).strip()
    if password == "ramana@200305":
        print("User login successful")
    else:
        print("User exists but wrong password\nTry again!.")
else:
    print("user doesn't exist..")"""

# Check if a bank account is active, and if active, check whether sufficient balance is available.
"""account_status = input("Enter the bank account status (active/inactive)?: ").lower()
if account_status == 'active':
    balance = int(input("Enter the balance: "))
    if balance > 0:
        print("You ha a sufficient balance keep it and save it.")
    else:
        print("You have insufficient balance please add otherwise your account will inactive..")
else:
    print("Your account is inactive\nPlease active your account and add some money..")"""

# Determine if a person is eligible for a job:

# First check qualification

# Then check experience
print("➡️Microsoft hiring only freshers please check eligibility:-")
print()
name = input("Enter the name of the candidate: ").lower().strip()
qualification = input("Enter the qualification: ").lower().strip().replace(" ","")

if qualification == 'b.tech' or qualification == 'degree':
    experience = input("Enter the experience (yes/no)?: ")
    if experience == 'no':
        print("Welcome to the interview.")
    else:
        print("Sorry sir! we are currently we encourage freshers not experience\nif we want experience candidates then we emai you so you may leave now! ")
else:
    print("Sorry you are not eligible for this job!.")

# Check if a vehicle is allowed on the highway:

# First check vehicle type

# Then check pollution certificate validity
# show me output mot code

vehicle = input("Enter the vehicle type:  ").lower().strip().replace(" ","")
allowed = input("Enter the vehicle is allowed on highway (yes/no)?: ")
if allowed == 'yes':
    puc = input("Show me the PUC (valid/invalid)?: ").lower()
    if puc == 'valid':
        print("The vehicle is allowed to highway")
    else:
        print("allowed but PUC experied.")
else:
    print("Not allowed")

# Check delivery availability for the user’s location.

# If delivery is available, proceed to payment.

# If payment is successful, confirm the order.

# If delivery is not available, show “Delivery not available” and stop the process.

# If payment fails, show “Payment failed” and do not confirm the order.

print("Flipkart shopping checkout list: ")
print()
checkout_list = input("Enter the product name: ").lower().strip().replace(" ","")
address = input("Enter the city pincode(available/not available)?: ").lower().strip().replace(" ","")
if address == "available":
    payment_status = input("Enter the payment status (success/fail)?: ").lower()
    if payment_status == "success":
        print("Confirm your order\nThankyou for choosing flipkart")
    else:
        print("Payment failed.\nOrder not confirmed.")
else:
    print("no delivery to your address..")

































password = input("Create your password: ").strip()
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
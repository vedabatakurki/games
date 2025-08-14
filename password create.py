import re
import random
import string

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()<>[\]]", password) is None

    errors = [length_error, lowercase_error, uppercase_error, digit_error, symbol_error]
    error_count = sum(errors)

    if error_count == 0:
        return "strong"
    elif error_count <= 2:
        return "medium"
    else:
        return "weak"

def generate_strong_password(length=12):
    if length < 8:
        length = 8

    chars = string.ascii_letters + string.digits + "!@#$%^&*()<>[]"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
def main():
    while True:
        print("1. password strength check")
        print("2. generate strong password")
        print("3. exit")

        choice = input("enter your choice (1/2/3): ")
        if choice == "1":
            pwd = input("enter your password: ")
            strength = check_password_strength(pwd)
            print(f"strength of your password is: {strength}")
        elif choice == "2":
            try:
                length = int(input("enter password length (min 8): "))
            except ValueError:
                print("Invalid input, using default length of 12")
                length = 12
            pwd = generate_strong_password(length)
            print(f"your password is: {pwd}")
        elif choice == "3":
            print("exit")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
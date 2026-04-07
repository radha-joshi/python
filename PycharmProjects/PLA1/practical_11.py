#exception handling in python

#Radha Joshi [122-A]
def check_adult_age():
    while True:
        try:
            user_input = input("Enter your age: ")
            assert int(user_input) > 18

        except ValueError:
            print("ValueError: Please insert a valid number. Let's try again.\n")

        except AssertionError:
            print("AssertionError: You are 18 or under. Let's try again.\n")

        else:
            print("Success: You are an Adult!")
            break

check_adult_age()

#Radha Joshi [122-A]
def get_quotient():
    print("Division Calculator")
    while True:
        try:
            n1 = input("Enter the first number: ")
            n2 = input("Enter the second number: ")

            ans = int(n1) / int(n2)

        except ZeroDivisionError:
            print("ZeroDivisionError: Denominator cannot be zero. Let's try again.\n")

        except ValueError:
            print("ValueError: Please insert valid integers. Let's try again.\n")

        else:
            print("The quotient is:", ans)
            break

get_quotient()

#Radha Joshi [122-A]
class InvalidPasswordError(Exception):
    pass

def check_password():
    print("Security Login")
    while True:
        try:
            pwd = input("Enter your password: ")

            if pwd != "admin123":
                raise InvalidPasswordError

        except InvalidPasswordError:
            print("InvalidPasswordError: Password is not correct. Try again.\n")

        else:
            print("Access Granted! Welcome to the system.")
            break

check_password()
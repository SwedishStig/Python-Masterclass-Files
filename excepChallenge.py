import sys
# first = input("Please input the first number:\n")
# second = input("Please input the second number:\n")
#
# try:
#     ruhsult = first / second
# except (ZeroDivisionError, FloatingPointError, TypeError):
#     ruhsult = "Yeah, that isn't something Python can process. Get bent"
#
# print(ruhsult)


def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Use a number, smart guy")
        except EOFError:
            sys.exit(1)


first = get_int("Please input the first number:\n")
second = get_int("Please input the second number:\n")

try:
    ruhsult = first / second
except ZeroDivisionError:
    ruhsult = "Yeah, that isn't something Python can process. Get bent"

print(ruhsult)
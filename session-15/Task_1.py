#Write a Python function safe_divide(a, b) that returns the result of a divided by b,
#and handles ZeroDivisionError by returning the string 'Cannot divide by zero'.


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Cannot divide by zero'


print(safe_divide(100, 4))
print(safe_divide(100, 0))
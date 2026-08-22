#Use ChatGPT or Copilot to generate a Python code snippet that asks for two numbers and divides them, handling both ZeroDivisionError and ValueError.
#Paste the generated code, run it, and write one line about what you learned from the AI's approach.


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

#Python can use separate except blocks to handle different types of error,making the program more reliable and userfriendly.
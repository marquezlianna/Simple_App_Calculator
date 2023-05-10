# Marquez, Lianna L._BSCpE 1-4

# Create a Simple App Calculator
    # The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
    # The application will ask the user for two numbers
    # Display the result
    # The application will ask if the user wants to try again or not.
    # If yes, repeat Step 1.
    # If no, Display “Thank you!” and the program will exit
    # Use Python Function and appropriate Exceptions to capture errors during runtime.
    
def calculator():
    
# Ask the user to input the first and second number
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
# Ask the user to choose an operation
    operation = input("Please enter an operation: +-*/ ")   
     
# Perform the operation
    # if addition
    if operation == "+":
        ans = num1 + num2
    # if subtraction
    elif operation == "-":
        ans = num1 - num2
    # if multiplication
    elif operation == "*":
        ans = num1 * num2
    # if division
    elif operation == "/":
        ans = num1/num2
    
    else:
        ans = "Invalid operation"

# Print the output
    print(f"Answer: {ans}")
    
while True:
    calculator()
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
    # Add space between every operation
    print("\n")
    
    # Ask the user to input the first and second number
    try:
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
    # Return if the user input invalid number
    except ValueError as ERROR:
        print("Invalid number input\n")
        print(ERROR)
        print("\nTry Again!")
        return
    
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
        # if the user input a zero number
        try:
            ans = num1/num2
        except ZeroDivisionError as ERROR:
            print("Invalid equation\n")
            print(ERROR)
            print("\nTry again!")
            return
    # if the user enter an invalid operation
    else:
        ans = "Invalid operation"

# Print the output
    print('\033[1;35m'f"Answer: {ans}")

# Ask if the user wants to try again or not.  
while True:
    print("\n")
    try_again = input('\033[1;34m'f"Do you want to try again? (yes/no): ")
    if try_again.lower() != "yes":
        print('\033[1;95;40m'f"Thank you for using the Simple Calculator App!")
        break
    
    calculator()
    

    
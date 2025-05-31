# --- Step 1: Get the two numbers from the user ---
try:
    num1_str = input("Enter the first number: ")
    num1 = float(num1_str) # Convert text to a number (allows decimals)

    num2_str = input("Enter the second number: ")
    num2 = float(num2_str) # Convert text to a number
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    # Exit the program if numbers are not valid
    exit()

# --- Step 2: Ask the user to choose an operation ---
print("\nChoose an operation:")
print("  + for Addition")
print("  - for Subtraction")
print("  * for Multiplication")
print("  / for Division")

operation = input("Enter your choice (+, -, *, /): ").strip() # .strip() removes extra spaces

# --- Step 3: Perform the chosen operation ---
result = None # Initialize result to None

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
else:
    print("Invalid operation choice. Please use +, -, *, or /.")

# --- Step 4: Print the result ---
if result is not None: # Only print if a valid calculation happened
    print("Result:", result)

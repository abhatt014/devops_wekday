# Ask the user to enter two numbers.
# Ask the user to enter an operation (+, -, *, /).
# Based on the operation, calculate and print the result.

# Get user input for the first number
num1_str = input("Enter the first number: ")
num1 = float(num1_str)  # Convert to float  
# Get user input for the second number
num2_str = input("Enter the second number: ")
num2 = float(num2_str)  # Convert to float  
# Get user input for the operation
operation = input("Enter the operation (+, -, *, /): ")     
# Perform the calculation based on the operation
if operation == '+':    
    result = num1 + num2    
elif operation == '-':  
    result = num1 - num2    
elif operation == '*':  
    result = num1 * num2    
elif operation == '/':     
    result = num1 / num2    
else:    
    result = "Error: Invalid operation!"
# Print the result      
print(f"The result is: {result}")   

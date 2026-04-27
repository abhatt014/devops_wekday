# def greeting(name):
# 	return f"Hello, {name}!"

# fname = input("Enter your name: ")
# print(greeting(fname))

def add_numbers(a, b):
    return a + b
input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")
num1 = float(input1)  # Convert to float
num2 = float(input2)  # Convert to float
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")    
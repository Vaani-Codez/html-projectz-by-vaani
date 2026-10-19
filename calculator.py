def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error! Division by Zero."
    return a/b
# Dictionary acting as a switch statement
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    print("---Python Calculator---")
    print("Select operation: +, -, *, /")
    choice = input("Enter operator (+, -, *, /): ")
    if choice not in operations:
        print("Invaild operator choice!")
        return
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return
    # Call the corresponding function from the dictionary
    result = operations[choice](num1,num2) 
    print(f"Result: {num1} {choice} {num2} = {result}")
if __name__ == "__main__":
    calculator()
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def exponentiate(a, b):
    return a ** b

def square_root(a): 
    if a < 0:
        return "Error: Square root of a negative number is not defined."
    return math.sqrt(a)   

def trig_function(operation, angle):
    radians = math.radians(angle)
    if operation == "sin":
        return math.sin(radians)
    elif operation == "cos":
        return math.cos(radians)
    elif operation == "tan":
        return math.tan(radians)
    else:
        return "Error: Invalid trigonometric function."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    history = []
    
    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Square Root (√)")
        print("7. Trigonometric Functions (sin, cos, tan)")
        print("8. View History")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '9':
            print("Exiting calculator. Goodbye!")
            break
        
        elif choice == '8':
            print("Calculation History:")
            for entry in history:
                print(entry)
            continue
        
        elif choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"
            elif choice == '5':
                result = exponentiate(num1, num2)
                operation = f"{num1} ^ {num2} = {result}"
            
        elif choice == '6':
            num = get_number("Enter a number: ")
            result = square_root(num)
            operation = f"√{num} = {result}"
        
        elif choice == '7':
            func = input("Enter function (sin, cos, tan): ")
            angle = get_number("Enter angle in degrees: ")
            result = trig_function(func, angle)
            operation = f"{func}({angle}°) = {result}"
        
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print("Result:", result)
        history.append(operation)
        
if __name__ == "__main__":
    calculator()

        


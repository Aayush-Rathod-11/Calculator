# Basic Calculator with Error Handling

# --- Calculator Functions ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:   # Handling division by zero
        return "Error: Division by zero is not allowed."
    return a / b

def power(a, b):   # Bonus Function
    return a ** b

# --- Main Program ---
def calculator():
    print("===== Basic Calculator =====")
    while True:
        print("\nMenu:")
        print("1. Perform Calculation")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == "2":
            print("Exiting... Thank you for using the calculator!")
            break
        elif choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operation = input("Choose operation (+, -, *, /, ^): ")

                if operation == "+":
                    print(f"Result: {add(num1, num2)}")
                elif operation == "-":
                    print(f"Result: {subtract(num1, num2)}")
                elif operation == "*":
                    print(f"Result: {multiply(num1, num2)}")
                elif operation == "/":
                    print(f"Result: {divide(num1, num2)}")
                elif operation == "^":
                    print(f"Result: {power(num1, num2)}")
                else:
                    print("Error: Invalid operation selected!")
            
            except ValueError:
                print("Error: Invalid input! Please enter numbers only.")
        
        else:
            print("Error: Invalid choice. Please select 1 or 2.")

# Run the program
if __name__ == "__main__":
    calculator()

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result

    def sub(self, num1, num2):
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multi(self, num1, num2):
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def div(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        result = num1 / num2
        self.history.append(f"{num1} / {num2} = {result}")
        return result
    
    def expo(self,num1,num2):
        result=num1**num2
        self.history.append(f"{num1}**{num2}={result}")
        return result
        
    def display_history(self):
        print("Calculator History:")
        for entry in self.history:
            print(entry)
calculator = Calculator()

while True:
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Display History")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.add(num1, num2)
        print(f"Result: {result}")
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.sub(num1, num2)
        print(f"Result: {result}")
    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.multi(num1, num2)
        print(f"Result: {result}")
    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculator.div(num1, num2)
        print(f"Result: {result}")
    elif choice =="5":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number:"))
        result = calculator.expo(num1, num2)
        print(f"Result:{result}")
    elif choice == "6":
        calculator.display_history()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")


def add(a, b):
    return a + b

def subtract(a, b):
     return a - b
 
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def remainder(a,b):
    return a % b

def floor_divide(a, b):
    return a // b

def calculator():
    while True:
        try:  
            while True:
                try:
                    a = float(input("Enter the first number: "))
                    break
                except ValueError : 
                    print("Please enter a number!")
                    
            while True:
                try:
                    b = float(input("Enter the second number: "))
                    break
                except ValueError : 
                    print("Please enter a number!")
                    
            while True:
                    op = input("Enter the operation : ")
                    if op in ["+", "-", "*", "/", "**", "%", "//"]:
                        break
                    else:
                        print("Invalid operation! Please try again.")   
                                    
            if op == "+":
                result = add(a,b)
            elif op == "-":
                result = subtract(a,b)
            elif op == "*":
                result = multiply(a,b)
            elif op == "/":
                result = divide(a,b)
            elif op == "**":
                result = power(a,b)
            elif op == "%":
                result = remainder(a,b)
            elif op == '//':
                result = floor_divide(a,b)
                
            print(f"\nResult : {result}")
            
            while True:
                again = input("\n Do you want to use calculator again?(yes/no): ").lower().strip()
                if again in ("yes", "no"):
                    break
                else:
                    print("Please enter 'yes' or 'no'.")
                
            if  again != "yes":
                print("Goodbye!")
                break
            else:
                continue
        except ZeroDivisionError : 
            print("Error: Cannot divide by zero!")
        except Exception as e :
            print("Unexpected error:", e)
            
if __name__ == "__main__" :   
    calculator()
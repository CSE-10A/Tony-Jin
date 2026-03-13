# skibidi calculator

def addition(a, b): # addition function
    return a + b

def subtraction(a, b): # subtraction function
    return a - b

def multiplication(a, b): # multiplication function
    return a * b

def division(a, b): # division function
    if b == 0:
        return "dividing by zero is undefined"
    return a / b

a = float(input("Enter the first number: ")) # first num input
b = float(input("Enter the second number: ")) # second num input

print("select an operation:") # printing all options
print("1) addition")
print("2) subtraction")
print("3) multiplication")
print("4) division")

choice = input("Enter choice (1/2/3/4): ")
if choice == "1":
    print(a, "+", b, "=", addition(a, b))
elif choice == "2":
    print(a, "-", b, "=", subtraction(a, b))
elif choice == "3":
    print(a, "*", b, "=", multiplication(a, b))
elif choice == "4":
    print(a, "/", b, "=", division(a, b))

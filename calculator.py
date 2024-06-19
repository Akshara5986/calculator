# Add two numbers
def add(a, b):
    return a + b
 
# Subtract two numbers
def subtract(a, b):
    return a - b
 
# Multiply two numbers
def multiply(a, b):
    return a * b
 
# Divide two numbers
def divide(a, b):
    return a / b

# Exponentiation of two numbers
def pow(a, b):
    return a ** b
 
print("Please select operation -\n" 
        "1. Add\n" 
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n"
        "5. Power\n")
 
 
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4, 5:"))
 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
 
if select == 1:
    print(a, "+", b, "=",
                    add(a, b))
 
elif select == 2:
    print(a, "-", b, "=",
                    subtract(a, b))
 
elif select == 3:
    print(a, "*", b, "=",
                    multiply(a, b))
 
elif select == 4:
    print(a, "/", b, "=",
                    divide(a, b))

elif select == 5:
    print (a, "**", b, "=",
                    pow(a, b))
else:
    print("Invalid input")

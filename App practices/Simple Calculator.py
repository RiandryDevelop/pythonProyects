# Simple calculator

def operations():    
    a = int(input("#1:"))
    b = int(input("#2:"))
    op = input("Operation:")
    
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    if op == "x" or op == "X":
        print(a * b)
    if op == "/":
        print(abs(a / b))


operations()


again = input("Again:")

if again.capitalize() == "Si":
    operations()
else:
    breakpoint()
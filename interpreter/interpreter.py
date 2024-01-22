x,y,z = input("Expression: ").split(" ")

if y == "+":
    sol = float(x) + float(z)
    print(sol)
if y == "-":
    sol = float(x) - float(z)
    print(sol)
if y == "*":
    sol = float(x) * float(z)
    print(sol)
if y == "/":
    sol = float(x) / float(z)
    print(sol)

Expression = input("Expression: ")
x, y, z = Expression.split()

if y == "+":
    output = float(x) + float(z)
    print(output)
elif y == "-":
    output = float(x) - float(z)
    print(output)
elif y == "*":
    output = float(x) * float(z)
    print(output)
elif y == "/":
    output = float(x) / float(z)
    print(output)
num1 = float(input("Enter First Number: "))
print("The operators are +, -, *, /. P.M.M.D.")
op = input("Enter Operator: ")
num2 = float(input("Enter Second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
input("Press enter when you're done")
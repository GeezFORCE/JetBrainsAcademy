# put your python code here
num1, num2, op = float(input()), float(input()), input()
if op == '/':
    if num2 == 0:
        print("Division by 0!")
    else:
        print(num1 / num2)
elif op == "pow":
    print(num1 ** num2)
elif op == "div":
    if num2 == 0:
        print("Division by 0!")
    else:
        print(num1 // num2)
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "mod":
    if num2 == 0:
        print("Division by 0!")
    else:
        print(num1 % num2)
elif op == "*":
    print(num1 * num2)

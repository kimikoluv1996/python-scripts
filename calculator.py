n = input("enter two numbers: ")
opp = input("enter an operation to do: ")

li = n.split()

try:
    num1 = li[0]
    num2 = li[1]
except IndexError:
    print("please enter two numbers")
    
if opp == "*":
    print(f"{num1} times {num2} is equal to {int(num1) * int(num2)}")
elif opp == "/":
    try:
        print(f"{num1} divided by {num2} is equal to {int(num1) / int(num2)}")
    except ZeroDivisionError:
        print(f"{num1} divided by zero is undefined.")
elif opp == "+":
    print(f"{num1} plus {num2} is equal to {int(num1) + int(num2)}")
elif opp == "-":
    print(f"{num1} minus {num2} is equal to {int(num1) - int(num2)}")
else:
    print(f"{opp} is not a valid operation")
# Working Basic Calculator

while True:
    try:
        inp = input("Expr: ")
        token_list = inp.split()
        if token_list[1] == '+':
            answer = int(token_list[0]) + int(token_list[2])
        elif token_list[1] == '-':
            answer = int(token_list[0]) - int(token_list[2])
        if token_list[1] == '*':
            answer = int(token_list[0]) * int(token_list[2])
        elif token_list[1] == '/':
            answer = int(token_list[0]) / int(token_list[2])

        print(f"{answer}")
    except KeyboardInterrupt:
        print("Exiting....")
        break
    except ZeroDivisionError:
        print("Can't Divide by Zero.")



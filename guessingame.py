import random

# computer selects random integer and stores it
random_num = random.randint(1, 4)
print(random_num) # print for debug

print("I'm thinking of a number")

try:
    while True:
        n = input("> ")
        if int(n) != random_num:
            if int(n) > random_num:
                print("too high")
                continue
            elif int(n) < random_num:
                print("too small")
                continue
        elif int(n) == random_num:
            print("congrats, you got it right!")
            break
except KeyboardInterrupt:
    print("quitting...")
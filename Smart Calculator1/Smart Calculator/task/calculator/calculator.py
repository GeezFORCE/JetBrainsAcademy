# write your code here
while True:
    inp = input()
    if inp == "/exit":
        print("Bye!")
        exit()
    elif inp == "/help":
        print("The program calculates the sum of numbers")
    else:
        num = [int(i) for i in inp.split()]
        if len(num) == 0:
            continue
        else:
            print(sum(num))
# write your code here
while True:
    inp = input()
    if inp == "/exit":
        print("Bye!")
        exit()
    else:
        num = list(map(int, inp.split()))
        if len(num) == 0:
            continue
        else:
            print(sum(num))
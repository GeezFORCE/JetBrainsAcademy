num = int(input())
flag = 1
if num == 1:
    print("This number is not prime")
    exit()
else:
    for i in range(2, num//2):
        if num % i == 0:
            flag = 0
            break
if flag == 0:
    print("This number is not prime")
else:
    print("This number is prime")

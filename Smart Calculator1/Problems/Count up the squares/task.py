# put your python code here
num = list()
while True:
    num.append(int(input()))
    if sum(num) == 0:
        break
print(sum([i ** 2 for i in num]))

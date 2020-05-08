# put your python code here
numbers, key = [int(digits) for digits in input().split()], int(input())
if key not in numbers:
    print("not found")
for pos, number in enumerate(numbers):
    if key == number:
        print(pos, end=" ")

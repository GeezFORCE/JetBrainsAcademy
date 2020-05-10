a, b, h = int(input()), int(input()), int(input())
if a <= h < b:
    print("Normal")
elif h > b:
    print("Excess")
else:
    print("Deficiency")
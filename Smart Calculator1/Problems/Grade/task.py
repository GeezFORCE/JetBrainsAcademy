score, max_score = int(input()), int(input())
percentage = score / max_score * 100
if 90 < percentage <= 100:
    print("A")
elif 80 < percentage <= 90:
    print("B")
elif 70 < percentage <= 80:
    print("C")
elif 60 < percentage <= 70:
    print("D")
else:
    print("F")

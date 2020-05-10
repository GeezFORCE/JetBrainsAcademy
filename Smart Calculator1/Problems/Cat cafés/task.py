cats = dict()
while True:
    inp = input()
    if inp == "MEOW":
        break
    cat, num = inp.split()
    num = int(num)
    cats[num] = cat
print(cats[max(cats, key=cats.get)])

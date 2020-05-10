offset = int(input())
hours = 10
#print(hours-offset)
if hours - abs(offset) < 0:
    print("Monday")
elif 0 < hours - offset < 24 or 0 < hours - offset < 24 :
    print("Tuesday")
else:
    print("Wednesday")
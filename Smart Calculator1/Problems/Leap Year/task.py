# put your python code here
year = int(input())
print("Leap" if year % 4 == 0 and 0 != year % 100 or year % 400 == 0 else "Ordinary")

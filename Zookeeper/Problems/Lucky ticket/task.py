# Save the input in this variable
ticket = list(input())
# Add up the digits for each half
ticket = list(map(int, ticket))
half1 = sum(ticket[:3])
half2 = sum(ticket[3:])
# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
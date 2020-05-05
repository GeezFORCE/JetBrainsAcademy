intial_sum = float(input())
year=0
sum=intial_sum;
while(sum<=700000):
    sum = 1.071*sum
    year+=1
print(year)
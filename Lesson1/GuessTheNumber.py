import random

n=random.randrange(0,20,1)
found = False
print(n)
for i in range(1,4):
    a=int(input())
    if a==n:
        print("Correct")
        found=True
        break
    elif a<n:
        print("Too low")
    else:
        print("Too high")
if found:
    print("Winner")
else:
    print("Looser")

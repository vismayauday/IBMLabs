x=int(input())
y=0
for i in range(2,x):
    if x%i==0:
        print("Composite")
        y=1
        break
if y==0:
    print("Prime")
x=int(input())
y=int(input())
m=0
if x>y:
    l=x
else:
    l=y
for i in range(2,l+1):
    if x%i==0 and y%i==0:
        m=i
print(m)

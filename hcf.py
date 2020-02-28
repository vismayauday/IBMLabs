x=int(input())
y=int(input())
if x>y:
    sml=y
else:
    sml=x
for i in range(1,sml+1):
    if x%i==0 and y%i==0:
        h=i;
print(h)
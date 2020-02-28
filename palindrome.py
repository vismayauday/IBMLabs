x=int(input())
y=x
r=0
s=0
while x>0:
    s=x%10;
    r=(r*10)+s
    x//=10
if r==y:
    print("Palindrome")
else:
    print("Not Palindrome")
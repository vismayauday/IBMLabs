x=int(input())
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
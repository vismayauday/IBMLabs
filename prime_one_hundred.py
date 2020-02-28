for i in range(2,100):
    y=0
    for j in range(2,i):
        if i%j==0:
            y=1
            break
    if y==0:
        print(i)

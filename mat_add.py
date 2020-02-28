a=[[12,5,6],[5,6,7],[6,7,8]]
b=[[3,4,5],[4,5,6],[6,7,8]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
            r[i][j]=a[i][j]+b[i][j]
for i in r:
    print(i)
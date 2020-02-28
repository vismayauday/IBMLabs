m=[]
n=[]
r=[]
for i in range(3):
    a=[]
    for j in range(3):
        a.append(int(input()))
    m.append(a)
for i in range(3):
    a=[]
    for j in range(4):
        a.append(int(input()))
    n.append(a)
for i in range(3):
    a=[]
    for j in range(4):
        a.append(0)
    r.append(a)
for i in range(3):
    for j in range(4):
        for k in range(3):
            r[i][j]+=m[i][k]*n[k][j]
for i in r:
    print(i)
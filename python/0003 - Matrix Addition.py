n = input().split()
m1 = []
m2 = []
mAns = []

for i in range(int(n[0])):
    m1.append([])
    m2.append([])
    mAns.append([])
    for j in range(int(n[1])):
        m1[i].append(0)
        m2[i].append(0)
        mAns[i].append(0)

for i in range(int(n[0])):
    x = input().split()
    for j in range(int(n[1])):
        m1[i][j] = x[j]

for i in range(int(n[0])):
    x = input().split()
    for j in range(int(n[1])):
        m2[i][j] = x[j]

for i in range(int(n[0])):
    for j in range(int(n[1])):
        mAns[i][j] = int(m1[i][j]) + int(m2[i][j])
        mAns[i][j] = str(mAns[i][j])

for i in range(len(mAns)):
    print(" ".join(mAns[i]))

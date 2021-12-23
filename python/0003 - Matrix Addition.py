X, Y = input().split()
A = []
B = []
#A = [[1,2,3],[3,2,1],[1,3,2]]
#B = [[1,1,1],[1,1,1],[1,1,1]]
for i in range(int(X)):
    A.append([int(z) for z in input().split()])
for i in range(int(Y)):
    B.append([int(z) for z in input().split()])

new = []

for i in range(int(X)):
    new.append([])
    for j in range(int(X)):
        #print(i, j)
        new[i].append(A[i][j]+B[i][j])
#print(new)
total = len(new)
for i in range(total):
    print(*new[i], sep = " ")
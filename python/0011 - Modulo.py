num = []
chk = []
for i in range(10):
    num.append(int(input()))  

count = 0  
for i in num:
    cal = i % 42
    if cal not in chk:
        chk.append(cal)
        count += 1
print(count)

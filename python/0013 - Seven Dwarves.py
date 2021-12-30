dwarves = []

for i in range(9):
    dwarves.append(int(input()))

total = sum(dwarves) - 100
for i in range(9):
    for j in range(i+1, 9):
        if total == dwarves[i] + dwarves[j]:
            for k in dwarves:
                if k!=dwarves[i] and k!=dwarves[j]:
                    print(k)
    
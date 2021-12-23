move = input()
glass = [1 ,0, 0]

for i in move:
    if i == "A":
        a, b = glass[1], glass[0]
        glass[0], glass[1] = a, b
    if i == "B":
        a, b = glass[2], glass[1]
        glass[1], glass[2] = a, b
    if i == "C":
        a, b = glass[2], glass[0]
        glass[0], glass[2] = a, b

count = 0
for i in glass:
    count += 1
    if i == 1:
        break
print(count)
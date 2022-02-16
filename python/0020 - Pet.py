max_score = 0
winner = 0

for i in range(5):
    people = sum([int(x) for x in input().split()])
    if people > max_score:
        max_score = people
        winner = i+1
print(winner, max_score)
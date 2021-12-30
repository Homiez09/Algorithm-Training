n = int(input())
people_score = {
    'Adrian':0,
    'Bruno':0,
    'Goran':0
}
people_answer = {
    'Adrian':'ABC',
    'Bruno':'BABC',
    'Goran':'CCAABB'
}

for i, j in enumerate(input()):
    for k, l in people_answer.items():
        if l[i%len(l)] == j:
            people_score[k] += 1

max_point = max(people_score.values())
print(max_point)

for i, j in people_score.items():
    if j == max_point:
        print(i)
           
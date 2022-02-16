teams = []
scores = []

for i in range(4):
    teams.append(input())
for i in range(4):
    scores.append(input().split())

score_team = {teams[0]: 0, teams[1]: 0, teams[2]: 0, teams[3]: 0}
score_end = {teams[0]: 0, teams[1]: 0, teams[2]: 0, teams[3]: 0}

for i in range(4):
    for j in range(i, 4):
        if i == j:
            continue
        if int(scores[i][j]) > int(scores[j][i]):
            score_end[teams[i]] += 3
        elif int(scores[i][j]) < int(scores[j][i]):
            score_end[teams[j]] += 3
        elif int(scores[i][j]) == int(scores[j][i]):
            score_end[teams[i]] += 1
            score_end[teams[j]] += 1

score_end_ans = score_end
# sort score_end by value
score_end = sorted(score_end.items(), key=lambda x: x[1], reverse=True)

# sum value in scores 
for i in range(4):
    x = 0
    for j in range(4):
        x += int(scores[i][j])
    score_team[teams[i]] += x

# check diff
score_diff = {teams[0]: 0, teams[1]: 0, teams[2]: 0, teams[3]: 0}                                       
for i in range(4):
    h = 0
    for j in range(4):
        h += int(scores[j][i])
    score_diff[teams[i]] += score_team[teams[i]] - h

ans = []

# print everthing in score_end
for i in range(4):
    ans.append(score_end[i][0])

for i in range(4):
    for j in range(i,4):
        if score_end[i][0] != score_end[j][0]:
            if score_end[i][1] == score_end[j][1]:
                if score_diff[score_end[i][0]] > score_diff[score_end[j][0]]:
                    continue
                else:
                    a = ans[i]
                    ans[i] = ans[j]
                    ans[j] = a
            

# print all in score_end_ans
for i in range(4):
    print(ans[i], score_end_ans[ans[i]])

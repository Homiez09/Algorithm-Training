D, M = input().split()
# 1 Jan 2009 = thursday

day = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
ans = day[(int(D) + (month[int(M) - 1])) % 7]
print(ans)
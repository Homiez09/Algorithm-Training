totalPoint = 0
for i in range(3):
    totalPoint += int(input())
    
if totalPoint >= 80:
    print("A")
elif totalPoint >= 75:
    print("B+")
elif totalPoint >= 70:
    print("B")
elif totalPoint >= 65:
    print("C+")
elif totalPoint >= 60:
    print("C")
elif totalPoint >= 55:
    print("D+")
elif totalPoint >= 50:
    print("D")
else:
    print("F")
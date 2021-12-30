# A < B < C
# 1 < 3 < 5

number1, number2, number3 = input().split()
alphabet = input()

alphabet = [alphabet[0], alphabet[1], alphabet[2]]
listNum = [int(number1), int(number2), int(number3)]
listNum.sort()

A, B, C = str(listNum[0]), str(listNum[1]), str(listNum[2])
AA, BB, CC = alphabet.index('A'), alphabet.index('B'), alphabet.index('C')
#print(loA, loB, loC)

alphabet.pop(AA)
alphabet.insert(AA, A)
alphabet.pop(BB)
alphabet.insert(BB, B)
alphabet.pop(CC)
alphabet.insert(CC, C)

print(f'{alphabet[0]} {alphabet[1]} {alphabet[2]}')


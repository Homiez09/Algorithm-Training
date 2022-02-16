N, K = input().split(" ")
number = []
prime = []

for i in range(2, int(N)+1):
    number.append(i)
    
while number != []:
    x = number[0]
    count = 0
    while count < len(number):
        if number[count]%x == 0:
            prime.append(number[count])
            number.remove(number[count])
            count = 0
        count += 1

print(prime[int(K)-1])
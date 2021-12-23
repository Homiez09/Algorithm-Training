# A < B < C

# mode => ABC ACB CBA CAB BCA BAC
A, B, C = input().split()
a, b, c = int(A), int(B), int(C)
mode = input()
abc = [a, b, c]
abc.sort()

if mode == "ABC":
    print(*abc, sep = ' ')
elif mode == "CBA":
    abc.reverse
    print(*abc, sep = ' ')
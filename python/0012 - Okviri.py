alp = input()

def out_line(x, alp):
    if x%3 < 2:
        print('..#.', end = '')
    else:
        print('..*.', end = '')
    if x == len(alp)-1:
        print(".")
        
def in_line(x, alp):
    if x%3 < 2:
        print('.#.#', end = '')
    else:
        print('.*.*', end = '')
    if x == len(alp)-1:
        print(".")

def same_line(x, alp):
    if x%3 == 1 or x == 0:
        print(f"#.{alp[x]}.", end='')
    else:
        print(f"*.{alp[x]}.", end='')
    if x == len(alp)-1:
        if x%3 == 2:
            print('*')
        else:
            print('#')
        
for i in range(len(alp)):
    out_line(i, alp)
for i in range(len(alp)):
    in_line(i, alp)
for i in range(len(alp)):
    same_line(i, alp)
for i in range(len(alp)):
    in_line(i, alp)
for i in range(len(alp)):
    out_line(i, alp)
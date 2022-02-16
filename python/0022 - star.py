''' 
input
4
''' 
''' 
output
-*-
*-*
*-*
-*- 
'''
# create a function that takes a number as an argument and prints a square of stars
def star(num):
    for i in range(num):
        print('*' * num)
star(4)

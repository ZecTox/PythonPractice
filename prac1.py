"""Learning Method 1 of input and output in python
"""
    # my_str = input()
    # print(my_str)

    # #taking in a integer n on a single line
    # n = int(input())
    # print(n, end="Test")


'''
2nd method for the input and output

The stdin and stdout

'''

    # import sys

    # my_str = sys.stdin.readline()
    # sys.stdout.write(str(my_str) + "\n")


    # # we can here rename the read and write methods according to our convenience

    # input = sys.stdin.readline
    # output = sys.stdout.write

    # #taking an integer as output

    # my_int = int(input())
    # #sys.stdout.write requires you to format code manually

    # print(str(my_int) + "\n")

'''
we can also use split, map or a list comprehension to read in multiple whitespaces - seperated integer on the same line
'''

# import sys

    # nums = [int(x) for x in input().split()]

    # #this below code also does the same thing

    # nums = list(map(int, input().split()))

    # #if I have to use the stdin/stdout then just replace input() with  sys.stdin.readline()

    # nums = list(map(int, sys.stdin.readline().split()))

# #we can do something similar to the above if we are unpacking  a fixed number of integers

    # n,m = [int(x) for x in input().split]

    # #doing the same thing with map

    # n,m = map(int, input().split())

    # #can also use stdin/stdout also
    # import sys
    # n,m = map(int, sys.stdin.readline().split())

'''
So taking three integers as input and printing their sum is quite simple. On a larger scale(thousands of integers, using stdin and stdout becomes far more imporant for speed)
'''

    # import sys

    # a,b,c = map(int, input().split())
    # print("The sum of these three number is", a+b+c)

    # # we can also implement the same thing using stdin/stdout

    # a, b, c = map(int, sys.stdin.readline().split())
    # sys.stdout.write("The sum of these three number is " + str(a+b+c) + "\n")
    
#Weirds algorith answer, question in usaco

    # hehe = int(input())

    # while hehe > 1:
    #     print(hehe, end=" ")
    #     if hehe % 2 == 0:
    #         hehe //= 2
    #     else:
    #         hehe = (hehe * 3) + 1
    # print(hehe)

'''
FILE I/O 
'''

#Fence painting problem, below is its solution(my logic)

    # a , b = map(int, input().split())
    # c , d = map(int, input().split())

    # ans1 = []
    # ans2 = []

    # for i in range(a,b):
    #     ans1 += [i]

    # for j in range(c,d):
    #     ans2 += [j]

    # ans = ans1+ans2
    # ans = set(ans)

    # print(len(ans))

"""
about whitespaces in python
"""

print(ans, end=" ") #OK, no newline
print(ans) #OK, creates newline
print(str(ans) + "\n", end = " ") #OK, creates newline
print(str(ans) + " ", end = "") #NOT OK, extra space
print(str(ans) + "\n") #NOT OK, extra newline
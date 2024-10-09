"""
INTRODUCTION TO DATA STRUCTURES
"""
    # #i am currently in bronze class

    # #Lists
    # arr = []
    # #lists are generic and can take in any type of data type

    # #lets see a regular for loop 
    # for i in range(1,11): # here we can say that range(i,j), note that range includes i but not j.. it will iterate till j-1 only.
    #     arr.append()


    # #in array we can also give a dynamic array an initial size. THe below code creates a dynamic array with 30 zeroes.

    # arr = [0] * 30

"""
ITERATING
"""

# we can use a normal for loop to iterate through all the elements

    # arr = [1,2,3,4,5]
    # for i in range(len(arr)):
    #     print(arr[i], end=" ")

    # print()

    # #also
    # for elements in arr:
    #     print(elements, end=" ")

#we can also use iterators. an iterator allows you to traverse a container by pointing to an object within the container. "iter(arr)" returns an iterator pointing to the first element of the list arr.

    # arr = [4,2,0,0,5]
    # it = iter(arr)
    # print(next(it)) #will print 4
    # print(next(it)) #will print 2
    # print(next(it)) #will print 0

"""

INSERTING AND ERASING

"""

    # arr = []
    # arr.append(1)
    # arr.append(2)
    # arr.append(3)
    # arr.append(4)
    # arr.append(5)
    # print(arr)
    # arr[1] = 4 # this will set the element on the index 1 as 4
    # arr.pop(1) #this will remove the element at index 1, so the list will be [1,3,4,5]
    # #this methos is O(n), to be avoided.
    # arr.append(9)
    # print(arr)
    # arr.pop()
    # print(arr)
    # arr.append(6)
    # arr.append(7)
    # arr.append(8)
    # arr.append(9)
    # print(arr)
    # print(arr[2])
    # arr = arr[3:] #it erases the  first 3 elements while printing
    # print(arr)

"""

LIST COMPREHENSION

"""

    # old_list = [2,5,3,1,6]
    # new_list = []

    # for i in old_list:
    #     if i % 2 == 1:
    #         new_list.append(i*2)
    # print(new_list)
    # #simplified with one liner with list comperehension
    # #recall the form [expression for item in list if conditional]
    # #expression : i * 2
    # #list : old_list
    # #conditional: i % 2 == 1 (only include item i if satisfies the conditional)
    # new_list = [i*2 for i in old_list if i%2==1] #need to learn to write such small hacks in python
    # print(new_list) 
""" what i have written in one liner is called list comprehension and its useful"""

# A very applicable use for of list comprehensions for competitive programming in particular is creating an integer list from space seperated input

    # arr = [int(x) for x in input().split()]
    # print(arr)

"""
PAIRS IN PYTHON
"""
# if we want to store a collection of points on the 2D plane, then we can use a dynamic array of pairs
# while python doesnt have a specific class just for pairs, 2-element tuples give nearly the exact functionality. The only issue is that you cant modify the elements since tuples are immutable
#on the other hand, python has built-in comparison support for tuples. When comparing, it looks at the first element of the pair, then the second, and so on and so forth.


    # p1 = (5, "asdf") #this is a tuple and its created using normal brackets
    # print(p1)
    # print(p1[0])

    # p2 = (6, "asdf") #this is a tuple and its created using normal brackets
    # print

""""
MEMORY ALLOCATION
"""

#one thing to keep in mind is when using arrays is the memory limit. so if a question has 256mb of memory limit. 
#1) calculate it in bytes ->  256 * 10^6
#2) divide by the size, in bytes of an int(4 bytes) or a long lond(in c++) 
# for example the number of int "S" that is that you are able to store is bounded above by 
# (256 * 10^6)/4 = 64 * 10^6


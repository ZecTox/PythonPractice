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

arr = [4,2,0,0,5]
it = iter(arr)
print(next(it)) #will print 4
print(next(it)) #will print 2
print(next(it)) #will print 0

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


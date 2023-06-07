'''
Write a function which will take an array of numbers and return the number most repeated in the
array with how many times it was repeated. For example, if the array is
[4,3,5,6,4,7,9,2,4,6,3,4,6,3,4,8,5,1,5] the function should return 4 is repeated 5 times.'''

'''
Pseudocode: 
1: using dictionary Data structure
-- make a dictionary from the list elements, for example: if a new number is encountered, push it into the dict
   and set the value to 1, and if the list element is already present in dict, then increment it by one
-- once a dict from the given list is obtained, find the largest value among all the key, value pairs in the 
   dictionary
'''


def findMaxOccured(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict.keys():
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    largest = 0
    key = 0
    for k, v in count_dict.items():
        if v > largest:
            largest = v
            key = k
    return str(key) + " is repeated " + str(largest) + " times"

arr = [4,3,5,6,4,7,9,2,4,6,3,4,6,3,4,8,5,1,5]
print(findMaxOccured(arr))
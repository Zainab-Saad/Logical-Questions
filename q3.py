'''
Write a function which will take an array as input and return the sum of two largest numbers in a n
array. For example, in array [3,7,1,5,11,19] the result would be 30 because 11 and 19 are largest
numbers.'''
'''
1: Brute force:
loop once and find the two largest numbers. it does the task in linear time complexity
2: Sort the array and then pick the last two numbers:
sorting in general takes nlog(n) time and in worst case can be O(n^2), so it is not the optimal solution
'''

def sumOfLargest(arr):
    largest, sec_largest = arr[0], arr[0]
    # start from index 1 instead of 0
    for num in arr[1:]:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num > sec_largest:
            sec_largest = num
    return largest + sec_largest 

arr = [3, 7, 1, 5, 11, 19]
print(sumOfLargest(arr))


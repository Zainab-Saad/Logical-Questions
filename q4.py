'''
Write a function which will take an array as input and return an array with every missing element
from 0 to highest entry. For example, in an array [3,4,9,1,7,3,2,6] the highest entry is 9 and missing
numbers are [0,5,8]'''

'''
1: Through sorting:
pseudocode:
-- sort the given array [1, 2, 3, 4, 6, 7, 9]
-- loop through the sorted array and check if there are any digits missing between consecutive indexes
-- Dry run: 
--- arr[0] = 1, return 0 because there is only one digit 0 in between 0 and 1 not present in the array
--- arr[1] - arr[3], all consecutive digits present
--- arr[4] = 6, arr[3] = 4 and arr[4] = 6 so one digit 5 is missing
--- arr[5], consecutive digit present
--- arr[6] = 9, arr[5] = 7 and arr[6] = 9, one digit is missing in between
--- returned = [0, 5, 8]
'''

def selectionSort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            temp = arr[min]
            arr[min] = arr[i]
            arr[i] = temp
    return arr


def findMissing(arr):
    arr = selectionSort(arr)
    missing = []
    # run the loop highest number times
    num, i = 0, 0
    while(num < arr[len(arr)-1]):
        if arr[i] <= num:
            i+= 1
        else:
            missing.append(num)
        if num > 0 and arr[i] == arr[i-1]:
            continue
        num += 1
    return missing


arr = [3,4,9,1,7,3,2,6]
print(findMissing(arr))



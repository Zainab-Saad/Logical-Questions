'''
Write a function which will take an array as input, sort and return the array in descending order. For
example, if the array is [3,2,7,4,6,9] the result should be [9,7,6,4,3,2].'''

'''
Any sorting algorithm such as merge sort, quick sort, insertion sort can be modified to sort the elements in 
descending order.
If we take merge sort as our sorting algorithm, the steps would be as follows
-- recursively divide the array into smaller arrays 
-- when combining the smaller arrays into bigger one, put elements in descending order

Dry run:
--- given array [3, 2, 7, 4, 6, 9]
--- recursively divide the array into smaller arrays as
__Dividing__
[3, 2, 7] , [4, 6, 9]
[3, 2] , [7] , [4, 6], [9]
[3], [2], [7], [4], [6], [9]
__Combining__
[3, 2], [7], [6, 4], [9]
[7, 3, 2], [9, 6, 4]
[9, 7, 6, 4, 3, 2] ---> reverse sorted array
'''

def merge(arr, left, mid, right):
    left_subarray = [0] * (mid-left+1)
    right_subarray = [0] * (right-mid)
    
            
    for i in range(0, (mid-left+1)):
        left_subarray[i] = arr[left+i]
    
    for i in range(0, (right-mid)):
        
        right_subarray[i] = arr[mid+i+1]

    left_subarray_ptr, right_subarray_ptr = 0, 0
    merged_array_ptr = left
    
    while left_subarray_ptr < (mid-left+1) and right_subarray_ptr < (right-mid):
        if left_subarray[left_subarray_ptr] >= right_subarray[right_subarray_ptr]:
            arr[merged_array_ptr] = left_subarray[left_subarray_ptr]
            left_subarray_ptr += 1
        else:
            arr[merged_array_ptr] = right_subarray[right_subarray_ptr]
            right_subarray_ptr += 1
        merged_array_ptr += 1
        
    while left_subarray_ptr < (mid-left+1):
        arr[merged_array_ptr] = left_subarray[left_subarray_ptr]
        merged_array_ptr += 1
        left_subarray_ptr += 1
        
    while right_subarray_ptr < (right-mid):
        arr[merged_array_ptr] = right_subarray[right_subarray_ptr]
        right_subarray_ptr += 1
        merged_array_ptr += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left+right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)
    
arr = [3,2,7,4,6,9]
mergeSort(arr, 0, len(arr)-1)

print('Reverse Sorted array is', arr)
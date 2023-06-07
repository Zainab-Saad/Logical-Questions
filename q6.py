'''
Write a function which will take an array as input, it will rotate the array to the right 1 time and
return the rotated array. Rotation of the array means that each element is shifted right by one index. For
example, the rotation of array A = [3,8,9,7,6] is [6,3,8,9,7].'''

def rotateArray(arr):
    length = 0
    for i in arr:
        length += 1
    temp, temp_2 = arr[0], arr[0]
    for i in range(0, length):
        temp_2 = arr[(i+1)%length]
        arr[(i+1)%length] = temp
        temp = temp_2
    return arr

arr = [3, 8, 9, 7, 6]
print(rotateArray(arr))
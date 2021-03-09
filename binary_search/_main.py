
arr = [2,3,5,8,10,11,15]  # last postion: six 


def binary_search(arr, target): 
    left = 0 # position of the first el in the array
    right = len(arr) - 1 # the position of the last element in the array
    while arr[left] <= arr[right]:
        mid = (left + right ) // 2 # rounded value
        if arr[mid] > target:
            # the mid el is greater than the target, set right value to the left value
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:  # arr[mid] = target
            return mid
    return -1

print(binary_search(arr, 15))
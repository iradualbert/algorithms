arr = [2,3,5,8,10, 11,15, 18, 20, 21, 23]

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while(left <= right):
        midpoint = (left + right) // 2
        
        if(arr[midpoint] == target):
            return midpoint
        
        elif arr[midpoint] > target:
            right = midpoint - 1
            
        else:
            left = midpoint + 1
            
    return -1

print(binary_search(arr, 5)) #2
print(binary_search(arr, 9)) # -1
print(binary_search(arr, 15)) # 6


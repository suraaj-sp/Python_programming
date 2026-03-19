def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
        elif arr[i] < arr[i-1]:
            increasing = False
    return increasing or decreasing

print(is_monotonic([1,2,3,4,5]))
print(is_monotonic([5,4,3,2,1]))
print(is_monotonic([1,3,4,2,4,5,4,3,2]))


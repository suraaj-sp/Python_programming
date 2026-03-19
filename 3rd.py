def rotate_array(arr,d):
    if d<0 or d>=len(arr):
        return "Invalid rotation value"
    
    rotated_arr = [0] * len(arr)
    for i in range(len(arr)):
        rotated_arr[i] = arr[(i+d)%len(arr)]
    return rotated_arr
print(rotate_array([1,2,3,4,5],2))


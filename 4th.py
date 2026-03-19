def split_and_add(arr,c):
    if c<0 or c>=len(arr):
        return arr
    first_part = arr[:c]
    second_part = arr[c:]
    result = second_part+first_part
    return result
print(split_and_add([1,2,3,4,5],3))
    


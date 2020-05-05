

def insert_element(arr, pos, ele):
    if pos < 0:
        return arr
    if pos > len(arr):
        return arr
    arr.append(arr[-1])
    for i in range(len(arr)-1, -1, -1):
       arr[i] = arr[i-1]
       if i == pos:
           arr[pos] = ele
           break
    return arr


arr = insert_element([4,6,8,2], 3, 0)
print(arr)


def remove_element(arr, pos):
    if  pos < 0:
        return arr
    if pos >= len(arr):
        return arr
    for i in range(pos, len(arr) -1):
        arr[i] = arr [i+1]

    arr = arr[:-1]
    return arr

arr = remove_element([1,2,3,4], 4)
print(arr)
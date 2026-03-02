def count_recursive(arr):
    if len(arr) == 1:
        return 1
    else:
        arr.pop(0)
        count = 1 + count_recursive(arr)
        return count
    
print(count_recursive([1, 2, 3, 4, 5, 6]))


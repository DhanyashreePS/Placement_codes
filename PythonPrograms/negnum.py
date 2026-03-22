def first_negative(arr):
    for num in arr:
        if num < 0:
            return num
    return None
arr = [5, 3, -2, 7, -8]
print(first_negative(arr))
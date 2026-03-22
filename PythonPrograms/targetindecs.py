def find_indices(arr,target):
    result=[]
    for i in range(len(arr)):
        if arr[i]==target:
            result.append(i)
    return result
arr=[1,4,2,4,5,4]
target=4
print(find_indices(arr,target))
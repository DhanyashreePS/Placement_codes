def find_ceiling(arr,target):
    left=0
    right=len(arr) - 1
    ceiling=None

    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            left=mid+1
        else:
            ceiling=arr[mid]
            right=mid-1
    return ceiling
arr=[2,5,8,10]
target=7
print(find_ceiling(arr,target))
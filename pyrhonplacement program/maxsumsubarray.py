#to find max sum with the help of all possible subarrays and subarray size should be 3.
#[1,5,6,7,8,9]
def subsum(arr,k):
    window=sum(arr[:k])
    max1=window
    for i in range(k,len(arr)):
        window+=arr[i]-arr[i-k]
        max1=max(window,max1)
    return max1
arr=[1,5,6,7,8,9]
k=3
print(subsum(arr,k))


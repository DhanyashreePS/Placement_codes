class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        i=0
        while(i<len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k+=1
            i+=1
        return k
# Create object
sol = Solution()

# Input
nums = [3, 2, 2, 3]
val = 3

# Call function
k = sol.removeElement(nums, val)

# Output
print("k =", k)
for i in range(k):
    print(nums[i])
#print("updated nums",nums[:k])
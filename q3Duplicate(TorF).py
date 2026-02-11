arr=[1,4,7,3,1,4]
new_arr=[]
for num in arr:
    if(num not in new_arr):
        new_arr.append(num)
print(new_arr)

#2nd method
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l1=len(nums)
        s1=set(nums)
        l2=len(s1)
        if(l1!=l2):
            return True
        else: 
            return False

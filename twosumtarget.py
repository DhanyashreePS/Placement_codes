class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while(i<j):
            cursum=numbers[i]+numbers[j]
            if(cursum==target):
                return [i+1,j+1]
            elif cursum<target:
                i+=1
            else:
                j-=1
        return []
numbers=[1,2,4,6]
target=5
sol=Solution()
print(sol.twoSum(numbers,target))

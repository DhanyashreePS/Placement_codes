class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)
        while(i<j):
            if(numbers[i]+numbers[j]==target):
                res=i+1,j+1
                return list(res)
                j-=1
            i+=1
numbers=[1,2,4,6,2]
target=5
sol=Solution()
solution=sol.twoSum(numbers,target)
print(solution)

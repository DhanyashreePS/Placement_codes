#check whether the string is palindrome or not
"""def palin(str1):
    i=0
    j=len(str1)-1
    while i<j:
        if str1[i]==str1[j]:
            return True
        else:
            return False
        i+=1
        j-=1
str1="mom"
res=palin(str1)
if res==True:
    print("palindrome")
else:
    print("not")"""
#linkedIn,flipkart,microsoft,amazon,google,expedia asked this
#dry and run table
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

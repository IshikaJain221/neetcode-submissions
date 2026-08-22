class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        
        temp=1
        for i in range(1,len(nums)):
            temp=temp*nums[i-1]
            prefix.append(temp)
        
        temp=1
        for j in range(len(nums)-2,-1,-1):
            temp=temp*nums[j+1]
            suffix.append(temp)
        suffix.reverse()
        res=[]
        for k in range(len(nums)):
            res.append(prefix[k]*suffix[k])
        return res

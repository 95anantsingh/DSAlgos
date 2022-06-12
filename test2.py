List =list
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        maxsum = 0
        csum = 0
        numdict = {}
        
        for i in range(len(nums)):
            csum += nums[i]
            if nums[i] in numdict:
                maxsum = max(csum - numdict[nums[i]], maxsum)    
            numdict[nums[i]] = csum
            
        return maxsum



L = [4,2,4,5,6]
obj = Solution()
res = obj.maximumUniqueSubarray(L)

print(res)
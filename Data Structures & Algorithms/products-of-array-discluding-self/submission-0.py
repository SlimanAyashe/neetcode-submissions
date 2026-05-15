class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        prior = [1] * nums_length
        after = [1] * nums_length
        for i in range(1, nums_length):
           prior[i] = prior[i-1] * nums[i-1] 
        
        for i in range(nums_length-2,-1,-1):
            after[i] = after[i+1] * nums[i+1]
        result = []
        for i in range(nums_length):
            result.append(prior[i] * after[i])
        return result
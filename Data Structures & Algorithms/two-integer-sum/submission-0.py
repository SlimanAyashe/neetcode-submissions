class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for  i,j in enumerate(nums): 
            if j in seen:
                return [seen[j],i]
            seen[target-j] = i
        return None
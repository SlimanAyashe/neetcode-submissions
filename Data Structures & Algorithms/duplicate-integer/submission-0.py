class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums:
            if not str(num) in numsDict.keys():
                numsDict[str(num)]=1
            else:
                return True
        return False 
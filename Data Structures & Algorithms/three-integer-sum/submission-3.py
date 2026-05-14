class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        seen = set()
        used_pairs = set()  # To prevent returning the same pair twice
        lists = []
        for num in nums:
            complement = target - num
            if complement in seen:
                # We found a pair. We use a sorted tuple to ensure [1, -1] 
                # and [-1, 1] are treated as the same duplicate.
                pair = tuple(sorted([num, complement]))
                if pair not in used_pairs:
                    lists.append([num, complement])
                    used_pairs.add(pair)
            
            # Change: Add the current number to seen, not the target-num
            seen.add(num) 
        return lists

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. You MUST sort the array for the duplicate skipping logic to work
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # 2. Skip the same number to avoid duplicate triplets in the result
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Your slicing logic
            temp = self.twoSum(nums[i+1:], -1 * nums[i])
            
            if temp:
                for arr in temp:
                    result.append([nums[i]] + arr)
        return result
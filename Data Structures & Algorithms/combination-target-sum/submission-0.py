class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start_index: int, current_combination: List[int], current_sum: int):
            # Base Case 1: Found a valid combination
            if current_sum == target:
                result.append(list(current_combination))  # Simple shallow copy [:] is enough
                return
            
            # Base Case 2: Exceeded target sum
            if current_sum > target:
                return
            
            # Loop through choices starting from start_index to prevent reverse-order duplicates
            for i in range(start_index, len(nums)):
                current_combination.append(nums[i])
                
                # Pass 'i' instead of 'i + 1' because we can reuse the same number
                backtrack(i, current_combination, current_sum + nums[i])
                
                current_combination.pop()  # Backtrack and clean up

        backtrack(0, [], 0)
        return result
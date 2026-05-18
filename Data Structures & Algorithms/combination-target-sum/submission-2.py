class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums_length = len(nums)
        def backtrack(index: int, current_permutation: list[int], current_sum):
            #base cases
            if current_sum > target:
                return
            if current_sum == target:
                result.append(list(current_permutation))
                return

            #main backtracking logic
            for i in range(index, nums_length):
                temp = nums[i]
                current_permutation.append(temp)
                backtrack(index,current_permutation,current_sum + temp)
                index += 1
                current_permutation.pop()
        backtrack(0,[],0)
        return result

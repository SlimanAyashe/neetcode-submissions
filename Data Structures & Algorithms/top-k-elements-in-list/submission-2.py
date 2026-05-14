class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for i in range(-1000,1001, 1):
            arr[i] = 0 
        for num in nums:
            arr[num] += 1
        sorted_arr = sorted(arr.items(), key = lambda x :x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(sorted_arr[i][0])
        return result
        

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = [-1*num for num in nums]
        heapq.heapify(temp)
        for _ in range(k-1):
            heapq.heappop(temp)
        return -1 * heapq.heappop(temp)
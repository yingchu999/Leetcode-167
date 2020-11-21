# Given an integer array. Find the kth smallest distance between all the pairs.
# The difference of a pair is the absolute difference between two elements.

# Solutions:
# 1. Heap
# Time complexity is O((k+n)logn), where k =O(n^2). So time complexity is O(n^2logn) in the worst case.
# The time complexity is added by heap operation O(klogn+n) and sort operation is O(nlogn)
# Space complexity is O(n)
from heapq import heappop, heappush
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(n - 1)]
        heapify(heap)

        for _ in range(k):
            d, root, nei = heappop(heap)
            if nei + 1 < n:
                heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))

        return d
      
# 2. Binary search
# First, sort the array.
# The distance between two elements is in the range of [0,nums[-1]-nums[0]]
# Then create a function to calculate the number of pairs whose distance is less than given value.
# Time complexity is O(NlogW+NlogN), W is equal to nums[-1]-nums[0]. Space complexity is O(1).
def count(value):
  count = left = 0
  for right,num in emunerate(nums):
    while num-nums[left]>value:
      left += 1
    count += right-left
  return count >= k

nums.sort()
lo = 0
hi = nums[-1]-nums[0]
while lo<hi:
  mid = (lo+hi)//2
  if count(mid):
    hi = mid
  else:
    lo = mid+1
return lo


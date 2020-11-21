# Given an integer array. Find the kth smallest distance between all the pairs.
# The difference of a pair is the absolute difference between two elements.

# Solutions:
# 1. Heap
# Time complexity is O((k+n)logn), where k =O(n^2). So time complexity is O(n^2logn) in the worst case.
# The time complexity is added by heap operation O(klogn+n) and sort operation is O(nlogn)
# Space complexity is O(n)


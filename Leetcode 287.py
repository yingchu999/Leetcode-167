# Given an array of integers containing n+1 elements in the range of [1,n] inclusive.
# There is only one duplicate number in the array. But this duplicate number may duplicate several times.
# Return the duplicate number.

# Solution:
# 1. Dictionary
# First I thought we can solve this problem using dictionary.
# Go through the whole array. If the current_element not in the dictionary A, then A[current_element]=1.
# If the current_element is already in the dictionary, then return the current_element.
# The time complexity is O(n) and the space complexity is O(n).

dic={}
  for num in nums:
      if num not in dic:
          dic[num] = 1
      else:
          return num
          
# 2. Sorting
# First sort the array.
# Then if any current_element is the same with the previous_element, return the current_element.
# Time complexity is O(nlogn) and space complexity is O(1) or O(n).
# Here we sort the array in place, so the space complexity is O(1). 
# But if we need to copy the array then space complexity is O(n)

nums.sort()
for i in range(1,len(nums)):
  if nums[i] == nums[i-1]:
    return nums[i]
    
# 3. Tortoise and hare
# Since the length of array is n+1 and the element is in the range of [1,n], so each element can represent a index of the array.
# Let's create a circle using function F(x) = nums[x].
# So the sequence will be x, nums[x], nums[nums[x]], nums[nums[nums[x]]]....
# Each new element in the sequence is an element in nums at the index of previous element.
# IF there are any duplicates, there will be a circle.
# Here we set two pointers tortoise and hare. Tortoise is slower than hare.
# If tortoise is twice slower than hare, then 2(F+a) = F+a+C.
# So F = C-a
# First, find the intersection.
# Second, tortoise start from 0 and hare start from intersection. After F steps they will meet at intersection.
# Last, return the intersection.
# Time complexity is O(n) and space complexity is O(1)

tortoise, hare = nums[0], nums[0]
while true:
  tortoise = nums[tortoise]
  hare = nums[nums[hare]]
  if tortoise == hare:
    break
tortoise = nums[0]

while tortoise != hare
  tortoise = nums[tortoise]
  hare = nums[hare]

return tortoise

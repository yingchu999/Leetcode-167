left = 0
maxi = -1
cur = 0
total = sum(nums)
for right in range(len(nums)):
    cur += nums[right]
    while cur > total - x and left <= right:
        cur -= nums[left]
        left += 1
    if cur == total-x:
        maxi = max(maxi, right-left+1)
return len(nums)-maxi if maxi != -1 else -1

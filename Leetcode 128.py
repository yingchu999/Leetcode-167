# Approach 1: Hashset

if not nums:
    return 0
S = set(nums)
count = 1
m = float('-inf')
for s in S:
    if s-1 not in S:
        cur = s
        count = 1
        while cur+1 in S:
            cur += 1
            count += 1
        m = max(m, count)
return m


# Approach 2: Sort

if not nums:
    return 0
if len(nums) == 1:
    return 1
nums.sort()
count = 1
m = float('-inf')
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        if nums[i] == nums[i+1]-1:
            count += 1
        else:
            m = max(m, count)
            count = 1
return max(m,count)

# Approach 1: Two pointers

left, right = 0, len(height)-1
left_max, right_max = float('-inf'), float('-inf')
count = 0
while left < right:
    if height[left] < height[right]:
        if height[left] > left_max:
            left_max = height[left]
        count += left_max - height[left]
        left += 1
    else:
        if height[right] > right_max:
            right_max = height[right]
        count += right_max - height[right]
        right -= 1
return count

# Approach 2: DP

left,right = [0]*len(height),[0]*len(height)
left_max,right_max = float('-inf'),float('-inf')
length = len(height)
for i in range(length-1, -1, -1):
    if height[i] > right_max:
        right_max = height[i]
    right[i] = right_max
for i in range(length):
    if height[i] > left_max:
        left_max = height[i]
    left[i] = left_max
count = 0
for i in range(length):
    count += min(left[i],right[i]) - height[i]
return count

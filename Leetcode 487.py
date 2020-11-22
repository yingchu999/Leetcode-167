# Given a binary array.
# Find the maximum number of consecutive 1s in this array if you can flip at most one 0.
# Go through the whole array.
# If element is 1, count+1.
# If element is 0, pre=count and count=0.
# Result=is max(Result,pre+1+count)
# Time complexity is O(n), space complexity is O(1).
pre,count,res = -1,0,0
for i in range(len(nums)):
  if nums[i] == 0:
    pre,count=count,0
  else:
    count+=1
  res = max(res,pre+1+count)
return res

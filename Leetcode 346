# Given a stream of integers and a window size.
# Calculate the average of all the integers in the sliding window.
# Time complexity is O(1) and space complexity is O(N), N is the size of the window.
pre,count,res = -1,0,0
  for i in range(len(nums)):
      if nums[i] == 0:
          pre,count=count,0
      else:
          count+=1
      res = max(res,pre+1+count)
  return res

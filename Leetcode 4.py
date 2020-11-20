# Two arrays of integers in ascending order of size m and n, respectively.
# Return the median of two sorted arrays.
# To find the median of a set, means to seperate the set into two equal length subsets and one subset is always larger than the other.
# Suppose we seperate the two arrays at index i and j, where 0<=i<=m and 0<=j<=n.
# To satisfy the requirement, i+j=m-i+n-j+1 or m-i+n-j.
# Therefore, j = (m+n+1)/2-i and n>=m.
# Here we set n>=m. Because if m>n, j could be negative. So if m>n, we change the two arrays.
# Then the two arrays have been seperated to four subarrays.
#   A[0]...A[i-1],  A[i]...A[m]
#   B[0]...B[j-1],  B[j]...B[n-1]
# There are three requirements that have to be satisfied:
# 1. j = (m+n+1)/2-i
# 2. A[i]>B[j-1] 
# 3. B[j]>A[i-1]
# If all the requiremtns are satisfied, then max(A[i-1],B[j-1]) is returned if m+n is odd or (max(A[i-1],B[j-1])+min(A[i],B[j]))/2 is returned.
# What if i=0 or m and j=0 or n?
# If m+n is odd, we only need to know the max(A[i-1],B[j-1]). If i = 0, then return B[j-1]. If j = 0, then return A[i-1].
# If m+n is even, we need to know both max(A[i-1],B[j-1]) and min(A[i],B[j]). We have already known max(A[i-1],B[j-1]). So we need to know the next one.
# If i=m, then min(A[i],B[j])=B[j]. If j=n, then min(A[i],B[j])=A[i]
# Last, return (max(A[i-1],B[j-1])+min(A[i],B[j]))/2

m,n = len(nums1),len(nums2)
  if m>n:
      nums1,nums2,m,n = nums2,nums1,n,m

  imin, imax = 0, m
  while imin<=imax:
      i = (imin+imax)//2
      j = (m+n+1)//2-i
      if i<m and nums1[i]<nums2[j-1]:
          imin = i+1
      elif i>0 and nums1[i-1]>nums2[j]:
          imax = i-1
      else:
          if i == 0:
              left = nums2[j-1]
          elif j == 0:
              left = nums1[i-1]
          else:
              left = max(nums1[i-1],nums2[j-1])
          if (m+n)%2==1:
              return left
          if i == m:
              right = nums2[j]
          elif j == n:
              right = nums1[i]
          else:
              right = min(nums1[i],nums2[j])
          return (left+right)/2

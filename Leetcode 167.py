#This problem is about an array of intergers that is already sorted in ascending order. 
#Find two numbers such that they add up to a specific target. 
#Should return indexes of two numbers and index 1 should be less than index 2.
#Return indexes are not zero_based.
#Only one solution and may not use the same element twice.
          
#This problem has two solutions:
#1.
#Set a dictionary A. Go through the list. 
#Using target minus current element.
#If the difference is not in the dictionary, A[current_element] = current_index. 
#If the difference is already in the dictionary, result = [A[difference]+1,current_index+1]
#Time complexity: O(n), Space complexity: O(n)

search = {}
for i, num in enumerate(numbers):
  if target - num in search:
    return [search[target-num]+1, i+1]
  else:
    search[num] = i

#2. Binary search
#Set two pointers at the most left (0) and most right of the list (len(list)-1).
#While left_pointer is less than len(list)-1, 
#if list[left_pointer) + list[right_pointer] < target, than move right_pointer to the left,
#if list[left_pointer) + list[right_pointer] = target, than return the result = [left_pointer+1, right_pointer+1],
#if list[left_pointer) + list[right_pointer] > target, than move left_pointer to the right.
#Time complexity: O(n), Space complexity: O(1)

i,j = 0,len(numbers)-1
  while i < len(numbers):
      if numbers[i] + numbers[j] < target:
          i += 1
      elif numbers[i] + numbers[j] > target:
          j -= 1
      else:
          return(i+1, j+1)
          

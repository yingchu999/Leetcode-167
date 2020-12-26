left, right = 0, len(seats)-1
left_cnt, right_cnt = 0,0
max_ = float('-inf')
max__ = float('-inf')
while seats[left] == 0:
    left_cnt += 1
    left += 1
while seats[right] == 0:
    right_cnt += 1
    right -= 1
max_ = max(left_cnt, right_cnt)
while left<right:
    left += 1
    right -= 1
    left_cnt, right_cnt = 0,0
    while seats[left] == 0:
        left_cnt += 1
        left += 1
    while seats[right] == 0:
        right_cnt += 1
        right -= 1
    max__ = max(max__, (left_cnt+1)//2, (right_cnt+1)//2)
return max(max_, max__)

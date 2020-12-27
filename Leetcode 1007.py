# Approach 1

res = 0
for num in [A[0], B[0]]:
    for i in range(len(A)):
        if num != A[i] and num != B[i]:
            break
        if i == len(A)-1 and (num == A[i] or num == B[i]):
            res = num
    if res != 0:
        break
count_a, count_b = 0,0
for num in A:
    if num == res:
        count_a += 1
for num in B:
    if num == res:
        count_b += 1
return min(len(A)-count_a, len(B)-count_b) if res != 0 else -1

# Ajusted

res = float('inf')
m = float('inf')
for num in [A[0], B[0]]:
    count_a, count_b = 0, 0
    for i in range(len(A)):
        if num != A[i] and num != B[i]:
            break
        elif num != A[i]:
            count_a += 1
        elif num != B[i]:
            count_b += 1
        if i == len(A)-1:
            res = min(count_a, count_b)
return res if res != float('inf') else -1

# Approach 2:

def check(x):
    rotations_a = rotations_b = 0
    for i in range(n):
        # rotations coudn't be done
        if A[i] != x and B[i] != x:
            return -1
        # A[i] != x and B[i] == x
        elif A[i] != x:
            rotations_a += 1
        # A[i] == x and B[i] != x    
        elif B[i] != x:
            rotations_b += 1
    # min number of rotations to have all
    # elements equal to x in A or B
    return min(rotations_a, rotations_b)

n = len(A)
rotations = check(A[0]) 
# If one could make all elements in A or B equal to A[0]
if rotations != -1 or A[0] == B[0]:
    return rotations 
# If one could make all elements in A or B equal to B[0]
else:
    return check(B[0])

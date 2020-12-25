d={}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i + j not in d:
            d[i+j] = [matrix[i][j]]
        else:
            d[i+j].append(matrix[i][j])
ans= []
for entry in d.items():
    if entry[0] % 2 == 0:
        ans += entry[1][::-1]
    else:
        ans += entry[1]
return ans

row_a, col_a = len(A), len(A[0]) 
row_b, col_b = len(B), len(B[0])
C = [[0 for _ in range(col_b)] for _ in range(row_a)]
for i,row in enumerate(A):
    for k,elea in enumerate(row):
        for j, eleb in enumerate(B[k]):
            C[i][j] += elea*eleb
return C

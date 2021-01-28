mod = 10**9+7
res = ''
for i in range(1,n+1):
    res += bin(i)[2:]
return int(res,2) % mod

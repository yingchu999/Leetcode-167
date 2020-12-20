dic = collections.defaultdict(int)
start = 0
res = 0
for i in range(len(s)):
    dic[s[i]] += 1
    while len(dic)>k:
        dic[s[start]]-=1
        if dic[s[start]] == 0:
            del dic[s[start]]
        start += 1
    res = max(res, i-start+1)
return res

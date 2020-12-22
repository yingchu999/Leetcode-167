dic = collections.defaultdict(int)
start = 0
res = float('-inf')
for i, cha in enumerate(s):
    dic[cha] += 1
    while len(dic) > 2 and start <len(s):
        dic[s[start]] -= 1
        if dic[s[start]] == 0:
            del dic[s[start]]
        start += 1
    res = max(res, i-start+1)
return res if res != float('-inf') else 0

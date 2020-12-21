if not s or not t:
    return ''
dic = Counter(t)
require = len(dic)
form = 0
check = collections.defaultdict(int)
l, r = 0,0
ans = (float('inf'), None,None)
while r < len(s):
    check[s[r]] += 1
    if s[r] in dic and check[s[r]] == dic[s[r]]:
        form += 1
    while l<=r and form == require:
        if r-l+1<ans[0]:
            ans = (r-l+1,l,r)
        check[s[l]] -= 1
        if s[l] in dic and check[s[l]]<dic[s[l]]:
            form -= 1
        l +=1
    r += 1
return '' if ans[0]==float('inf') else s[ans[1]:ans[2]+1]

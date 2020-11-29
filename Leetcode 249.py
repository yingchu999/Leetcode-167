# key is the difference between adjcent element.
# difference first add 26 then % 26.
# dictionary.get(key,value): if key not exist, return value.

dic = {}
for string in strings:
    key = ()
    for i in range(len(string)-1):
        difference = 26+ord(string[i+1])-ord(string[i])
        key += (difference%26,)
    dic[key] = dic.get(key,[])+[string]
return dic.values()

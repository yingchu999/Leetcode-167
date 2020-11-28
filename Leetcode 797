# Time complexity is O(2^N * N) and space complexity is O(2^N * N).
length=len(graph)-1
res = []

def dfs(value,temp):
    if value == length:
        res.append(list(temp))
        return
    for next in graph[value]:
        temp.append(next)
        dfs(next,temp)
        temp.pop()

temp = [0]
dfs(0,temp)
return res


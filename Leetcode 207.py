# This is a graph problem.
# Here I use DFS to solve this problem.
# Time complexity is O(|V|+|E|) and space complexity is O(|V|+|E|) where V is number of courses and E is the number of dependencies.

self.check = [0 for _ in range(numCourses)]
self.dic = collections.defaultdict(list)
for pre in prerequisites:
    self.dic[pre[0]].append(pre[1])
print(self.dic)
res = True
for i in range(numCourses):
    res = self.dfs(i)
    if res is not True:
        return False
return True



def dfs(self,course):
    if self.check[course] == -1:
        return False
    elif self.check[course] == 1:
        return True
    self.check[course] = -1
    List = self.dic[course]
    res = []
    while List:
        pre = List.pop()
        res.append(self.dfs(pre))
    self.check[course] = 1
    if res == []:
        return True
    else:
        return all(res)

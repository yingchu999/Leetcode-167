class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        dic = collections.defaultdict()
        def dfs(value):
            List = graph[value]
            for num in List:
                if num in dic:
                    if dic[num] == dic[value]:
                        return False
                else:
                    dic[num] = dic[value]*(-1)
                    if not dfs(num):
                        return False
            return True
        
        for i in range(len(graph)):
            if i not in dic:
                dic[i] = 1
                if not dfs(i):
                    return False
        return True

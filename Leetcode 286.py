# BFS
# Search for the 0 point, then append the around four points into the queue.
# Then continue to pop the front element and append the surround fout points into the queue.

if not rooms:
    return []
m = len(rooms)
n = len(rooms[0])
for i in range(m):
    for j in range(n):
        if rooms[i][j] == 0:
            queue = collections.deque()
            queue = self.A(i,j,1,m,n,queue)
            see = set()
            while queue:
                a,b,val = queue.popleft()
                if rooms[a][b] in [0,-1] or (a,b) in see:
                    continue
                rooms[a][b] = min(rooms[a][b],val)
                see.add((a,b))
                queue = self.A(a,b,val+1,m,n,queue)
                        
def A(self,i,j,val,m,n,queue):
    if i+1<m:
        queue.append((i+1,j,val))
    if j+1<n:
        queue.append((i,j+1,val))
    if i-1>=0:
        queue.append((i-1,j,val))
    if j-1>=0:
        queue.append((i,j-1,val))
    return queue

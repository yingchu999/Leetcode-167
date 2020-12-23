queue = []
queue.append([root])
while queue:
    current = queue.pop(0)
    new = []
    while current:
        temp = current.pop(0)
        if temp.val == u.val:
            if not current:
                return None
            else:
                return current[0]
        if temp.left:
            new.append(temp.left)
        if temp.right:
            new.append(temp.right)
    queue.append(new)

def inorderTraversal(node):
    l = []
    cur = node
    
    if cur.left is not None: l.extend(inorderTraversal(cur.left))
    l.append(cur.val)
    if cur.right is not None: l.extend(inorderTraversal(cur.right))

    return l

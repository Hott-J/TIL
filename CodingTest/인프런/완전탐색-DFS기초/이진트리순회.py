def preorder(v):
    if v>7:
        return
    else:
        print(v, end=' ')
        preorder(v*2)
        preorder(v*2+1)

def inorder(v):
    if v>7:
        return
    else:
        inorder(v*2)
        print(v,end=' ')
        inorder(v*2+1)

def postorder(v):
    if v>7:
        return
    else:
        postorder(v*2)
        postorder(v*2+1)
        print(v,end=' ')

preorder(1)
print()
inorder(1)
print()
postorder(1)
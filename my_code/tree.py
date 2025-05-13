class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
        print(f"A new Node is initialized with value of {self.value}")
        return

    def add_left_child(self, new_node):
        if not self.left:
            self.left = new_node
        elif not self.right:
            self.right.add_left_child(new_node)
        else:
            self.left.add_left_child(new_node)
        return new_node

    def add_right_child(self, new_node):
        if not self.right:
            self.right = new_node
        elif not self.left:
            self.add_left_child(new_node)
        else:
            self.left.add_left_child(new_node)
        return new_node

class Bin_tree:
    def __init__(self, node: Node):
        self.root = node

    def bfs(self):
        result = []
        q = []
        if self.root:
            cur = self.root
            q.append(cur)
            while q:
                cur = q[0]
                q = q[1:]
                result.append(cur)
                # for i in cur.childNodes: q.append(i)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            print("The traverse of BFS reslt is ", [i.value for i in result])
            return result
        else:
            return

    def bfs_recursive(self, result:list, q:list):
        if not q:
            return
        else:
            a = q[0]
            q = q[1:]
            if a.left:
                result.append(a.left.value)
                q.append(a.left)
            if a.right:
                result.append(a.right.value)
                q.append(a.right)
            return self.bfs_recursive(result, q)


    """DFS has Three mainly types Preorder, postorder and inorder
    Much easier to be implemented by recursion but we may use a stack as well and write into a iterative model
    """

    def dfs_inorder(self, node, result):
        if not node:
            return
        else: 
            if node.left:
                self.dfs_inorder(node.left, result)
            result.append(node.value)
            if node.right:
                self.dfs_inorder(node.right,result)
            return result
        
    def dfs_preorder(self, node, result):

        if not node:
            return
        else:
            result.append(node.value)
            if node.left:
                self.dfs_preorder(node.left, result)
            if node.right:
                self.dfs_preorder(node.right,result)
            return result
    
    def dfs_postorder(self, node, result):

        if not node:
            return
        else: 
            if node.left:
                self.dfs_postorder(node.left, result)
            if node.right:
                self.dfs_postorder(node.right,result)
            result.append(node.value)
            return result
        
        
if __name__ =="__main__":
    a=Node(5)
    b=a.add_left_child(Node(6))
    c=a.add_right_child(Node(7))
    d=b.add_left_child(Node(8))
    e=b.add_right_child(Node(9))
    f=c.add_right_child(Node(10))
    g=a.add_left_child(Node(11))
    t=Bin_tree(a)
    t.bfs()
    res,q = [],[]
    if t.root:
        q=[t.root]
    if t.root:
        res= [t.root.value]
    t.bfs_recursive(res,q)
    print("Recursive BFS Traverse is ", res)
    print("======================")
    a1,a2,a3=t.root,t.root,t.root
    print("Inorder DFS:", t.dfs_inorder(a2,[]))
    print("Preorder DFS:",t.dfs_preorder(a1,[]))

    print("Postorder DFS:",t.dfs_postorder(a3,[]))

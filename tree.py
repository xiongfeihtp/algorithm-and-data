# 树的存储单位为节点
class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    """二叉树"""
    def __init__(self):
        # 根节点
        self.root = None

    def add(self, item):
        # 广度优先的遍历,始终在左边读取，右边补充，队列
        node = Node(item)
        queue = []  # 列表当做队列处理
        queue.append(self.root)

    #特殊情况,将问题等效为一个基本数据结构的操作
        if self.root is None:
            self.root = node
            return
        while queue:
            cur_node = queue.pop(0)
        #如果根节点一开始为空。
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)
#树的广度遍历
    def breadth_travel(self):
        """树的广度遍历"""
        queue=[self.root]
        if self.root==None:
            return
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.lchild is not None:
                queue.append(cur_node.rchild)
#树的深度遍历
#遍历的过程存在递归
    def preorder(self, node):
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)


    def medorder(self,node):
        if node is None:
            return
        self.medorder(node.lchild)
        print(node.elem)
        self.medorder(node.rchild)


    def endorder(self,node):
        if node is None:
            return
        self.endorder(node.lchild)
        self.endorder(node.rchild)
        print(node.elem)

        
if __name__=="__main__":
    tree=Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
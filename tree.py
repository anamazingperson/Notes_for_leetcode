class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 把所有的和都加起来，每得到一个判断来计数，
        prefix = {0:1}
        self.ans = 0
        def dfs(root,cur_sum):
            if not root:
                return 0
            
            cur_sum += root.val
            self.ans += prefix.get(cur_sum-targetSum,0)

            prefix[cur_sum] = prefix.get(cur_sum,0) + 1
            dfs(root.left,cur_sum)
            dfs(root.right,cur_sum)
            prefix[cur_sum] -= 1
            return self.ans
        return dfs(root,0)

# 数的基本遍历
# DFS三种遍历
from collections import deque
def buildtree_leveldorder(l):
    if not l:
        return []
    root = TreeNode(l[0])
    que = deque([root])
    n = len(l)
    i = 1
    while i < n:
        node = que.popleft()
        left = TreeNode(l[i])
        node.left = left
        que.append(left)
        i +=1
        if i < n :
            right= TreeNode(l[i])
            node.right = right
            que.append(right)
        i +=1
    return root

def firstorder(root):
    if not root:
        return []
    return [root.val] + firstorder(root.left) + firstorder(root.right)
def midorder(root):
    if not root:
        return []
    return  midorder(root.left) +[root.val] + midorder(root.right)
def lastorder(root):
    if not root:
        return []
    return  lastorder(root.left) + lastorder(root.right)+[root.val]

def test_build_order():
    root = buildtree_leveldorder([1,2,3,4,5,6])
    l = lastorder(root)
    print(root,l)

# 复原树结构
# 前序和中序复原树结构
def rebuild_tree(l1,l2):
    if not l1 or not l2:
        return
    value  = l1[0]
    ind = l2.index(value)
    root = TreeNode(value)
    root.left = rebuild_tree(l1[1:1 + ind],l2[:ind])
    root.right = rebuild_tree(l1[1+ind:],l2[ind+1:])
    return root

# 要复原一棵树，必须要有中序遍历
def test_rebuild():
    root = buildtree_leveldorder([1,2,3,4,5,6])
    l1 = firstorder(root)
    l2 = midorder(root)
    root = rebuild_tree(l1,l2)
    print(l1,firstorder(root))
    print(l2,midorder(root))

# 层序遍历
def levelorder(root):
    # 返回一维的
    res = []
    deq = deque([root])
    while deq:
        node = deq.popleft()
        res.append(node.val)
        if node.left:
            deq.append(node.left)
        if node.right:
            deq.append(node.right)
    return res

def test_level():
    true = range(15)
    root = buildtree_leveldorder(true)
    rebuild = levelorder(root)
    print("true:",true,"rebuild",rebuild)

# 树结构，递归的理解，路径的和，采用前缀和。
# 树的基本遍历，  递归引进之后的代码执行顺序，对于空节点处理，那些代码怎么执行
# 树的和，判断相连接节点的值和等于固定值的，对应的子连接数目

def Count(root,targetSum):
    dict_ = {0:1}
    def dfs(root,nodeSum):
        if not root:
            return 0
        nodeSum += root.val
        ans = dict_.get(nodeSum - targetSum, 0) 
        dict_[nodeSum] = dict_.get(nodeSum,0) + 1
        ans +=dfs(root.left,nodeSum)
        ans +=dfs(root.right,nodeSum)
        dict_[nodeSum] -= 1
        return ans
    
    return dfs(root,0)

def test_sum():
    root = buildtree_leveldorder([1,2,3,4,5,6])
    print(Count(root,6))
# test_sum()
    

# 构建二叉搜索树
# 利用二叉搜索树查询某个数
def build_research(l):
    if not l:
        return
    n = len(l)
    root = TreeNode(l[n//2])
    root.left = build_research(l[:n//2])
    root.right = build_research(l[n//2+1:])
    return root
def find_value(root,value):
    if not root:
        return False
    if root.val == value:
        return True
    if value > root.val:
        return find_value(root.right,value)
    else:
        return find_value(root.left,value)
def test_research():
    l = range(200)
    root = build_research(l)
    print(levelorder(root))
    import random
    print(find_value(root,random.randint(200,500)))

    
# 树结构中的合并二叉树，首先得利用递归的思想，拆解成小问题，然后合并结果
# 判断递归是否需要有返回值，返回值设置成什么，
# 递归是自顶部向下部分解问题，自底向上合并结果，返回子树方便理解。
# 递归定义好之后，功能和返回值，以及终止条件三要数

# 合并二叉树
def merge(root1,root2):
    if not root1 and not root2:
        return
    if root1 and root2:
        root = TreeNode(root1.val + root2.val)
        root.left = merge(root1.left,root2.left)
        root.right = merge(root1.right,root2.right)
    elif not root1:
        return root2
    elif not root2:
        return root1
    return root
def test_merge():
    l1 = range(10)
    l2 = range(8)
    root1 = buildtree_leveldorder(l1)
    root2 = buildtree_leveldorder(l2)
    print(levelorder(merge(root1,root2)))

# 二叉搜索树的数量，给定n值，有多少种不同的二叉搜索树
# 通过根节点数值分类，根据二叉搜索树的性质，得到左右子树的数值关系，从而得到状态转移方程

def CountRT(n):
    res = [0]*(n+1)
    res[0] = 1
    res[1] = 1
    if n < 2:
        return res[n]
    for i in range(2,n+1):
        value = 0
        for j in range(i):
            value += res[j]*res[i-1-j]
        res[i] = value
    return res[-1]
def test_countrt():
    print(CountRT(2))

# 小偷问题，不能偷相连的节点
# 递归的思路，偷当前节点，或者不偷当前节点
# 递归的返回值，当前节点偷与不偷的最大值
# 有返回值的递归
# 递归的终止条件，节点为空，返回0

def chief_tree(root:TreeNode):
    if not root:
        return (0,0)
    # 主要是局部的三点博弈

    left = chief_tree(root.left)
    right = chief_tree(root.right)
    take = root.val + left[1] +right[1]
    skip = max(left) + max(right)
    return (take,skip)

def test_chief():
    l = range(4)[::-1]
    l = [3,2,3,0,3,0,1]
    root = buildtree_leveldorder(l)
    print(max(chief_tree(root)))


# 树展开为链表。
# 递归的思路，先展开左右子树，然后把左子树接到右子树上，然后把右子树接到左子树的末端
# 或者采用后续遍历，从尾巴开始连接，逆序连接。


def toHead(root:TreeNode):
    if not root:
        return 
    
    toHead(root.right)
    left = root.left
    right = root.right
    root.left = None
    root.right = left
    root.right.left =None
    root.right.right = right
    toHead(root.left)
    return root


l = range(5)
root = buildtree_leveldorder(l)
print(toHead(root))
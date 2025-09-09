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

# 树结构，递归的理解，路径的和，采用前缀和。
# 树的基本遍历，  递归引进之后的代码执行顺序，对于空节点处理，那些代码怎么执行


# 递归总结：
# 大问题拆解的小问题具有相似性；
# 递归的终止条件；


# 树结构中的合并二叉树，首先得利用递归的思想，拆解成小问题，然后合并结果
# 判断递归是否需要有返回值，返回值设置成什么，
# 递归是自顶部向下部分解问题，自底向上合并结果，返回子树方便理解。
# 递归定义好之后，功能和返回值，以及终止条件三要数


# 树的几种遍历方法，以及通过遍历方法复原一棵树
# 前序遍历，中序遍历，后序遍历，层次遍历，核心是递归，搞清楚怎么递归，功能，返回值，终止条件


# 二叉搜索树的数量，给定n值，有多少种不同的二叉搜索树
# 通过根节点数值分类，根据二叉搜索树的性质，得到左右子树的数值关系，从而得到状态转移方程


# 小偷问题，不能偷相连的节点
# 递归的思路，偷当前节点，或者不偷当前节点
# 递归的返回值，当前节点偷与不偷的最大值
# 有返回值的递归
# 递归的终止条件，节点为空，返回0

# 树展开为链表。
# 递归的思路，先展开左右子树，然后把左子树接到右子树上，然后把右子树接到左子树的末端
# 或者采用后续遍历，从尾巴开始连接，逆序连接。
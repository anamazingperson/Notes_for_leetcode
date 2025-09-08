# 相交列表，

# 列表：单向，局部的连接
# 相遇节点判断，采用相等，哈希或者采用分析出终止条件。

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA
    

# 前缀树


# 定义对应的节点

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

# 对于树结构，最好不要改变根节点，重新定义变量，防止该变根节点

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root  # ✅ 用局部变量，不要改 self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

#  链表实现两数相加
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 涉及到进位，链表的终止；
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        # 相当于把位数补齐，然后进行一致性操作，还要注意最后一位的加减
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    

# 数组中的出现一次的数字
# 其他数字出现两次
# 位操作异或，或者采用集合、哈希实现，但是需要额外空间




# 中位数，两个排列好的数组
# 一般思路，两个指针，越小的移动，保留当前值和上一刻值，注意边界条件

# 数组中出现次数大于一半的数字，投票法或者哈希遍历，计算每个的次数，投票法，同就投，不同就减。


# 乘积最大子数组，动态规划，状态怎么实现转移，需要了解其中的机理
# 乘积可能为负数，负负得正，所以需要同时保存最大和最小值

# 戳气球，动态规划，把气球分为前后两段
# 两段均采用边界来区分


#链表排序，归并排序，拆分两段，保存一段，小的数字排序，，，还用用到next属性的，需要先判断current是否为空

# 二分法，基础的二分法，改进的二分法，边界变化，不仅仅是赋值mid,而是Mid的上一个或者下一个数，实现区间的搜索
# 改进方法，可以改进判断的条件，是否取等号，来实现不同的边界条件


# 买股票的最佳时机，理解题目，以每个数字为卖出点，把买入不确定性转化为前序数组的最小值，进而变为确定性事件
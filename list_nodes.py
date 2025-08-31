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

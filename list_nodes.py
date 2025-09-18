# 相交列表，
import  random

# 列表：单向，局部的连接
# 相遇节点判断，采用相等，哈希或者采用分析出终止条件。
# 创建链表
class ListNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
        
def create_list(nums):
    head = ListNode(0)
    dirty = head
    for num in nums:
        node = ListNode(num)
        head.next = node
        head  = head.next
    
    return dirty.next

def expand_list(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums

def get_cross(headA,headB):
    Ahead = headA
    Bhead = headB
    while headA != headB:  # 循环的结束条件
        if headA == headB:
            return headA.val
        if not headA:
            headA= Bhead
        if not headB:
            headB= Ahead
        headA = headA.next
        headB = headB.next
def test_create():
    nums1 = [1,3,5,6,7,8]
    nums2 = [-1,0,2,4,5,6,7,8]
    headA = create_list(nums1)
    headB = create_list(nums2)
    headC = create_list(nums2)
    A=headA
    headA.next.next = headC
    headB.next = headC

    print(get_cross(A,headB))


#  链表实现两数相加
def add(l1:ListNode,l2:ListNode):
    ans = 0
    sign = 0
    sign_last = 0
    t = 0
    while l1 or l2 or sign:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + sign
        sign = (total)//10
        ans += (total%10)*10**t

        # update
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        t += 1
    return ans
def test_add():
    nums = [1,2,3,9,2]
    nums2 = [1,2]
    print(add(create_list(nums),create_list(nums2)))

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


def get_once(nums):
    set_num = set(nums)
    return 2*sum(set_num) - sum(nums)
def test_once():
    nums = [1,2,3,2,1]
    print(get_once(nums))



# 中位数，两个排列好的数组
# 一般思路，两个指针，越小的移动，保留当前值和上一刻值，注意边界条件


# 只考虑奇数，没有考虑偶数
def find_mid(nums1,nums2):
    m = len(nums1)
    n = len(nums2)

    stop = (m+n)//2
    i,j = 0,0
    pre,cur = 0,0
    for t in range(stop + 1):
        pre = cur
        if i < m and (j>=n or nums1[i] < nums2[j]):
            cur = nums1[i]
            i += 1
        elif j < n-1:
            # 变量的作用其实是一致的，有些保留历史有些保留当前值
            cur = nums2[j]
            j += 1
    if (m+n)%2:
        return cur
    else:
        return (pre+cur)/2
    


def test_mid():
    nums1 = range(10)
    nums2=range(18,20)
    print(find_mid(nums1,nums2))


# 数组中出现次数大于一半的数字，投票法或者哈希遍历，计算每个的次数，投票法，同就投，不同就减。

def vote(nums):
    n = len(nums)
    dic_nums = {}
    for i in range(n):
        dic_nums[nums[i]] = dic_nums.get(nums[i],0) + 1
    ind = sorted(dic_nums,key=lambda x: dic_nums[x])
    return ind[-1]

def vote2(nums):
    n = len(nums)
    condidate,count = 0,0
    for num in nums:
        if count ==0:
            condidate = num
        count += 1 if num==condidate else -1
    
    if nums.count(condidate) > n//2:
        return condidate
    else:
        return None
def test_vote():
    nums = [1,2,3,3,3,4,4,4,4,4,4]
    print(vote2(nums))




#链表排序，归并排序，拆分两段，保存一段，小的数字排序，，，还用用到next属性的，需要先判断current是否为空

# 链表的基本操作
# 排序
def rank(head:ListNode):
    if not head or not head.next:
        return head

    start = head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    # 切割前后半段
    slow.next = None

    rankA = rank(start)
    rankB = rank(mid)
    return merge(rankA,rankB)


def merge(l1:ListNode,l2:ListNode):
    dummy = ListNode(0)
    head = dummy

    while l1 and l2:
        if l1.val < l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
     
    head.next = l1 if l1 else l2

    return dummy.next


def test_rank():
    nums = range(10)[::-1]
    head = create_list(nums)
    print(expand_list(rank(head)))

# test_rank()



# 二分法，基础的二分法，改进的二分法，边界变化，不仅仅是赋值mid,而是Mid的上一个或者下一个数，实现区间的搜索
# 改进方法，可以改进判断的条件，是否取等号，来实现不同的边界条件
# 螺旋数组排序，拆分的两段会有一段是连续的，然后对连续的采用二分法，需要添加判断连续的条件。

def base_2(nums,target): 
    n = len(nums)
    left ,right = 0, n-1
    while left < right:
        mid = (left+right)//2

        if nums[mid] < target:
            left = mid +1
        elif nums[mid] > target:
            right = mid -1
        else:
            return mid
    

def rotate_2(nums,target):
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid -1
            else:
                left = mid +1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid +1
            else:
                right = mid -1
    

                
            


def base_2(nums,target): 
    n = len(nums)
    left ,right = 0, n-1
    while left <= right:
        mid = (left+right)//2

        if nums[mid] < target:
            left = mid +1
        elif nums[mid] > target:
            right = mid -1
        else:
            return mid



def test_rotate():
    nums1 = [i for i in range(2,10)]
    nums2 = [0,1]
    nums = nums1 + nums2
    a =0
    print(nums[rotate_2(nums,a)])
    # print(rotate_2(nums,a))



# 买股票的最佳时机，理解题目，以每个数字为卖出点，把买入不确定性转化为前序数组的最小值，进而变为确定性事件

def buy_tik(nums:list):
    ans = float('-inf')
    in_min = nums[0]
    for i in range(1,len(nums)):
        in_min = min(in_min,nums[i-1])
        ans = max(ans,nums[i]-in_min)
    return ans



def test_buy():
    nums = [random.randint(3,10) for _ in range(10)]
    print(nums)
    print(buy_tik(nums))

# 任务调度，休息工作，根据规律得到公式，【AAA,BBB]





# 下一个排列，[1,2,3,].[1,3,2]，主要是下一个的通用逻辑是，先找到右左第一个小的，然后右左比这个数大的，交换之后，翻转，【i+1,..]
def get_next(nums):
    n = len(nums)
    for i in range(n):
        if n-i-2 >=0 and nums[n-i -1] > nums[n-i-1-1]:
            i_min = n-i-1-1
            break
        
    for i in range(n):
        if nums[n-i-1] > nums[i_min]:
            i_max = n-i-1
            break
    print(i_max,i_min)
    temp = nums[i_min]
    nums[i_min] = nums[i_max]
    nums[i_max] = temp

    return nums[:i_min+1] + sorted(nums[i_min+1:],reverse= True)

def test_next():
    nums = [i for i in range(10)]
    nums = [2,3,1]
    print(get_next(nums))

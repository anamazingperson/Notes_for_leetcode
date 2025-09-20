# 为什么需要带记忆
# 带记忆的递归
# 递归的本质是重复计算
# 带记忆的递归是自顶向下的动态规划

# 硬币零钱问题
# 两种思路，向上规划和向下规划
# 无穷大, float('inf')


# 给定coins，里面的数字组成target，可以的话返回true ，否则 False
#[2,2,8],10
# 时间效率很低，递归循环n！
def charge(coins,target):
    if target == 0:
        return True
    if target < 0:
        return False
    n = len(coins)
    # 循环加递归有什么后果
    ans = False
    for i in range(n):
        ans = ans or charge(coins[:i]+coins[i+1:],target - coins[i])
    return ans

# 采用动态规划,根据目标值是否可以表示来动态规划
# i是否可以表示
# 输出只是判断是否不够，需要具体的数字或者单词组合
# 保存数字的话需要先把路径保存，然后不断回溯
def dp_charge(coins,target):
    dp = [False]*(target + 1)
    dp[0] = True
    prev = [-1] * (target +1)
    for coin in coins:
        for t in range(target,coin-1,-1):
            if dp[t - coin]:
                dp[t] = True
                prev[t] = coin

    if not dp[target]:
        return None


    t = target
    res = []
    while t>0:
        if prev[t]==-1:
            return None

        res.append(prev[t])
        t -= prev[t]

    return res[::-1]


def test_dp():
    coins = [1,2,5,10]
    target = 30
    print(dp_charge(coins,target))
# test_dp()
# 字符串是否可以由单词组成
# 动态规划
# 自底向上，一段一段来，每一段单词返回一个标志


# 例子 s = "nihao",words = ['ni','hao']

def match(s,words):
    n = len(s)
    dp = [False]*(n +1)
    dp[0] = True
    prev = [-1]*(n+1)
    for i in range(1,n+1):
        for word in words:
            if i >=len(word) and dp[i-len(word)] and s[i-len(word):i] == word:
                dp[i] = True
                prev[i] = word
                break
    
    # 回溯
    if not dp[n]:
        return None
    res = []
    while n>0:
        res.append(prev[n])
        n = n - len(prev[n])
    return res[::-1]
def test_match():
    s = "nidas"
    words = ['ni','hao','das']
    print(match(s,words))



# 每日温度，# 单调栈
# 一个一个遍历，添加出栈条件，形成单调栈，出栈
# 描述：给定一个整数数组 temperatures，表示每天的温度。
# 请返回一个数组 answer，其中 answer[i] 表示：在第 i 天之后，才会有更高的温度。
# 如果之后没有更高的温度，则在该位置用 0 来代替。


# 直接一个二层循环，存在的问题是，重复对比
# 遇到一个高的，前面的温度排序都解决了，这里面有一个单调栈的思想
# 构造一个单调递减的栈
from collections import deque
def get_high_t(temperatures):
    stack = []
    n = len(temperatures)
    ans = [0]*n
    for i,t in enumerate(temperatures):
        # 出
        while stack and t> temperatures[stack[-1]]:
            ind = stack.pop()
            ans[ind] = i - ind
        stack.append(i)
    return ans
def test_t():
    print(get_high_t([73,74,75,71,69,72,76,73]))
# 输出: [1,1,4,2,1,1,0,0]




# 爬楼梯问题，# 斐波那契数列，机器人寻路问题，主要是把状态转移方程找出来

# 输入几阶楼梯，返回方法数
def climb(n):
    if n ==1 or n==0:
        return 1
    
    return climb(n-1) +climb(n-2)

# print(climb(2))


# 机器人类似的，主要是把边界条件理清楚





# 乘积最大子数组，动态规划，状态怎么实现转移，需要了解其中的机理
# 乘积可能为负数，负负得正，所以需要同时保存最大和最小值
# 给你一个整数数组 nums，请你找出数组中 乘积最大的连续子数组（子数组最少包含一个数），并返回该乘积。

def MultSubNum(nums):
    # 以某个数为结束的最大值或最小值作为函数整体功能
    # 分开做
    n = len(nums)
    min_dp = [0]*n
    max_dp = [0]*n
    min_dp[0]  = max_dp[0] = nums[0]
    for i in range(1,n):
        # nums[i]必须用到
        min_dp[i] = min(min_dp[i-1]*nums[i],max_dp[i-1]*nums[i],nums[i])
        max_dp[i] = max(min_dp[i-1]*nums[i],max_dp[i-1]*nums[i],nums[i])
    return max(max_dp)

def test_Mul():
    nums = [-2,0,-1]
    nums =[2,3,-2,4]
    print(MultSubNum(nums))





# 戳气球，动态规划，把气球分为前后两段
# 两段均采用边界来区分
# 有 n 个气球，编号从 0 到 n - 1，每个气球上都标有一个数字，存放在数组 nums 中。

# 你可以选择任意一个气球进行戳破，如果戳破编号为 i 的气球，你将获得：
# nums[i-1] * nums[i] * nums[i+1]
# 戳破后，i 位置的气球消失，两侧的气球将直接相邻。

# 如果 i-1 或 i+1 超出数组范围，则当作 1 处理。

# 请你计算，最多能获得多少枚硬币。

# 动态规划需要在变化中得到不变的因素，然后
def bullen(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    for length in range(2,n):
        for i in range(0,n-length):
            j = i+ length
            for k in range(i+1,j):
                dp[i][j] = max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
    return dp[0][n-1]
def test_bullen():
    nums = [3,1,5,8]
    print(bullen(nums))



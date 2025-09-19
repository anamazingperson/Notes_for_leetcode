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


# 爬楼梯问题，# 斐波那契数列，机器人寻路问题，主要是把状态转移方程找出来


# 乘积最大子数组，动态规划，状态怎么实现转移，需要了解其中的机理
# 乘积可能为负数，负负得正，所以需要同时保存最大和最小值


# 戳气球，动态规划，把气球分为前后两段
# 两段均采用边界来区分
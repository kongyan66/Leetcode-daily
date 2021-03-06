# 题目：给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
# 思路：和115.不同子序列相比，多了删除操作

'''
1.确定dp数组及下标含义
dp[i][j]：以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。
2.确定递推公式
- 当word1[i - 1] 与 word2[j - 1]
dp[i][j] = dp[i-1][j-1]
- 当word1[i - 1] 与 word2[j - 1]不相同
情况一：删word1[i - 1]，最少操作次数为dp[i - 1][j] + 1
情况二：删word2[j - 1]，最少操作次数为dp[i][j - 1] + 1
情况三：同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2
dp[i][j] = min({dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1});
3. dp初始化
dp[i][0] 和 dp[0][j]是一定要初始化的（咋看出的）
dp[i][0]：word2为空字符串，以i-1为结尾的字符串word1要删除多少个元素，才能和word2相同呢，很明显dp[i][0] = i。
'''

# 解法
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # 空字符可由任意字符删除i次得到
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for j in range(1, len(word2)+1):
            dp[0][j] = j
        # 标准遍历模板
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                #当前字母相等，不需任何操作
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 字母不相等，要么删word1,要么删word2,要么都删，然后取最小值
                else:
                    dp[i][j] = min(dp[i-1][j-1]+2, dp[i][j-1]+1, dp[i-1][j]+1)
        return dp[-1][-1]
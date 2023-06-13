# 最小插入次數建構回文串 time complexity: O(n^2); space complexity: O(n^2)
def min_insertions(s: str):
    # Define DP table: DP[i][j] is minium of s[i:j] insertion times to build palindrome string.
    DP = [[0 for i in range(len(s))] for j in range(len(s))]

    # DP[i][j] = 0 if i==j or j>i

    for i in reversed(range(len(s)-1)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                # 兩邊相同不須插入任何數，加上DP[i+1][j-1]插入數即可成回文
                DP[i][j] = DP[i+1][j-1]
            else:
                # 選擇s[i+1: j] or s[i: j-1] 何者插入數最少
                # 再插入一次即可成回文
                DP[i][j] = min(DP[i+1][j], DP[i][j-1]) + 1
    
    # solution is DP[0][len(s)-1]
    return DP[0][len(s)-1]

def min_insertions1(s: str):
    DP = [0 for i in range(len(s))]

    for i in reversed(range(len(s)-1)):
        pre = 0
        for j in range(i+1, len(s)):
            temp = DP[j]
            if s[i] == s[j]:
                DP[j] = pre
            else:
                DP[j] = min(DP[j], DP[j-1]) + 1
            
            pre = temp

    return DP[len(s)-1]


if __name__ == "__main__":
    print(min_insertions1("acvca"))
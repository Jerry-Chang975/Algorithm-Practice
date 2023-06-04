# 最長回文子序列 time complexity O(N^2)
def LPS(s: str):
    # define DP table: DP[i][j] = LPS of s[i:j]
    # solution is DP[0][len(s)]
    DP = [[0 for i in range(len(s))] for i in range(len(s))]

    # i = j -> len(s) = 1 -> LPS = 1
    for i in range(len(s)):
        DP[i][i] = 1
    
    for i in reversed(range(len(s)-1)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                DP[i][j] = DP[i+1][j-1] + 2
            else:
                DP[i][j] = max(DP[i][j-1], DP[i+1][j])
    
    return DP[0][len(s)-1]

# 進一步狀態壓縮，DP 2d->1d
def LPS_2(s: str):
    # define DP table: DP[i][j] = LPS of s[i:j]
    # solution is DP[len(s)-1]

    # i = j -> len(s) = 1 -> LPS = 1
    # 2d 映射到 row
    DP = [1 for j in range(len(s))]
    
    for i in reversed(range(len(s)-1)):
        pre = 0
        for j in range(i+1, len(s)):
            # 先把目前個 DP[j] 值存起來
            temp = DP[j]
            if s[i] == s[j]:
                DP[j] = pre + 2 # pre = 上一個 DP[j]
            else:
                DP[j] = max(DP[j-1], DP[j])
            pre = temp # 更新上一個 DP[j]
    
    return DP[len(s)-1]


if __name__ == "__main__":
    print(LPS("acfsdfdsdea"))
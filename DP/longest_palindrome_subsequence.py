# 最長回文子序列
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


if __name__ == "__main__":
    print(LPS("acfsdfdsdea"))
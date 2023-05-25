# 最長共用子序列 LCS
def LCS(str1, str2):
    # use a DP table to save LCS
    DP = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]

    # base case 
    # DP[0][..] and DP[..][0] = 0

    for i in range(len(str2)):
        for j in range(len(str1)):
            if str2[i] == str1[j]:
                DP[i][j] = DP[i-1][j-1] + 1
            else:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j])

    return DP[i][j]


if __name__ == "__main__":
    str1 = "ascse"
    str2 = "asase"

    print(LCS(str1, str2))

                

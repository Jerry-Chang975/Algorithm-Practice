# 最長共用子序列 LCS
def LCS(str1, str2):
    # use a DP table to save LCS
    # DP = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]

    # base case 
    # DP[0][..] and DP[..][0] = 0


    # for i in range(1, len(str2)+1):
    #     for j in range(1, len(str1)+1):
    #         if str2[i-1] == str1[j-1]:
    #             DP[i][j] = DP[i-1][j-1] + 1
    #         else:
    #             DP[i][j] = max(DP[i][j-1], DP[i-1][j])
    # return DP[i][j]

    # state compression: space complexity: O(N)
    DP_1 = [0 for i in range(len(str1)+1)]
    DP_2 = [0 for i in range(len(str1)+1)]
    
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                DP_2[j] = DP_1[j-1] + 1
            else:
                DP_2[j] = max(DP_2[j-1], DP_1[j-1])
        DP_1 = [i for i in DP_2]

    return DP_2[j]


if __name__ == "__main__":
    str1 = "asaafeghera"
    str2 = "assegerg"

    print(LCS(str1, str2))

                

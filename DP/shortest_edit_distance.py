# 最短編輯距離 Shortest Edit Distance O(N^2)

def edit_distance(str1, str2):
    """ use recursion
    """
    # memo 
    memo = {}
    # dp table: (i, j) = > str1[0:i], str2[0:j] shortest edit distance
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # base case
        if i == -1: return j + 1 # remaining steps 
        if j == -1: return i + 1 

        if str1[i] == str2[j]:
            memo[(i, j)] = dp(i-1, j-1)
        else:
            memo[(i, j)] = min(
                dp(i-1, j) + 1, # remove
                dp(i, j-1) + 1, # insert
                dp(i-1, j-1) + 1 # replace
            )
        
        return memo[(i, j)]

    return dp(len(str1)-1, len(str2)-1)

def edit_distance2(str1, str2):
    # DP table 
    dp = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]

    # remove 
    for i in range(len(str1)+1):
        dp[i][0] = i

    # insert
    for j in range(len(str2)+1):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] # skip
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1, # remove 
                    dp[i][j-1] + 1, # insert
                    dp[i-1][j-1] + 1 # replace
                )
    
    return dp[len(str1)][len(str2)]

if __name__ == "__main__":
    str1 = "Miigun"
    str2 = "Miibo"
    print(edit_distance2(str1, str2))
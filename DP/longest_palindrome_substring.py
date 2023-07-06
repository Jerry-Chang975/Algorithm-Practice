#最長連續回文子字串 

# DP solution time complexity O(n^2)
def LPSubstring(s: str):
    res = ''
    DP = [['' for _ in range(len(s))] for _ in range(len(s))]

    for i in range(len(s)):
        DP[i][i] = s[i]
        res = s[i]

    for i in reversed(range(len(s)-1)):
        for j in range(i+1, len(s)):
            if s[i] == s[j] and DP[i+1][j-1] != None:
                DP[i][j] = s[i] + DP[i+1][j-1] + s[j]
                res = DP[i][j] if len(res) < len(DP[i][j]) else res
            else:
                DP[i][j] = None

    return res

# the more simple way time complexity is also O(n^2) but faster
def LPSubstring_2(s: str):
    if s == reversed(s): return s

    n = len(s)
    res = ''

    def searcher(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1: right]

    for i in range(n):
        # compare odd and even length
        res = max(searcher(i, i), searcher(i, i+1), res, key=len) # set compare key = length of string
    
    return res

if __name__ == "__main__":
    print(LPSubstring_2("ada"))
    
# use DP to solve regex matching problem: time complexity O(MN), space complexity O(MN)
def is_match(s: str, p: str):
    # Use i, j pointer which is indicate of s, p to check the s is matched with p.
    # traverse the s and p to compare
    s_index = 0
    j_index = 0

    # use memo to reduce time complexity
    memo = {}

    # Use DP recursion dp(s, i, p, j) that return True if s[i:] is matched p[j:]
    def dp(s, i, p, j):

        # check memo has answer or not
        if (i, j) in memo:
            return memo[(i, j)]

        # base case
        if j == len(p):  # p traverse completed and check s complete or not
            return i == len(s)

        if i == len(s):  # p[j:] must be 'a*b*z*' type
            if (len(p)-j) % 2 == 1:
                return False

            for ind in range(j+1, len(p), 2):
                if p[ind] != '*':
                    return False

            return True

        # "." can match any char
        if s[i] == p[j] or p[j] == ".":
            # compare
            if j < len(p)-1 and p[j+1] == "*":
                # "*" can compare many times or not compare
                res = dp(s, i + 1, p, j) or dp(s, i, p, j + 2)
            else:
                # general compare
                res = dp(s, i+1, p, j+1)

        else:
            # not compare
            if j < len(p)-1 and p[j+1] == "*":
                res = dp(s, i, p, j + 2)
            else:
                res = False

        memo[(i, j)] = res

        return res

    return dp(s, s_index, p, j_index)


if __name__ == "__main__":
    print(is_match('abddddfe', 'abd*f.'))

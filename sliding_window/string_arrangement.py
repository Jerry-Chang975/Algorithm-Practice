# 字串排列: 給兩字串 s, t，若字串s內含有任一種t字串之全排列，則return True
# 與最小覆蓋字串非常相似，只需多判斷length是否與t字串相等。
def sliding_window(s, t):
    window = {}
    need = {} 
    valid = 0
    left = 0; right = 0

    # 紀錄目標
    for c in t: need[c] = need.get(c, 0) + 1

    # start sliding
    while right < len(s):
        right_ele = s[right]
        right += 1
        if need.get(right_ele, 0):
            window[right_ele] = window.get(right_ele, 0) + 1
            if window[right_ele] == need[right_ele]:
                valid += 1

        while valid == len(need):
            # check if has satisfied target
            if right - left == len(t):
                return True

            left_ele = s[left]
            left += 1
            if need.get(left_ele, 0):
                if window[left_ele] == need[left_ele]:
                    valid -= 1
                window[left_ele] = window.get(left_ele, 0) - 1
    
    return False

if __name__ == "__main__":
    s = "weiofnlwefneiow"
    t = "lfn"

    print(sliding_window(s, t))
        

                
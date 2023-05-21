# sliding window algorithm - time complexity: O(N)

def sliding_window(s, t):
    left = 0; right = 0
    window = {} # char: count
    need = {}
    valid = 0 # record counts of valided char

    # result sub-string of start index and length
    start = 0
    length = float("inf")
    
    # record need chars
    for c in t: need[c] = need.get(c, 0) + 1

    while right < len(s):
        right_ele = s[right]
        right += 1
        if need.get(right_ele, 0):
            window[right_ele] = window.get(right_ele, 0) + 1 # str's count + 1
            if window[right_ele] == need[right_ele]:
                valid += 1
        

        # check if window has satisfied need
        while (valid == len(need)):
            # updata shortest substring solution
            if right - left < length:
                length = right - left
                start = left
            
            left_ele = s[left]
            left += 1
            if need.get(left_ele, 0):
                if window[left_ele] == need[left_ele]: # 如果目前char數量與目標相同，則左移後該char一定不滿足valid
                    valid -= 1
                window[left_ele] -= 1 # str's count - 1

    if length == float("inf"): return ""

    return s[start:start+length]

if __name__ == "__main__":
    string = "ewfzvsdfwefzsdafwe"
    target = "eva"

    print(sliding_window(string, target))

    
                


# return longest not repeat sub-string in given string
def sliding_window(s):
    window = {}
    left = 0; right = 0
    length = 0

    # start sliding
    while right < len(s):
        # get longest
        if right - left > length:
            length = right - left
            start = left
            
        right_ele = s[right]
        right += 1
        window[right_ele] = window.get(right_ele, 0) + 1

        while window[right_ele] > 1:
            
            left_ele = s[left]
            left += 1
            window[left_ele] = window.get(left_ele, 0) - 1
    
    return s[start: start+length]

if __name__ == "__main__":
    s = "shhhhhfdsfwefokwejcirj"

    print(sliding_window(s))
        
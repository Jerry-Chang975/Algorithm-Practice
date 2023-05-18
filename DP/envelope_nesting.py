# 信封嵌套問題，給幾個(w, h)大小不一的信封袋，返回最大嵌套數量
# 二維LIS問題

def envelope_nesting(envelops: list[list[int, int]]): # O(NlogN)
    # 先昇序排w，若w相同則降序排h  O(NlogN)
    sort_env = sorted(envelops, key=lambda x: (x[0], -x[1]))
    print(sort_env)

    # LIS O(NlogN)
    top = []
    piles = 0

    for i in range(len(sort_env)):
        ele = sort_env[i][1]
        left = 0; right = piles
        while left < right:
            mid = (left + right) // 2
            if top[mid] > ele:
                right = mid
            elif top[mid] < ele:
                left = mid + 1
            elif top[mid] == ele:
                right = mid
            
        if left == piles:
            piles += 1
            top.append("")
        top[left] = ele
    
    return piles    

if __name__ == "__main__":
    envelops = [[2, 4], [3, 8], [5, 7], [1, 2], [2, 5], [7, 9]]
    print(envelope_nesting(envelops))

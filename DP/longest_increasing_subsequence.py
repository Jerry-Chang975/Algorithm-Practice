# 給一無序陣列nums，找出最長的的遞增子序列(LIS)  序列不必連續

# DP解 O(n^2) 
def longest_increasing_subsequence(nums): 
    # define DP table
    DP = [1 for i in range(len(nums))] # DP[i]代表以nums[i]結尾之LIS
    
    for i in range(len(nums)): # 這層要逐步推算出DP[i]之值
        for j in range(i): # 透過DP[j]推算DP[i]
            if nums[i] > nums[j]:
                DP[i] = max(DP[i], DP[j]+1)

    res = 1

    for i in range(len(DP)): # 從DP table中找出最大值
        res = max(DP[i], res)

    return res

# 特殊解法 牌堆+binary search (詳見參考書籍 P104)
def binary_search(nums):
    top = [] # 牌堆最上層牌
    piles = 0 # 牌堆數
    for ele in nums: # 依序進行排列分堆
        left = 0; right = piles
        
        # 用binary_search找要放哪一牌堆
        while left < right:
            mid = (left + right) // 2

            if top[mid] > ele:
                right = mid
            elif top[mid] < ele:
                left = mid + 1
            elif top[mid] == ele:
                right = mid

        if left == piles: # 找不到牌堆可以放 新增一個
            piles += 1
            top.append("")
        top[left] = ele
    
    return piles
        
        

if __name__ == "__main__":
    nums = [2,1,4,12,3,11,17,18]
    print(longest_increasing_subsequence(nums))
    print(binary_search(nums))
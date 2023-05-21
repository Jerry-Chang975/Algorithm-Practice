# 最大子陣列和 -> time complexity: O(N)
def max_subarray(nums: list) -> int:
    # define dp table
    # 儲存dp[i] -> nums[i]結尾的max_subarray_sum
    # dp = [float("-inf") for _ in range(len(nums))] 
    # dp可進一步狀態壓縮 space complexity O(N) -> O(1)
    dp = nums[0]
    res = dp # 紀錄最大值
    dp_last = dp
    for i in range(1, len(nums)):
        # 狀態轉移方程
        dp = max(nums[i], dp_last + nums[i])
        res = max(res, dp)
        dp_last = dp

    return res

if __name__ == "__main__":
    nums = [2, -1, -10, 4, -2, 6, 3, -5, 1]
    print(max_subarray(nums))
    
    
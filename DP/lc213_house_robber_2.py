class Solution:
    def rob(self, nums: List[int]) -> int:
        # 長度 < 3 直接返回最大元素
        if len(nums) <= 3: return max(nums)

        def helper(n):
            rob1, rob2 = 0, 0
            for i in n:
                temp = rob2
                rob2 = max(rob1 + i, rob2)
                rob1 = temp
            
            return rob2
        
        # 避免頭尾都Rob，分開比較即可(1. 去除第一個與去除最後一個比較)
        return max(helper(nums[1:]), helper(nums[:-1]))
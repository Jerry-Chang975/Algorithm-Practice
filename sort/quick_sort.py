# 快速排序法 quick sort: time complexity: O(NlogN), but worst may be O(N^2)
def quick_sort(nums: list):
    # base condition
    if len(nums) == 0 or len(nums) == 1:
        return nums
    
    comp = nums[0]
    left = []; right = []
    for ele in nums[1:]:
        if ele <= comp:
            left.append(ele)
        else:
            right.append(ele)
    
    return quick_sort(left) + [comp] + quick_sort(right)


if __name__ == "__main__":
    import random
    unordered_arr = [random.randint(1, 10) for i in range(5000)]
    print(quick_sort(unordered_arr))
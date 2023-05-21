# 氣泡排序法 time complexity: O(N^2)
def bubble_sort(nums: list):
    for i in range(len(nums)): # 每一輪交換會讓 len(nums)-i 完成排序
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums


if __name__ == "__main__":
    import random
    unordered_arr = [random.randint(1, 10) for i in range(5000)]
    print(bubble_sort(unordered_arr))           
            
    
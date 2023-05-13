# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:34:44 2022

@author: jerry
"""

# 密碼轉正一格 ex: ind=1  0100 -> 0200, 0900 -> 0000
def plus_num(nums_str, ind):
    
    # string is immutable, so convert it to list type
    nums_str = list(nums_str)
    
    if nums_str[ind] == "9":
        nums_str[ind] = "0"
    else:
        nums_str[ind] = str(int(nums_str[ind]) + 1)
        
    nums_str = "".join(nums_str)
    
    return nums_str

# 密碼轉負一格 ex: ind=2  0130 -> 0120, 0100 -> 0190
def minus_num(nums_str, ind):
    
    # string is immutable, so convert it to list type
    nums_str = list(nums_str)
    
    if nums_str[ind] == "0":
        nums_str[ind] = "9"
    else:
        nums_str[ind] = str(int(nums_str[ind]) - 1)
        
    nums_str = "".join(nums_str)
    
    return nums_str


def pw_solution(init_str, target_str, deadend, record_dict):
    
    queue = [] # 佇列用來儲存待檢查的密碼
    visited = set() # 儲存檢查過的密碼
    step = 0 # 計算轉到目標密碼的步數
    
    queue.append(init_str)
    visited.add(init_str)
    visited.update(deadend) # 將不可轉到的密碼加入visited名單
    
    while queue:
        queue_size = len(queue) # 目前佇列的大小
        
        for i in range(queue_size):
            cur_str = queue.pop(0) # get first element
            
            if cur_str == target_str: return step
            
            # 將當前密碼的下一步所有可能加入queue裡，檢查過的就不加
            for j in range(len(cur_str)):
                plus_str = plus_num(cur_str, j)
                minus_str = minus_num(cur_str, j)
                
                if plus_str not in visited:
                    queue.append(plus_str)
                    visited.add(plus_str)
                    record_dict[plus_str] = cur_str
                if minus_str not in visited:
                    queue.append(minus_str)
                    visited.add(minus_str)
                    record_dict[minus_str] = cur_str
        step += 1
        
        
    return -1 # 列舉完仍找不到

# 檢視解鎖流程
def get_route(record, pw_str):
    
    def find_last(record, pw_str):
    
        last_str = record.get(pw_str)
        
        if last_str:
            find_last(record, last_str)
            print(last_str)
            
    find_last(record, pw_str)
    
    print(pw_str)
    
    

if __name__ == "__main__":
    
    init_str = "0300"
    
    target_str = "0529"
    
    # 限制不可轉到的密碼
    deadend = ["0310", "0320", "0329", "0400", "0410", "0420", "0429", "0500", "0510", "0520", "1300", "0200", "0390", "0301", "0309"]
    
    # 用字典紀錄當前密碼(key)的上一個狀態(value)
    record_dict = {}
    
    # 計算轉到目標密碼的步數
    step = pw_solution(init_str, target_str, deadend, record_dict)
    
    get_route(record_dict, "0529")
    
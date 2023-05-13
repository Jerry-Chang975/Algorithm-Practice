def merge_sort(arr: list):
    # base condition
    if len(arr) == 1: return arr

    mid = len(arr)//2

    arr_1 = merge_sort(arr[:mid]) 
    arr_2 = merge_sort(arr[mid:])

    sorted_arr = []

    p1 = 0
    p2 = 0
    while True:
        if p1 == len(arr_1):
            sorted_arr += arr_2[p2:]
            break
        elif p2 == len(arr_2):
            sorted_arr += arr_1[p1:]
            break

        if arr_1[p1] <= arr_2[p2]:
            sorted_arr.append(arr_1[p1])
            p1 += 1
        elif arr_2[p2] < arr_1[p1]:
            sorted_arr.append(arr_2[p2])
            p2 += 1
        

    return sorted_arr

if __name__ == "__main__":
    unordered_arr = [2,1,4,67,3,2]

    print(merge_sort(unordered_arr))


    
        



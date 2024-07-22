# using while loop time complexity os o(n)
# def Two_Pointers_problem(arr,targret):
#     start = 0
#     end = len(arr)-1
#
#     while start < end:
#         current_sum = arr[start] + arr[end]
#         if current_sum == targret:
#             return arr[start],arr[end]
#         elif current_sum > targret:
#             end -= 1
#         else:
#             start +=1
#
#     return None
#
# arr = [2, 3, 5, 8, 9, 10, 11]
# val = 17
# print(Two_Pointers_problem(arr,val))

def Two_pointers_problen_usingForLoop(arr,target):
    n= len(arr)
    for i in range(n):
        for j in range(n):
            if (i==j):
                continue
            if (arr[i] + arr[j] == target):
                return [arr[i] , arr[j]]

            if(arr[i] + arr[j]> target):
                break

    return 0

arr = [2, 3, 5, 8, 9, 10, 11]
val = 17
print(Two_pointers_problen_usingForLoop(arr,val))
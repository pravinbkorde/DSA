# binary Search Algorithm
# Iterative method
# def binarySearch(array, x, low, high):
#
#     # Repeat until the pointers low and high meet each other
#     while low <= high:
#
#         mid = low + (high - low)//2
#
#         if array[mid] == x:
#             return mid
#
#         elif array[mid] < x:
#             low = mid + 1
#
#         else:
#             high = mid - 1
#
#     return -1
#
#
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")

# Using Recursive method

# Binary Search in python


# def binarySearchRecursive(array, x, low, high):
#
#     if high >= low:
#
#         mid = low + (high - low)//2
#
#         # If found at mid, then return it
#         if array[mid] == x:
#             return mid
#
#         # Search the left half
#         elif array[mid] > x:
#             return binarySearchRecursive(array, x, low, mid-1)
#
#         # Search the right half
#         else:
#             return binarySearchRecursive(array, x, mid + 1, high)
#
#     else:
#         return -1
#
#
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
#
# result1 = binarySearchRecursive(array, x, 0, len(array)-1)
#
# if result1 != -1:
#     print("Element is present at index " + str(result1))
# else:
#     print("Not found")
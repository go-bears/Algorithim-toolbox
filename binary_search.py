"""
Given a sorted array return index if a target number is in array.

Return 0 if num is not in array
Return 1 if num is in between numbers in array
Return last index if number is greater than any number in array

>>> binary_search([3,5,8,20,20,50,60], 0, 11, 1)
0

binary_search([3,5,8,20,20,50,60], 8), 0, 11, 90)
6

binary_search([3,5,8,20,20,50,60], 1, 11, 7)
2
"""

def binary_search(lst, low, high, target):
    """
    Given a sorted array return index if a target number 
    is in array.
    """
    
    # return 0 if array is empty
    if len(lst) < 2:
        return 

    # return 0 if num is less than lowest integer
    if target < lst[0]:
        return 0

    # return highest index number
    if target > lst[-1]:
        return len(lst) - 1
    
    # high - low = length of array
    # mid moves across the array during binary search
    mid = low + ((high - low) /2)

     # if target is found at midpoint, return midpoint as index
    if target == lst[mid]: 
        return mid
        # print mid

    if target < lst[mid]:
        high = mid + 1
        binary_search(array, low, high, target)

    # if targe is greater than midpoint move low to midpoint
    if target > lst[mid]:
        low = mid
        binary_search(array, low, high, target)


def main():
    import doctest
    import timeit
    
    print timeit.timeit(lambda: binary_search(array, 0, 11, 60), number=100)

    print binary_search(array, 0, 11, 60)
    
    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"

if __name__ == '__main__':
    array = [3,5,8,10,12,15,20,20,50,60]
    main()
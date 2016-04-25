def min_groups_naive(lst):

    """for a list of children's ages, find the smallest
    number of groups that for any grouping where the ages
    differ by a 1 year at most.

    >>> min_groups_naive([4, 3.2, 3.8, 4.6, 5])
    2

    >>> min_groups_naive([4, 3.2, 3.8, 4.6, 5, 7])
    3

    >>> min_groups_naive([])
    

    >>> min_groups_naive([4, 3.8, 4.1])
    1

    min_groups_naive([4])
    1

    """

    # take the length of the list
    # initialize an empty array
    # for length of list, compare 
    # each num to check if difference
    # is greater than 1.
    # if less than 1 add elements to an array
    # if greater than one add element 
    # to a new list
    # return length of 
    groups = []

    # validate list of ages to check for if list can be grouped
    if len(lst) < 1:
        return None

    if len(lst) < 2 or max(lst) - min(lst) < 1:
        return 1

    # create groups
    else:

        # sort list
        lst.sort()
        
        # start first group with lowest age
        groups.append([min(lst)])

        # for every num, excepting the min age
        for num in lst[1::]:

            # if absolute difference between the min age and num is 
            # less than 1 append to the sub-group
            if abs(num - min(groups[-1])) <= 1:
                groups[-1].append(num)

            # if num > 1 append a new list with num as element
            else:
                groups.append([num])            
                

        return len(groups)


if __name__ == '__main__':
    import doctest
    import timeit


    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"

    print min_groups_naive([4, 3.2, 3.8, 4.6, 5, 7])
    print timeit.timeit(lambda: min_groups_naive([4, 3.2, 3.8, 4.6, 5]), number=1000)
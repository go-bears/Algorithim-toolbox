def pairwise_summonds(num):
    """
    Finds summonds of number where all sum integers are unique.
    
    >>> pairwise_summonds(8)
    [1, 3, 4]

    >>> pairwise_summonds(333)
    [30, 31, 32, 33, 34, 40, 41, 42, 50]
    
    >>> pairwise_summonds(1)
    False

    >>> pairwise_summonds(23444)
    [7813, 7814, 7817]
    """

    if num < 2:
        return False

    # initialize set to make sure all integers are unique
    summonds = set()

    # takes half of num to add to set
    half = num /2
    summonds.add(half)

    # create list of all of number less than half b/c you only need integers
    # that add up to the half the number  
    num_list = range(half)

    # sort list from highest to lowest
    num_list.sort(reverse=True)

    # iterate through reversed list 
    for i in num_list:

        # check for pairwise summond integers
        if sum(summonds) < num:
            summonds.add(i)

        # check if summonds set exceed num
        if sum(summonds) > num:
            summonds.pop()

        # returns list of integers once set equals num
        if sum(summonds) == num:
            return list(summonds)


def main():
    import timeit

    print pairwise_summonds(8)
    print timeit.timeit(lambda: pairwise_summonds(8), number=100)
    print pairwise_summonds(333)
    print timeit.timeit(lambda: pairwise_summonds(333), number=100)
    print pairwise_summonds(1)
    print timeit.timeit(lambda: pairwise_summonds(1), number=100)
    print pairwise_summonds(23444)
    print timeit.timeit(lambda: pairwise_summonds(23444), number=100)


if __name__ == '__main__':
    import doctest

    main()

    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"
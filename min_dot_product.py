def dot_product(array1, array2):

    """
    The goal in this problem is
    give two arrays of integers of equal length,
    find the minimum dot product of the two sequences

    >>> dot_product([23], [39])
    897

    >>> dot_product([1,3,-5], [-2,4,1])
    -25
    """

    if len(array1) < 1 or len(array2) < 1:
        return

    if len(array1) == len(array2):
        array1.sort() # sort list least to greatest
        array2.sort(reverse=True) # sort integers greatest to least

        
        products = []

        for i in range(len(array1)):        
            products.append(array1[i]*array2[i])

        return sum(products)


def main():
    import doctest
    import timeit

    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"

    print 'min dot product is ', dot_product([23], [39])
    print timeit.timeit(lambda: dot_product([23], [39]), number=100), '\n'

    print 'min dot product is ', dot_product([1,3,-5], [-2,4,1])
    print timeit.timeit(lambda: dot_product([1,3,-5], [-2,4,1]), number=100)

if __name__ == '__main__':
    main()
   
   

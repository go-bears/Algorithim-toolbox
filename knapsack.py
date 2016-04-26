def knapsack():
    """
    Maximization problem given a knapsack that can
    carry 7 lbs. what is the max value of items 
    with which you can pack the knapsack.

    items = {1:[20,4], 2:[18,3], 3:[12,2]}

    >>> knapsack()
    42

    """
    # breakdown item weight & value to unit cost
    # append unit to fractional list
    # sort fractional list from high to low
    # append units to knapsack until capacity is reached

    # key = item number, values = [cost, weight]
    items = {1:[20,4], 2:[18,3], 3:[14,2]}
    fractional = []

    knapsack = []
    knapsack_val = 0
    knapsack_capacity = 7

    # build array of fractional unit cost 
    for item, value in items.iteritems():
        for i in range(value[1]):
            unit_cost = value[0]/value[1]
            fractional.append(unit_cost)

    # sort the fractional list of items from high to low
    fractional.sort(reverse=True)

    # building the knapsack
    for unit in fractional:
        if len(knapsack) < knapsack_capacity: 
            knapsack.append(unit)
            knapsack_val += unit

    return knapsack_val

print knapsack()



if __name__ == '__main__':
    import doctest
    import timeit


    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"

    print 'maximized knapsack val', knapsack()
    print timeit.timeit(lambda: knapsack(), number=100)

def knapsack2(dct, capacity):
    
    items = dct
    fractional = []

    knapsack = []
    knapsack_val = 0
    knapsack_capacity = capacity

    # build array of fractional unit cost 
    for item, value in items.iteritems():
        for i in range(int(value[1])):
            unit_cost = value[0]/value[1]
            fractional.append(unit_cost)

    # sort the fractional list of items from high to low
    fractional.sort(reverse=True)

    # building the knapsack
    for unit in fractional:
        if len(knapsack) < knapsack_capacity: 
            knapsack.append(unit)
            knapsack_val += unit

    return format(knapsack_val, '.4f')

print knapsack2({1:[60,20.00], 2:[100,50.00], 3:[120, 30.00]}, 50)

print knapsack2({1:[500,30.00]}, 10)



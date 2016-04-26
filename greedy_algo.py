def largest_num1(lst):
    """Create largest integer from a list of numbers.

    Casts list of integers into strings to reverse and join
    then casts num_str into an integer

    >>> largest_num1([3,9,5,9,7,1])
    997531

    >>> largest_num1([1])
    1


    """

    if len(lst) > 0:
        lst.sort() # sort integers
        lst.reverse() # reverse list for highest to lowest value
        
        lst = [str(i) for i in lst] # convert i into strings
        
        num_str = ''.join(lst) # join list into a single string
        num = int(num_str) # cast num_string into an integer.
        

        return num

def changing_coins(lst, integer):

    pass

mileage = 400
stops = [0, 200, 375, 550, 750, 950]

def car_refuelling(array, length):
    """Find the minimum number of stops for gas refueling.
    mileage = 400
    stops = [0, 200, 375, 550, 750, 950]

    >>> car_refuelling([0, 200, 375, 550, 750, 950], 400)
    2

    """
    # go from a to g (farthest reachable stn)
    # make g the new a and then repeat until b is reached
    # initiaize variable to hold num_refills
    # save current position in last refill
    # while current position is less than index values in list
    # calculate farthest position that within 400km distance
    # move current position
    # increment num_refills
    # return num_refills or return "impossible"
    num_refills = 0
    start = stops[0]
    current = 0

    while current < (len(stops)-1):
        start = stops[current]
        farthest = 0 

        for index in range(len(stops)):
            if stops[index] - start < mileage:
                temp = stops[index] - start
                
                if temp > farthest and temp <= 400:
                    current = index
                    start = stops[current]
                    num_refills += 1

    return num_refills




    

def get_min_gas_stops(some_list, miles_per_tank):
    """Get the min number of gas stops to get from start to finish,
    where miles_per_tank is the max number of miles one can drive before needing
    to stop for gas
    >>> get_min_gas_stops([0, 200, 375, 500, 750, 900], 400)
    2
    """

    start = 0

    stops = []
    i = 0
    j = 1

    while j < (len(some_list)):
        # some_list[j] acts as runner
        if some_list[j] - start > miles_per_tank:

            # add  target some_list[i] to list of stops, and set start to some_list[i]
            stops.append(some_list[i])

            # shift start to new value in some_list
            start = some_list[i]
        i += 1
        j += 1
    return len(stops)



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
                
        # return number of groups
        return len(groups)



def knapsack2(dct, capacity):
    """
    Given a set of items and total capacity of a 
    knapsack,  nd the maximal value of fractions of 
    items that fit into the knapsack.

    >>> knapsack2({1:[60,20.00], 2:[100,50.00], 3:[120, 30.00]}, 50)
    180.0

    >>> knapsack2({1:[500,30.00]}, 10)
    166.6667


    """
    
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

    return float(format(knapsack_val, '.4f'))


if __name__ == '__main__':
    import doctest
    import timeit


    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"

    
    print 'largest num is,', largest_num1([3,9,5,9,7,1])
    print timeit.timeit(lambda: largest_num1([3,9,5,9,7,1]), number=100), "\n"
    
    print 'min gas stops is,', get_min_gas_stops([0, 200, 375, 500, 750, 900], 400)
    print timeit.timeit(lambda: get_min_gas_stops([0, 200, 375, 500, 750, 900], 400), number=100), "\n"
    
    print 'min number of groups,',\
          min_groups_naive([4, 3.2, 3.8, 4.6, 5])
    print timeit.timeit(lambda: min_groups_naive([4, 3.2, 3.8, 4.6, 5]), number=100), "\n"

    print 'max knapsack value is,', knapsack2({1:[60,20.00], 2:[100,50.00], 3:[120, 30.00]}, 50)
    print timeit.timeit(lambda: knapsack2({1:[60,20.00], 2:[100,50.00], 3:[120, 30.00]}, 50), number=100), "\n"

    print 'max knapsack value is,', knapsack2({1:[500,30.00]}, 10)
    print timeit.timeit(lambda: knapsack2({1:[500,30.00]}, 10), number=100)
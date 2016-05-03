def covering_segments(segment_list):
    """
    You are given a set of segments on a line and 
    your goal is to mark as few points on a line as 
    possible so that each segment contains at least
     one marked point

    >>> covering_segments([[1,3],[2,5],[3,6]])
    1
    >>> covering_segments([[4,7],[1,3],[2,5],[5,6]])
    2

    """

    if len(segment_list) < 1:
        return

    start = set(range(segment_list[0][0],(segment_list[0][1]+1)))
    segment_coverage =[start]

    i = 0

    while i < len(segment_list):
        
        # check that all inner lists are the same length
        if len(segment_list[i]) != len(start):
            return

        # convert segment points to list of number inclusive of the last number
        segment_list[i] = range(segment_list[i][0],(segment_list[i][1]+1))

        # check if segment has any overlapping number with start
        if start & set(segment_list[i]):

            # if it overlaps merge the new set to the start. 
            start = start | set(segment_list[i])
            
        else:
            # append the segment if it's disjoined with the previous segment
            segment_coverage.append(segment_list[i])
            
        i+= 1

    return len(segment_coverage)


if __name__ == '__main__':
    import doctest
    import timeit

    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"

    print 'min number of segments is ', covering_segments([[1,3],[2,5],[3,6]])
    print timeit.timeit(lambda: covering_segments([[1,3],[2,5],[3,6]]), number=100),'\n'


    print 'min number of segments is ', covering_segments([[4,7],[1,3],[2,5],[5,6]])
    print timeit.timeit(lambda: covering_segments([[4,7],[1,3],[2,5],[5,6]]), number=100)
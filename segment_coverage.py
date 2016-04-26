def covering_segments(segment_list):
    """
    You are given a set of segments on a line and 
    your goal is to mark as few points on a line as 
    possible so that each segment contains at least
     one marked point

    >>> covering_segments([[1,3],[2,5],[3,6]])
    1
    >>> covering_segments([[4,7],[1,3],[2,5],[5,6]])

    """

    if len(segment_list) < 1:
        return

    start = set(range(segment_list[0][0],(segment_list[0][1]+1)))
    segment_coverage =[start]

    i = 0

    while i < len(segment_list):
        segment_list[i] = range(segment_list[i][0],(segment_list[i][1]+1))

        if start & set(segment_list[i]):
            start = start & set(segment_list[i])
            
        else:
            segment_coverage.append(segment_list[i])
            

        i+= 1

    print segment_coverage
    return len(segment_coverage)



print covering_segments([[1,3],[2,5],[3,6]])
print covering_segments([[4,7],[1,3],[2,5],[5,6]])

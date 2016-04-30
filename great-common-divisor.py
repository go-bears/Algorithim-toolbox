import timeit
import doctest

"""

>>> gcd_ea(232435, 1450)
145

>>>lcm(28851538,1183019)
1933053046

"""
# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


# print(calc_fib(10))


def last_fib(n):

    fib = [0,1]

    for i in range(n-1):
        temp = fib[-1] + fib[-2]
        temp = str(temp)

        if len(temp) > 1:
            fib.append(int(temp[-1]))

        else:
            fib.append(int(temp))


    return fib[-1]

# print(last_fib(16))

def gcd1(n1, n2):
    """Find greatest common divisor with hill climbing alogrithim.

    divides both number by every number in range of lower number
    """

    best = 1

    for i in range(1,n2+1):
        if n1 % i == 0 and n2 % i == 0 and i > best:
            best = i            
            
    return best 



def gcd2(n1, n2):
    """Finding greatest common divisor by caching.

    Stores all integers in range 1-n2 that divide evenly
    into n1 and n2
     """

    if n1 > 0 and n2 > 0:

        divisor = []

        for i in range(1,n2+1):
            if n1 % i == 0 and n2 % i == 0:
                divisor.append(i)

        return divisor[-1]



def gcd_ea(n1, n2):
    """finds greatest common divisor with Euclid's alogrithim """

    # take in 2 integers
    # find the larger number
    # divide n1 by n2
    # store remainder
    # replace n1 by n2
    # replace n2 with remainder
    # repeat until r == 0
    # return n2 when r == 0


    if n1 > 0 and n2 > 0:
        if n1 > n2:
            a = n1
            b = n2
        else:
            a = n2
            b = n1

    remainder = a % b

    while remainder > 0:
        a, b = b, remainder
        remainder = a % b

    return b



def lcm(n1, n2):
    """Find lowest common multiple of two numbers.

    Imports gcd_ea() find greatest common denominator
    """
    
    if n1 > 0 and n2 > 0:
        gcd = gcd_ea(n1,n2)
        lcm = (n1 * n2) / gcd

    return lcm



if __name__ == '__main__':
    import doctest

    print lcm(232435,1450)
    print timeit.timeit(lambda: lcm(232435, 1450), number=100)

    print lcm(28851538,1183019)
    print timeit.timeit(lambda: lcm(28851538,1183019), number=100)

    print gcd_ea(232435, 1450)
    print timeit.timeit(lambda: gcd_ea(232435, 1450), number=100)

    print gcd1(232435, 1450)
    print timeit.timeit(lambda: gcd1(232435, 1450), number=100)

    print gcd2(232435, 1450)
    print timeit.timeit(lambda: gcd1(232435, 1450), number=100)


if doctest.testmod().failed == 0:
    print "\n*** ALL TESTS PASSED. GO YOU!\n"
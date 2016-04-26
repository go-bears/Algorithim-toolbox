def make_change(coins, money):

    """
    The goal in this problem is to and the minimum number of coins needed to change the given amount
    of money using coins with denominations 1, 5, and 10

    >>> make_change([1,5,10], 2)
    2

    >>> make_change([1,5,10], 28)
    6
    """
    num_coins = 0

    coins.sort(reverse=True)
    dime, nickel, penny = coins
    if money < 1:
        return

    while money > 0:

        if money >= dime:
            money -= dime
            num_coins += 1

        if money < dime and money > penny:
            money -= nickel
            num_coins += 1

        if money < nickel:
            money -= penny
            num_coins += 1

    return num_coins


if __name__ == '__main__':
    import doctest
    import timeit

    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"

    print 'min amount of coins is', make_change([1,5,10], 2)
    print timeit.timeit(lambda: make_change([1,5,10], 2), number=100)

    print 'min amount of coins is', make_change([1,5,10], 28)
    print timeit.timeit(lambda: make_change([1,5,10], 28), number=100)




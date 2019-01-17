"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

limit_number = 1000

def sum_of_multiples(x: int, y: int, limit_number: int) -> int:
    """

    :param x: Int value
    :param y: Int value
    :param limit_number: Int value under which the multiples of x and y can be found
    :return:
    """
    factors_set = {i for i in range(limit_number) if i % x == 0 or i % y == 0}
    sum = 0
    for val in factors_set:
        sum += val

    print(sum)
    return sum



sum_of_multiples(3, 5, limit_number)
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

TODO: Can improve this function based on the online discussion
"""
from time import  time


def get_fibonacci_seq(limit: int = 3)-> list:
    if limit == 0:
        return []

    ret_value = [1, 2, 3]
    for i in range(limit-3):
        ret_value.append(ret_value[-1]+ret_value[-2])

    return ret_value


def sum_of_even_fibonacci_seq(limit: int = 0) -> int:
    """

    :param limit: value not to be exceeded
    :return: sum of all the even number occurring in the Fibonacci sequence
    """
    last_1 = 1
    last_2 = 2
    ret_value = 0 # base condition
    while last_1 < limit:
        latest_num_in_seq = last_1 + last_2
        last_1 = last_2
        last_2 = latest_num_in_seq
        if last_1 % 2 == 0 and last_1 < limit:
            ret_value += last_1

    return ret_value


before = time()
print("Final answer: " + sum_of_even_fibonacci_seq(4000000).__str__())
after = time()
print(after - before)
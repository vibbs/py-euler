"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import floor, sqrt


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True


def get_prime_factors(num: int) -> list:
    # sqrt of the number is an optimization here so that we avoid uneccesaary iterations
    return [i for i in range(1, floor(sqrt(num))) if num % i == 0 and is_prime(i)]


def largest_prime_factor(num: int) -> int:
    return max([i for i in range(1, floor(sqrt(num))) if num % i == 0 and is_prime(i)])


print(largest_prime_factor(13195))

print(largest_prime_factor(600851475143))

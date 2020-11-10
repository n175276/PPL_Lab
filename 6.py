# Program to find first 10 pairs of amicable numbers

import math


def divisor_sum(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == (n / i):
                sum += i
            else:
                sum += i + (n / i)
    return sum


count = 0
i = 1

print("First 10 pairs of amicable numbers are :")
while count < 10:
    n = int(divisor_sum(i))
    if divisor_sum(n) == i and n > i:
        print(i, n)
        count += 1
    i += 1

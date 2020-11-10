# Program to display first 10 harmonic numbers

import statistics
n = 0
num = 1
while n != 10:
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    hm = float(statistics.harmonic_mean(lst))
    if hm.is_integer():
        print(num)
        n += 1
    num += 1

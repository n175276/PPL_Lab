# Program to find Armstrong numbers in the given range

a = int(input('Enter lower range : '))
b = int(input('Enter upper range : '))

print("Armstrong numbers in the range {} to {} is ".format(a, b))

for i in range(a, b):
    n = len(str(i))
    sum1 = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** n
        temp //= 10

    if i == sum1:
        print(i)

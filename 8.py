# Program to find LU decomposition of a matrix by Doolittle Method

matrix = []
n = int(input("Enter size of matrix : "))
print("Enter matrix elements in row major order : ")

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

# initializing upper and lower triangular matrices.
upper = [[0 for i in range(n)] for j in range(n)]
lower = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    # Upper decomposition
    for k in range(i, n):
        # sum of products lower[i][j]*upper[j][k]
        sum = 0
        for j in range(i):
            sum += (lower[i][j] * upper[j][k])

        upper[i][k] = matrix[i][k] - sum

    # Lower decomposition
    for k in range(i, n):
        if i == k:
            # diagonal elements set to 1
            lower[i][i] = 1
        else:
            sum = 0
            for j in range(i):
                sum += (lower[k][j] * upper[j][i])

            lower[k][i] = int((matrix[k][i] - sum) / upper[i][i])

print("Input Matrix :\n")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end="\t")
    print('')

print("Lower Triangular Matrix :\n")
for i in range(n):
    for j in range(n):
        print(lower[i][j], end="\t")
    print('')

print("Upper Triangular Matrix :\n")
for i in range(n):
    for j in range(n):
        print(upper[i][j], end="\t")
    print('')

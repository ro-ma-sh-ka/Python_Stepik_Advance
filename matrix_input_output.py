n, m = int(input()), int(input())
matrix = []
for _ in range(n):
    row = [input() for _ in range(m)]
    matrix.append(row)
# print(*[' '.join(row) for row in matrix], sep='\n')
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
n, m = int(input()), int(input())
matrix = [[row for row in input().split()] for _ in range(n)]
i, j = [int(_) for _ in input().split()]
for row in range(n):
    matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
print(*[' '.join(m) for m in matrix], sep='\n')
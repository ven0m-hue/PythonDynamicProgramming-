#Grid Travller Problem 
#Brute Force 


def gridTravaller(n,m):
    if (n == 1 and  m == 1): return 1
    if (n == 0 or   m == 0): return 0
    return gridTravaller(n-1,m) + gridTravaller(n, m-1)
# t = O(2^n+m)
# s = O(N)

print(gridTravaller(1,1))

#Memoization 
# Using the dp approch 
# using memoization 
def gridTravaller(n,m, mem = {}):
    key = f'{m},{n}'
    for key in mem : return mem[key]
    if (n == 1 and  m == 1): return 1
    if (n == 0 or   m == 0): return 0
    mem[key] = gridTravaller(n-1,m, mem) + gridTravaller(n, m-1, mem)
    return mem[key]
# t = O(2^n+m)
# s = O(N)


#Tabulation

def gridTravaller(m,n):
    matrix = [0]*(m+1)
    matrix = [[0]*(n+1) for i in matrix]   # create a MxN table and init it with some defualt value
    matrix[1][1] = 1                       # Seed value, trivial subproblem 1x1 is always 1  
    for i in range(m+1):                   # Iteration and logic
        for j in range(n+1):
            current = matrix[i][j]
            if j+1 <= n: matrix[i][j+1] += current
            if i+1 <= m: matrix[i+1][j] += current
    return matrix[i][j]
# t = O(m*n)
# s = O(m*n)

print(gridTravaller(18,18))


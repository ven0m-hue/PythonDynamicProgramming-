#The fibo sequence 
def fib(n):
    if (n<= 2):return 1
    return fib(n-1) + fib(n-2)
#T = O(2^n)
#S = O(n)

# Now using dynamic programming approach 
# memoization 
def fib(n, mem = {}): # store all the previously found sub solution into a memory or in hash table.
    if (n in mem) : return mem[n]  # if in that memo return else compute untill it hits the base case.
    if n<=2 : return 1
    mem[n] =  fib(n-1, mem) + fib(n-2, mem)

    return mem[n]
#T = O(n)
#S = O(n)

print(fib(50))
#Tabulation

def fib(n):
    a, b = 0,1
    for _ in range(n-1):
        c = a + b
        a = b
        b = c
    return b
# t = O(N)
# s = O(N)

print(fib(5000))

def fib(n):
    list = [0]*(n+1)  # Construct a table and init with some deafult vlaues
    list[1] = 1   # Seed value
    
    for i in range(1,n):
        list[i+1] += list[i] + list[i-1]
    return list[n]
print(fib(500))
# t = O(N*M)
# s = O(M)

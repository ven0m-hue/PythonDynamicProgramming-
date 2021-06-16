#CanSum Problem 
#Brute Force

def canSum(targetSum, llist):
    # base cases +ve
    if targetSum == 0: return True
    if targetSum <  0: return False 
    
    for ts in llist:
        rem = targetSum - ts
        if(canSum(rem, llist)): return True
    return False
# t = O(n^m)
# s = O(n)

#Memoization 

# Using the dp approch 
# using memoization 
def canSum(targetSum, llist, mem = {}):
    # base cases +ve
    key = targetSum
    if key in mem: return mem[key]
    if targetSum == 0: return True
    if targetSum <  0: return False 
    
    for num in llist:         
        if(canSum(targetSum - num, llist)): 
            mem[key] = True
            return mem[key]
    else:
        mem[key] = False
        return mem[key] 
# t = O(n)
# s = O(n)

canSum(300,[7,14])

#Tabulation

def canSum(targetSum, llist):
    table = [False] * (targetSum + 1)# Create a table of (targetSum length + 1) and init with some default vlaue based on the return vlaue 
    table[0] = True  # Seed valu by making trival sub problem. Given any array it is possible to generate 0
    
    for i in range(targetSum +1):  # iteration and the logic 
        if(table[i]):
            for j in llist:
                if (i+j) <= targetSum : table[i+j] = True

    return table[targetSum]
# t = O(n*m)
# s = O(m)           

canSum(7,[5,4,3])

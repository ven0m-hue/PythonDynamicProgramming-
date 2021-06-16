#### 3.2 HowSum Problem
#Brute Force

def howSum(targetSum, numbers):
    #base case 
    if targetSum == 0: return []
    if targetSum <  0: return None
    
    for num in numbers:  # iterate through the numbers in the array for possible matches 
        result = howSum(targetSum - num, numbers)
        if result != None:
            return [ *result, num]
    return None
# time complexity = O(n**m * m)
# space = O(m)

howSum(300,[7,14])

#Memoization

# Using the dp approch 
# using memoization 
def howSum(targetSum, numbers, mem = {}):
    if targetSum in mem: return mem[targetSum]
    #base case 
    if targetSum == 0: return []
    if targetSum <  0: return None
    
    for num in numbers:  # iterate through the numbers in the array for possible matches 
        result = howSum(targetSum - num, numbers)
        if result != None:
            mem[targetSum] = [ *result, num]
            return mem[targetSum]
    mem[targetSum] = None
    return mem[targetSum]
# time complexity = O(n*m**2)
# space = O(m**2)

#Tabulation

def howSum(targetSum, llist):
    table = [None] * (targetSum + 1)# Create a table of (targetSum length + 1) and init with some default vlaue based on the return vlaue 
    table[0] = []  # Seed valu by making trival sub problem. Given any array it is possible to generate 0
    
    for i in range(targetSum +1):  # iteration and the logic 
        if(table[i] is not None):
            for j in llist:
                if (i+j) <= targetSum : table[i+j] = [*table[i],j]
         
    return table[targetSum]   #filter out the none in the final answer
# t = O(n*m**2)
# s = O(m**2)           

howSum(8,[5,3,2])

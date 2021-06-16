#BestSum Problem 
#Brute Force

def bestSum(targetSum, numbers):
    #base case 
    if targetSum == 0: return []
    if targetSum <  0: return None
    
    shortestCombination = None
    
    for num in numbers:  # iterate through the numbers in the array for possible matches 
        result = bestSum(targetSum - num, numbers)
        if result != None:
            currentCombination =  [ *result, num]
            if ( shortestCombination == None or len(currentCombination) < len(shortestCombination)):
                shortestCombination = currentCombination
                
    return shortestCombination
# time complexity = O(n**m * m)
# space = O(m)

bestSum(100,[1,2,5,25])


#Memoization

def bestSum(targetSum, numbers, mem = {}):
    #base case 
    if targetSum in mem: return mem[targetSum]
    if targetSum == 0: return []
    if targetSum <  0: return None
    
    shortestCombination = None
    
    for num in numbers:  # iterate through the numbers in the array for possible matches 
        result = bestSum(targetSum - num, numbers)
        if result != None:
            currentCombination =  [ *result, num]
            if ( shortestCombination == None or len(currentCombination) < len(shortestCombination)):
                shortestCombination = currentCombination
    mem[targetSum] = shortestCombination
    return mem[targetSum]
# time complexity = O(n**m * m)
# space = O(m)

# Or, 
# Using the dp approch 
# using memoization 
def bestSum(targetSum, numbers, mem = {}):
    #base case 
    if targetSum in mem: return mem[targetSum]
    if targetSum == 0: return []
    if targetSum <  0: return None
    
    mem[targetSum] = None
    
    for num in numbers:  # iterate through the numbers in the array for possible matches 
        result = bestSum(targetSum - num, numbers, mem)
        if result != None:
            currentCombination =  [ *result, num]
            if ( mem[targetSum] == None or len(currentCombination) < len(mem[targetSum])):
                mem[targetSum] = currentCombination
                
    return mem[targetSum]
# time complexity = O(n**m * m)
# space = O(m)

#Tabulation

def bestSum(targetSum, llist):
    table = [None] * (targetSum + 1)# Create a table of (targetSum length + 1) and init with some default vlaue based on the return vlaue 
    table[0] = []  # Seed values by making trival sub problem. Given any array it is possible to generate 0
    
    for i in range(targetSum +1):  # iteration and the logic 
        if(table[i] is not None):
            for j in llist:
                if (i+j) <= targetSum : 
                    current = table[i] + [j]
                    if table[i+j] is None or (len(table[i+j]) > len(current)): table[i+j] = current
    return table[targetSum]   #filter out the none in the final answer
# t = O(n*m**2)
# s = O(m**2)           

bestSum(8,[7,8,3,1])
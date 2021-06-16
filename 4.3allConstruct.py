#AllConstruct Problem
#Brute Force

def allConstruct(target, wordBank):
    #base cases
    if target == "" : return [[]]
    allWays = []
    for word in wordBank:
        try:
            if(target.index(word) == 0):
                suffix = target[len(word):]
                suffixWay = allConstruct(suffix, wordBank)   # returns the solution from one of the child node
                totalWay = [[word] + way for way in suffixWay]                  # pushes the array (solution) with the parent node to form a sub solution of that parent target 
                if totalWay:
                    allWays.extend(totalWay)            # pushes the sub-solution to the root and obtain one of the ways
                
        except:None
    return allWays


#Memoization

def allConstruct(target, wordBank, mem={}):
    #base cases
    if target in mem: return mem[target]
    if target == "" : return [[]]
    
    result = []
    
    for word in wordBank:
        try:
            if(target.index(word) == 0):
                suffix = target[len(word):]
                suffixWay = allConstruct(suffix, wordBank, mem)   # returns the solution from one of the child node
                totalWay = [[word] + way for way in suffixWay]                  # pushes the array (solution) with the parent node to form a sub solution of that parent target 
                result.extend(totalWay)            # pushes the sub-solution to the root and obtain one of the ways
                
        except:None
    mem[target] = result
    return mem[target]

allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","eee","eeeeeeeeee","eeeeeeeeeeee","e"])


#Tabulation

def allConstruct(target, wordBank):
    #table = [[]]* (len(target) + 1) # do not use this, this is a trap. Just map it using a for loop, this only creates the illusion that it has created list of empty list.
    table = [[] for _ in range(len(target) + 1)]# Create a table of (targetSum length + 1) and init with some default vlaue based on the return vlaue 
    table[0] = [[]] # Seed values by making trival sub problem. Given any array it is possible to generate 0
    
    for i in range(len(target)):
        for word in wordBank:
            if(target[i: i + len(word)] == word): 
                newCombination = [ prevCombination + [word] for prevCombination in table[i]] # take the (combination present in the current cell) along with the current word
                table[i + len(word)].extend(newCombination) # Push the new combination to the new target
    return table[-1]
# time complexity = O(n*m**m)
# space = O(m**m) 


allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])

# CountConstruct Problem
# Brute Force

def countConstruct(target, wordBank):
    #base case 
    if target == '': return 1
    totalCounter = 0
    for word in wordBank:
        try:
        
            if target.index(word) == 0:          # ie. check whether the sub-string is present in the target string
                                                 # And, importantly make sure that it is a prefix only.(From the tree diagram)
                    sufix = target[len(word):]    # List slicing, slice the prefix from the list so that,
                                                 #next substring is the prefix for futre recurssion
                    counter = countConstruct(sufix,wordBank)
                    totalCounter += counter
                    
        except:None
                
    return totalCounter
            
# time complexity = O(n**m * m)
# space = O(m**2)   
     
#Memoization
def countConstruct(target, wordBank, mem = {}):
    #base case 
    if target in mem: return mem[target]
    if target == '': return 1
    totalCounter = 0
    for word in wordBank:
        try:
        
            if target.index(word) == 0:          # ie. check whether the sub-string is present in the target string
                                                 # And, importantly make sure that it is a prefix only.(From the tree diagram)
                    sufix = target[len(word):]    # List slicing, slice the prefix from the list so that,
                                                 #next substring is the prefix for futre recurssion
                    counter = countConstruct(sufix,wordBank, mem)
                    totalCounter += counter
            
        except:None
            
    mem[target] = totalCounter
    return totalCounter 
            
# time complexity = O(n**m * m)
# space = O(m**2)        

countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])
countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","eee","eeeeeeeeee","eeeeeeeeeeee","e"])

#Tabulation

def countConstruct(target, wordBank):
    table = [0] * (len(target) + 1)   # Create a table of (targetSum length + 1) and init with some default vlaue based on the return vlaue 
    table[0] = 1 # Seed values by making trival sub problem. Given any array it is possible to generate 0
    
    
    for i in range(len(target)):  # iteration and logic
        if table[i]:
            for word in wordBank:
                if (word == target[i: i + len(word)]):
                    table[i+len(word)] += table[i] 
     
    return table[len(target)]
# time complexity = O(n*m*m)
# space = O(m)             

countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])



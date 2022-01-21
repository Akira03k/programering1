import random
dc_first = ("Bat","Super", "Wonder", "Green", "Aqua", "Cat")
dc_last = ("man","woman","flash","lantern")
marvel_first = ("Spider", "Iron", "The", "Black", "Thor", "Captain", "Doctor", "Ant")
marvel_last = ("man", "hulk", "panther", "widow", "america", "strange")
gen1 = random.sample(dc_first, 1)
gen2 = random.sample(dc_last, 1)
gen3 = random.sample(marvel_first, 1)
gen4 = random.sample(marvel_last, 1)
mega1 = gen1 + gen3
mega2 = gen2 +gen4

firstn = random.sample(mega1, 1)
lastn = random.sample(mega2, 1)
def listToString(s): 
    str1 = ""   
    for ele in s: 
        str1 += ele    
    return str1 
print(listToString(firstn + lastn))

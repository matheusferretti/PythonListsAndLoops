theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def replaceNumber(x):
    if x == 1:
        return "wiki"
    else:
        return "woko"

mapping = list(map(replaceNumber , theBools))
print(mapping)

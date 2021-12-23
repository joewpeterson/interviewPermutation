

def myFunc(a, returnSets, returnMod = [], layer = 0):
    '''
    Take in array a, return a array of arrays (returnSets) which 
    contains all the permutations of the elements.

    Works by calling itself recursively
    '''

    for entry in a:
        if len(returnMod) <= layer :
            returnMod.append('')

        returnMod[layer] = entry
        
        if len(a) == 1:
            myMod = returnMod.copy()
            returnSets.append(myMod)

        else:
            b = a.copy()
            b.remove(entry)
            myFunc(b, returnSets, returnMod, layer + 1)


a = [1,2,3,4]
returnSets = []

myFunc(a, returnSets)

print(len(returnSets))
for entry in returnSets:
    print(entry)

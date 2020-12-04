import math

def minFallingPaht(sqrArray):
    storeAllMinimumValues    = [[10000 for c in range(len(sqrArray))]for r in range(len(sqrArray))]
    storeAllMinimumValues[0] = sqrArray[0]
    
    #max val = (lenght[max=100]*val[max=100])
    minimumSum = 10000

    for i in range(1, len(sqrArray)):
        for j in range(len(sqrArray)):
            #Check curr index + index above
            storeAllMinimumValues[i][j] = min(storeAllMinimumValues[i][j], sqrArray[i][j]+storeAllMinimumValues[i-1][j])

            if j - 1 >= 0:
                #Check curr index + index above and behind
                storeAllMinimumValues[i][j] = min(storeAllMinimumValues[i][j], sqrArray[i][j]+storeAllMinimumValues[i-1][j-1])

            if j + 1 < len(sqrArray):
                #Check curr index + index above and in front
                storeAllMinimumValues[i][j] = min(storeAllMinimumValues[i][j], sqrArray[i][j]+storeAllMinimumValues[i-1][j+1])
            
            if i == len(sqrArray)-1:
                #Last row contains min
                minimumSum = min(storeAllMinimumValues[i][j], minimumSum)
    
    return minimumSum

def palidromicSubstring(str):
    substrings = []
    counter    = 0

    for i in range(len(str)):
        substrings.append(str[i])
        counter+=1

        for j in range(len(substrings)-2, -1, -1):
            substrings[j] += str[i]
            
            if substrings[j][::-1] == substrings[j]:
                counter+=1

    return counter

class Pair:
    def __init__(self, data, count):
        self.data  = data
        self.count = count

def maximumPairOfChains(array):
    array.sort()
    chainPairs = []
    maximum    = 0

    for currentChain in array:
        chainPairs.append(Pair(currentChain, 1))

        for chainPair in chainPairs:
            if chainPair.data[1] < currentChain[0]:
                chainPair.data  = currentChain
                chainPair.count = chainPair.count + 1
                if chainPair.count > maximum:
                    maximum = chainPair.count
    
    return maximum
    
def arithmeticSlices(array):
    consecutive = 0
    count       = 0
    for i in range(2, len(array)):
        if array[i-1] - array[i-2] == array[i] - array[i-1]:
            consecutive += 1 
            count       += consecutive
        else:
            consecutive = 0
    
    return count

#Unable to get a working solution
def perfectSqr(n):    
    dict = {}
    for i in range(n + 1):
        dict[i] = []

    for i in dict:
        for j in range(i):
            if [j , i-j] in dict[i]:
                break
            dict[i].append([i - j, j])

    for i in range(n, -1, -1):
        stop    = True
        counter = 0
        key     = i
        while stop == True and key != 0:
            for j in dict[key]:
                if j[0] != 0 and j[1] != 0 and math.sqrt(j[0]) - math.floor(math.sqrt(j[0])) == 0 and math.sqrt(j[1]) - math.floor(math.sqrt(j[1])) == 0:
                    counter += 2
                    stop     = False
                elif j[0] != 0 and math.sqrt(j[0]) - math.floor(math.sqrt(j[0])) == 0:
                    key        = j[1]
                    counter += 1
                    break
                elif j[1] != 0 and math.sqrt(j[1]) - math.floor(math.sqrt(j[1])) == 0:
                    key       = j[0]
                    counter += 1
                    break
    
    return minimum

print("Question 1 Solution")
print(minFallingPaht([[4,3,2,1],[4,3,1,3],[3,1,7,8],[1,2,3,5]]))
print("Question 2 Solution")
print(arithmeticSlices([1,2,3,4,5,9,10,12,14]))
a = [[1,5], [2,3], [3,4], [4, 5], [6,7], [8,9], [10,11]]
print("Question 3 Solution")
print(maximumPairOfChains(a))
print("Question 4 Solution")
print(palidromicSubstring("abaab"))

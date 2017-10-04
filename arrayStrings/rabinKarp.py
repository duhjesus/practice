import time

#globals variables
alphaValues = {}

def initValue():
    global alphaValues
    alphaValues[" "] = 0
    for letter in range(97,123):
        alphaValues[chr(letter)]= letter - 96
    print(alphaValues)

def hashValue(theString):
    value = 0
    for char in theString:
        value += alphaValues[char]
    return value

def slowSearch(subString, bigString):
    indexList = []
    start = time.time()
    for i in bigString:
        for j in subString:
            if i != j:
                break
        if i == j: # broke because it matched, if it breaks we dont want to append if not a match
            indexList.append(i)
    end = time.time()
    return indexList, start, end 
def stillSlowSearch(subString, bigString):
    pass

def search(subString, bigString):
    subValue = hashValue(subString)
    for i in bigString:
        pass        

def main():
    B_string= "doe are hearing me"
    S_string = "ear"
    
    initValue()# give a value for each char
    stringValue = hashValue(S_string)# calculate hash value of string
    print("stringValue=", stringValue)
    indexList, start, end = slowSearch(S_string, B_string)
    print("indexList=",indexList, "time elapsed=", end-start)

    


if __name__ == "__main__":
    main()

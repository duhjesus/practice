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
    for i in range(0,len(bigString)-len(subString)):
        for j in range(0, len(subString)):
            tempi = i
            tempj = j
            if bigString[i+j] != subString[j]:
                break
        if bigString[tempi+tempj] == subString[tempj]:
            indexList.append(i)
    end = time.time()
    return indexList, start, end


    #for idxi, i in enumerate(bigString):
    #    if (len(bigString)-idxi) >len(subString):
    #        for idxj,j in enumerate(subString):
    #            print("i=",bigString[idxi+idxj]," & j=",subString[idxj])
    #            temp = j
    #            tempidxi = idxi
    #            if bigString[idxi+idxj] != subString[idxj]:
    #                break            
    #        print("***********")
    #        if bigString[idxi+idxj] == temp: # broke because it matched, if it breaks we dont want to append if not a match 
    #            indexList.append(tempidxi)
    #
    #end = time.time()
    #return indexList, start, end

def stillSlowSearch(subString, bigString):
    subValue = hashValue(subString)
    indexList = []
    curr_sum = 0
    start = time.time()
    for i in range(0,len(bigString)-len(subString)):
        for j in range(0,len(subString)):
            curr_sum += hashValue(bigString[i+j])
        
        if subValue == curr_sum:
            indexList.append(i)
        curr_sum = 0 

    end = time.time()
    return indexList, start, end
        
def search(subString,bigString):
    subValue = hashValue(subString)
    indexList = []
    curr_sum = 0
    start = time.time()
    for i in range(0, len(subString)):
        curr_sum += hashValue(bigString[i])
 
    if curr_sum == subValue:
        indexList.append(0)

    for i in range(1, len(bigString)-len(subString)):
        curr_sum = curr_sum - hashValue(bigString[i-1])+hashValue(bigString[i+len(subString)-1])

        if curr_sum == subValue:
            indexList.append(i)
    end = time.time()

    return indexList, start, end

def main():
    B_string= "doe are hearing me"
    S_string = "ear"
    
    initValue()# give a value for each char
    stringValue = hashValue(S_string)# calculate hash value of string
    print("stringValue=", stringValue)
    indexList, start, end = slowSearch(S_string, B_string)
    print("SLOW METHOD: indexList=",indexList, "time elapsed=", end-start)
    indexList, start, end = stillSlowSearch(S_string, B_string)
    print("STILL SLOW METHOD: indexList=",indexList, "time elapsed=", end-start)
    indexList, start, end = search(S_string, B_string)
    print("Rabin-karp aka FAST METHOD: indexList=", indexList, "time elapsed=", end-start) 
    print("TODO: incorporate rabin fingerprint which is just weight")



if __name__ == "__main__":
    main()

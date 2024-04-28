# Python algorithm

# Anagram algorithm
# Using Lists

def anagramVersion1():
   
    wordInput1 = "cover"
    # wordInput2 = "crovs"
    wordInput2 = "crove"
    
    print("This version of an anagram Checker uses python lists.")
    print(f"Are \"{wordInput1}\" and \"{wordInput2}\" anagrams?")

    wordList1 = sorted(list(wordInput1))
    wordList2 = sorted(list(wordInput2))

    listCount = 0
    if(len(wordList1) == len(wordList2)):

        for i in range(0, len(wordList1)):
            if(wordList1[i] == wordList2[i]):
                listCount += 1
                continue
            else:
                print("These words are not anagrams")
                break
        if(listCount == len(wordList1)):
            print("These words are anagrams")
    else:
        print("These words are not anagrams")

    # print("Meow")
    # print(str(wordList1) + " length: " + str(len(wordList1)))
    # print(str(wordList2) + " length: " + str(len(wordList2)))
    print("Anagram Version 1 finished")
anagramVersion1()
print(" ")


# Anagram algorithm
# Using Dictionary

def anagramVersion2():

    wordInput1 = "covers"
    wordInput2 = "crovsl"
    # wordInput2 = "crovess"
    # wordInput2 = "croves"
    tempDict = {}
    isLetterNotPresent = 0
    
    print("This version of an anagram Checker uses python dictionaries.")
    print(f"Are \"{wordInput1}\" and \"{wordInput2}\" anagrams?")
    if(len(wordInput1) == len(wordInput2)):
        # build dictionary
        for element in wordInput2:
            if element in tempDict:
                tempDict[element] += 1
            else:
                tempDict[element] = tempDict.setdefault(element, 1)

        # search dictionary
        for element in wordInput2:
            if element in wordInput1:
                # print("yes " + element)
                continue
            else:
                isLetterNotPresent += 1
                # print("no " + element)
        
        # check if any odd letters
        if isLetterNotPresent > 0:
            print("These words are not anagrams")
        else:
            print("These words are anagrams")
    else:
        print("These words are not anagrams")
    
    # print("Meow2")
    print("Anagram Version 2 finished")
anagramVersion2()
print(" ")



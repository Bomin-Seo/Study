#### ANSWER: START
import random

def calculateSecond(day,hour,minute,second):
    result = day*86400 + hour*3600 + minute*60 + second
    return result

def reverseString(str1):
    str1 = str1[::-1]
    return str1

def calcTwoCharactersFromString(iString, iCh1, iCH2):
    ans1 = iString.count(iCh1)
    ans2 = iString.count(iCH2)
    return ans1 + ans2

def calcTwoCharactersFromStringV2(iString, iCh1, iCH2):
    if iCh1 == iCH2:
        return -1
    else:
        ans1 = iString.count(iCh1)
        ans2 = iString.count(iCH2)
        return ans1 + ans2
def calcTwoCharactersFromStringV3(iString, iChList):
    ans1 = 0
    for i in range(len(iChList)):
        ans1 += iString.count(iChList[i])
        i += 1
    return ans1

def mergeAndSortTwoList(list1,list2):
    result = list1 + list2
    result = set(result)
    result = list(result)
    result.sort()
    return result

def mergeAndSortTwoListReverse(list1,list2):
    result = list1 + list2
    result = set(result)
    result = list(result)
    result.sort(reverse=True)
    return result

def searchMatchedCharacter(strlist,ch):
    result = []
    for i in range(len(strlist)):
        if strlist[i].startswith(ch):
            result.append(strlist[i])
    result.sort()
    return result

def makeRandomTenIntegers():
    result = []
    for i in range(10):
        num = random.randint(1,10)
        while num in result:
            num = random.randint(1, 10)
        result.append(num)
    return result

def makeRandomIntegersExtended(iStart, iEnd):
    if iStart <= 0 or iEnd <= 0 or iEnd == iStart or iStart < iEnd:
        return -1
    else:
        result = []
        for i in range(iStart - iEnd + 1):
            num = random.randint(iEnd, iStart)
            while num in result:
                num = random.randint(iEnd, iStart)
            result.append(num)
    return result

#### ANSWER: END

#### Self Scoring : Start ####

TotalScore = 0

try:
    if calculateSecond(1,1,1,2) == 90062:
        TotalScore += 5
        print("[Q01-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q01-failed.1] Score - ", TotalScore)
    if calculateSecond(2,3,4,5) == 183845:
        TotalScore += 5
        print("[Q01-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q01-failed.2] Score - ", TotalScore)
except:
    print("[Q01-failed.except] Score - ", TotalScore)

try:
    if reverseString("Hello World!!") == '!!dlroW olleH':
        TotalScore += 5
        print("[Q02-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q02-failed.1] Score - ", TotalScore)
    if reverseString("Welcome to Hell!!") == '!!lleH ot emocleW':
        TotalScore += 5
        print("[Q02-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q02-failed.2] Score - ", TotalScore)
except:
    print("[Q02-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromString("You only live once", 'o', 'o') == 6:
        TotalScore += 5
        print("[Q03-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q03-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromString("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q03-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q03-failed.2] Score - ", TotalScore)
except:
    print("[Q03-failed.except] Score - ", TotalScore)

try: 
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'o') == -1:
        TotalScore += 5
        print("[Q04-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q04-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q04-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q04-failed.2] Score - ", TotalScore)
except:
    print("[Q04-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromStringV3("You only live once", ['a', 'o', 'o']) == 6:
        TotalScore += 10
        print("[Q05-PASSED] Score - ", TotalScore)
    else:
        print("[Q05-failed.try] Score - ", TotalScore)
except:
    print("[Q05-failed.except] Score - ", TotalScore)

try:
    if mergeAndSortTwoList([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 24, 34, 55]:
        TotalScore += 10
        print("[Q06-PASSED] Score - ", TotalScore)
    else:
        print("[Q06-failed.except] try - ", TotalScore)
except:
    print("[Q06-failed.except] Score - ", TotalScore)

try: 
    if mergeAndSortTwoListReverse([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [55, 34, 24, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        TotalScore += 10
        print("[Q07-PASSED] Score - ", TotalScore)
    else:
        print("[Q07-failed.try] Score - ", TotalScore)
except:
    print("[Q07-failed.except] Score - ", TotalScore)

try:
    kingdoms = ['Bacteria', 'Protozoa','Chromista','Plantae','Fungi','Animalia']
    if searchMatchedCharacter(kingdoms, 'P') == ['Plantae', 'Protozoa']:
        TotalScore += 10
        print("[Q08-PASSED] Score - ", TotalScore)
    else:
        print("[Q08-failed.try] Score - ", TotalScore)
except:
    print("[Q08-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomTenIntegers()
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        TotalScore += 10
        print("[Q09-PASSED] Score - ", TotalScore)
    else:
        print("[Q09-failed.try] Score - ", TotalScore)
except:
    print("[Q09-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomIntegersExtended(20,1)
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        TotalScore += 10
        print("[Q10-PASSED] Score - ", TotalScore)
    else:
        print("[Q10-failed.try] Score - ", TotalScore)
except:
    print("[Q10-failed.except] Score - ", TotalScore)

#### Self Scoring : End ####

print("==>> FINAL SCORE: ", TotalScore)

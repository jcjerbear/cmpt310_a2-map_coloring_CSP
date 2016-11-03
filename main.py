from mapColoring import *

# data structures i am using
inputList = []  # put data from the input.txt into list inputList
numList = []  # replacing the tokens '(' and ')' in list x as empty and append the strings into the list numList
colorList = []  # list for storing available colors
visitedList = dict()  # recording visited keys/nodes and its assigned color
graphDict = dict()  # graph as a dictionary
MRVDict = dict()  # MRV dictionary
degreeDict = dict()  # degree dictionary

instance = mapColoring()

# put data from the input.txt into list x
file = open('input.txt', 'r')
firstLine = file.readline()
for line in file:
    inputList.append(line)
# print("the inputList")
# print(inputList)  # x is a list containing multiple strings

numList = instance.parser(inputList)
graphDict = instance.graph(numList)
colorList = instance.colorList(firstLine)
MRVDict = instance.MRV(numList, colorList)
degreeDict = instance.degree(graphDict)
'''
print("MRVList")
MRVList = sorted(MRVDict, key=lambda k: len(MRVDict[k]))
print(MRVList)

print("MRVDict")
print(MRVDict)
'''
# print("degreeList")
degreeList = sorted(degreeDict, key=lambda k: degreeDict[k])
# print(degreeList)

# print("degreeDict")
# print(degreeDict)
# print("this shows that after sorted() is invoked, the dictionary is still not sorted itself, but it gives out a list\n")

# print("enter while loop")
while True:
    if (bool(MRVDict) == False):
        break

    # print("MRVList")
    MRVList = sorted(MRVDict, key=lambda k: len(MRVDict[k]))
    # print(MRVList)

    #
    listtoDegree = []
    compareVal = MRVList[0]
    for key in MRVList:
        if (len(MRVDict[key]) == len(MRVDict[compareVal])):
            listtoDegree.append(key)
        else:
            break
    # choose the right node
    maxDegree = 0
    # print("listtoDegree", listtoDegree)
    for key in listtoDegree:
        # print("print key in listtoDegree", key)
        if (degreeDict[key] >= int(maxDegree)):
            maxDegree = degreeDict[key]
            chosenNode = key

    # choose the first available color of the color domain of the chosen node as the color of the node
    for key in MRVDict:
        if (key == chosenNode):
            chosenColor = MRVDict[key][0]

    # update chosen node and chosen color into the visitedList
    visitedList.update({chosenNode: chosenColor})

    # update dictionary data
    # delete key row of MRVDict with key value of chosenNode
    del MRVDict[chosenNode]

    # also remove chosenColor from neighbours color domain
    chosennodeList = []
    chosennodeList.append(chosenNode)
    # grab the neighbour list of the chosen node's from graphDict
    # print("print chosennodeList", chosennodeList)
    neighbourList = [graphDict[x] for x in chosennodeList]
    # print("print neighbourList before flatten", neighbourList)
    # flatten the list of lists out
    neighbourList = [item for sublist in neighbourList for item in sublist]
    # print("print neighbourList after flatten", neighbourList)
    # now we have the list of neighbours we can use to compare with
    # print('before')
    # print(MRVDict)
    for nkey in neighbourList:
        for Mkey in MRVDict:
            # print("MRVDict.keys() general", MRVDict.keys())
            if (nkey == Mkey):  # here we find the neighbour rows
                # print(Mkey, ':', MRVDict[nkey])

                if chosenColor in MRVDict[nkey]:
                    # print(MRVDict[nkey])
                    MRVDict[nkey].remove(chosenColor)
                '''
                for element in MRVDict[Mkey]:
                    print(Mkey,':',element)
                    if(chosenColor == element):
                        MRVDict[Mkey].remove(chosenColor)
                '''
    # print("chosenNode", chosenNode)
    # print("chosenColor", chosenColor)
    # print("MRVDict", MRVDict)
    # print("visitedList", visitedList)

print("Region    :    Color")
for key, value in visitedList.items():
    if(key == '10'):
        print(key, '       :   ', value)
    else:
        print(key, '        :   ', value)


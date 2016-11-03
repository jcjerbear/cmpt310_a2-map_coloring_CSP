# methods
from copy import  deepcopy

class mapColoring():
    def edgesGen(self, graph):
        edges = []
        for node in graph:
            for neighbour in graph[node]:
                edges.append((node, neighbour))
        return edges

    def colorList(self, firstLine):
        colorList = []
        firstLine = firstLine.replace('(', '').split()
        firstLine = int(firstLine[1])
        for i in range(0, firstLine):
            colorList.append(i)
        # print(colorList)
        return colorList

    def parser(self, inputList):
        numList = []  # replacing the tokens '(' and ')' in list x as empty and append the strings into the list numList
        # replacing the tokens '(' and ')' in list inputList as empty and append the strings into the list numList
        # print("\n")
        for string in inputList:
            numList.append(string.replace('(', '').replace(')', '').split())
        # print("numList with empty set still")
        # print(numList)  # numList is a list containing multiple sub-lists
        '''
        numList = []
        for string in x:
            numList.append([ int(item) for item in string if item.isdigit() ])
        print(numList)
        '''
        # eliminate out the last empty list
        numList = [x for x in numList if x != []]
        # print("numList without empty set")
        # print(numList)  # now the numList is a list containing multiple lists w/o any empty lists
        return numList

    def graph(self, numList):
        graph = dict()  # graph as a dictionary
        # constructing graph as a dictionary
        # print("\n")
        # print("lists putting into the graph")
        for lists in numList:
            # print(lists)
            graph.update({lists[0]: lists[1:]})
        # print("\n")
        # print("show the graph")
        # print(graph)
        return graph

    def MRV(self, numList, colorList):
        MRV = dict()
        # constructing MRV dictionary
        for lists in numList:
            MRV.update({lists[0]: deepcopy(colorList)})
        # print("\n")
        # print("show MRVDict")
        # print(MRV)
        return MRV

    def degree(self, graph):
        degree = dict()
        # constructing degree dictionary
        for key, value in graph.items():
            degree.update({key: len(value)})
        # print("show degreeDict")
        # print(degree)
        return degree

    def findMaxDegree(self, degree):
        for key, value in graph.items():
            degree.update({key: len(value)})

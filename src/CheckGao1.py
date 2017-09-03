#!coding:utf8

'''
descriptions: none
author: yqq
date: 2017/9/3 11:07
'''
from collections import  OrderedDict

gSubDict= {
"语":5,\
"数":5,\
"英":5,\
"物":3,\
"化":3,\
"生":2,\
"政":2,\
"历":2,\
"地":2,\
"音":1,\
"体":2,\
"美":1,\
"信":1,
}



def Check(classDict):
    for classNo, classSubList in classDict.items():
        for sub, count in gSubDict.items():
            if classSubList.count(sub) > count:
                print("{0} -> {1} 多了 {2}节".format(classNo, sub, classSubList.count(sub) - count))
            elif classSubList.count(sub) < count:
                print("{0} -> {1} 少了 {2}节".format(classNo, sub, count - classSubList.count(sub) ))
            else:
                pass


def ReadTabFile(inFilePath, classDict):

    with open(inFilePath, "r") as inFile:
        lineList = inFile.readlines()
        for line in lineList:
            splitList = line.split('\t')
            classDict[splitList[0]] = splitList[1:]
    pass


def main():

    classDict = OrderedDict()
    ReadTabFile("../txt/Gao1.txt", classDict)
    Check(classDict)

    pass

if __name__ == '__main__':

    main()

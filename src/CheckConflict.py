#!coding:utf8

'''
descriptions: 检查课表是否有冲突 
author: yqq
date: 2017/9/3 13:24
'''

from collections import OrderedDict



gKeyNameList = [\
"语",\
"数",\
"英",\
"物",\
"化",\
"生",\
"政",\
"历",\
"地",\
"音",\
"体",\
"美",\
"信",\
"班",
]


gClassDict = OrderedDict()
'''
gClassDict数据结构:

{
    classNo1 : {课程1:老师1, 课程2:老师2, 课程3:老师3, ....},
    classNo2 : {....}
    ....
}

'''


def Show():

    for classNo, subDict in gClassDict.items():
        print("{0}".format(classNo)),
        for subName, tName in subDict.items():
            print("({0}->{1})".format(subName, tName)),
        print("\n")
    pass


def ReadTabFile():

    with open("../txt/TeacherCourse.txt", "r") as inFile:
        lineList = inFile.readlines()
        for line in lineList:
            splitList = line.split('\t')
            tmpDict = OrderedDict()
            tmpClassNo = splitList[0]
            teacherNameList = splitList[1: -1]

            #for teacher in teacherNameList:
            #    print("{0}".format(teacher)),
            #print("\n")

            for index in range(len(teacherNameList)):
                tmpDict[gKeyNameList[index]] = teacherNameList[index]
            gClassDict[tmpClassNo] = tmpDict

    #print(len(gClassDict))

    pass


def CheckGao1Dict(Gao1Dict):
    '''
    :param Gao1Dict:  高一课表字典 
    :return: 无
    
    Gao1Dict 数据结构:
    
    {
        classNo1 : [(老师名, 课程名, 第节课), (老师名, 课程名, 第节课), ..],
        classNo2 : [(老师名, 课程名, 第节课), (老师名, 课程名, 第节课), ..],
        ....
    }
    
    '''

    CourseCount = len(Gao1Dict[Gao1Dict.keys()[0]])

    for index in range(CourseCount):
        tmpList = []
        for classNo, tmpTupleList in Gao1Dict.items():
            teacherName = tmpTupleList[index][0]
            if teacherName not in tmpList:
                tmpList.append(teacherName)
            else:
                print("{0}->第{1}节,{2},{3}".format( classNo,  index+1, tmpTupleList[index][0], tmpTupleList[index][1]))

    pass


def ReadGao1Table():
    '''
    读高一课表, 返回Gao1Dict, Gao1Dict的数据结构, 见上文
    :return:  Gao1Dict
    '''

    Gao1Dict = OrderedDict()
    with open("../txt/Gao1.txt", "r") as inFile:
        lineList = inFile.readlines()
        for line in lineList:
            splitList = line.split('\t')
            tmpClassNo = splitList[0]
            tmpSubList = splitList[1 : -1]
            tmpList = []

            index = 1
            for subName in tmpSubList:

                teacherName = ""
                try:
                    teacherName = gClassDict[tmpClassNo][subName]
                except:
                    print(tmpClassNo),
                    print(subName)
                    exit(1)
                tmpList.append((teacherName, subName, index))
                index += 1
            Gao1Dict[tmpClassNo] = tmpList

    return Gao1Dict




def main():

    ReadTabFile()
    #Show()

    CheckGao1Dict(ReadGao1Table())

    pass

if __name__ == '__main__':

    main()

from datetime import datetime
import pandas as pd

def makeRecord(name, Deadline, worknum, priority):
    worklist = []
    worklist.append(name, Deadline, worknum, priority)
    return worklist

def checkDeadline(list):
    Deadline = str(list[1])
    year = int(Deadline[:4])
    month = int(Deadline[4:6])
    day = int(Deadline[6:])
    today = int(str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day))
    if year != 2021:
        return False
    elif month not in range(1, 13):
        return False
    elif day not in range(1,32):
        return False
    elif today > int(Deadline):
        return False
    return True

def checkPriority(inputlist):
    priority = inputlist[3]
    if priority not in [1,2,3]:
        return False
    else:
        return True

class ToDoList:
    def __init__(self):
        self.today = int(str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day))
        self.worknumlist = []
        self.namelist =[]
        self.deadlinelist = []
        self.todolist=[]

    def addItem(self, worklist):
        if checkPriority(worklist) == False or checkDeadline(worklist) == False:
            return False
        else:
            if worklist[2] not in self.worknumlist:
                self.worknumlist.append(worklist[2])
            else:
                return False
            self.namelist.append(worklist[0])
            self.deadlinelist.append(worklist[1])
            self.todolist.append(worklist)
            return len(self.worknumlist)

    def getEarliestItem(self):
        todolist = self.todolist
        prioritylist = sorted(todolist, key = lambda key : key[1])
        result = []
        for i in range(len(prioritylist)):
            if prioritylist[0][1] == prioritylist[i][1]:
                result.append(prioritylist[i])
        result = sorted(result, key=lambda key : key[3])
        return result[0]

    def getItemByName(self, name):
        todolist = self.todolist
        prioritylist = sorted(todolist, key=lambda key: key[3])
        prioritylist = sorted(prioritylist, key=lambda key: key[1])
        result = []
        if name not in self.namelist:
            return False
        else:
            for i in range(len(prioritylist)):
                if name == prioritylist[i][0]:
                    result.append(prioritylist[i])
            return result

    def getItemsByEDF(self, bool = True or False):
        todolist = self.todolist
        prioritylist = sorted(todolist, key = lambda key : key[3])
        prioritylist = sorted(prioritylist, key = lambda key : key[1])
        if bool == True:
            return prioritylist
        else:
            return prioritylist[::-1]

    def getItemDeadline(self, worknum):
        if worknum not in self.worknumlist:
            return False
        else:
            worknumindex = self.worknumlist.index(worknum)
            return self.todolist[worknumindex][1]

    def deferDeadline(self, worknum, deferday):
        deadline = str(self.getItemDeadline(worknum))
        year = int(deadline[:4])
        month = int(deadline[4:6])
        day = int(deadline[6:])
        day += deferday
        if day > 31:
            month += 1
            day = day % 31
            if month > 12:
                year +=1
                month = month % 12
        if 1 < month < 10:
            momth = '0' + str(month)
        if 1 < day < 10:
            day = '0' + str(day)
        result = int(str(year) + str(month) + str(day))
        return result

    def writeFile(self):
        todolist = self.todolist
        prioritylist = sorted(todolist, key=lambda key: key[3])
        prioritylist = sorted(prioritylist, key=lambda key: key[1])
        df = pd.DataFrame(prioritylist)
        df.to_csv("output.csv", index=False, header=False)
class MySelfClass:
    def __init__(self):
        self.studentid = "9900000029"
        self.birthday = "20010203"

    def getStudentID(self):
        return self.studentid

    def getBirthday(self):
        return  self.birthday

    def getStudentIDByInteger(self):
        return int(self.studentid)

    def getBirthdayByIntegerSum(self):
        result = 0
        for i in range(len(self.birthday)):
            result += int(self.birthday[i])
        return result

    def getMaxInteger(self):
        result = []
        studentid = self.getStudentID()
        birthday = self.getBirthday()
        for i in range(len(studentid)):
            result.append(int(i))
        for j in range(len(birthday)):
            result.append(int(j))
        ans = max(result)
        return ans

    def getAverageInteger(self):
        result = []
        studentid = self.getStudentID()
        birthday = self.getBirthday()
        length = len(studentid) + len(birthday)
        for i in range(len(studentid)):
            result.append(int(studentid[i]))
        for j in range(len(birthday)):
            result.append(int(birthday[j]))
        ans = sum(result) / length
        return ans

    def getBirthdayByMonth(self):
        birthday = self.getBirthday()
        month = int(birthday[4:6])
        monthtable = {1 : 'JAN', 2:'FEB', 3:'MAR', 4:"APR", 5: 'MAY', 6:'JUN', 7 : 'JUL',
                      8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
        return monthtable[month]

class MyRecordClass:
    def __init__(self):
        self.studentid = "2020101111"
        self.deadline = "20211231"
        self.subnum = "A001"
        self.priority = 1
        self.recordlist = []
        self.subnumlist = []

    def makeRecord(self, studentid, deadline, subnum, priority):
        record = []
        if type(studentid) != str or type(deadline) != str or type(subnum) != str or type(priority) != int:
            return -1
        elif len(studentid) != 10 or len(deadline) != 8 or len(subnum) != 4 or priority not in [1,2,3]:
            return -2
        else:
            self.studentid = studentid
            self.deadline = deadline
            self.subnum = subnum
            self.priority = priority
            record.append(self.studentid)
            record.append(self.deadline)
            record.append(self.subnum)
            record.append(self.priority)
            self.recordlist.append(record)
            self.subnumlist.append(subnum)
            return self.recordlist[-1]

    def checkDelay(self, subnum, today):
        if subnum not in self.subnumlist:
            return -1
        else:
            subindex = self.subnumlist.index(subnum)
            deadline = int(self.recordlist[subindex][1])
            if deadline < int(today):
                return True
            else:
                return False

    def deferDeadline(self, subnum, deferday):
        if subnum not in self.subnumlist:
            return -1
        elif deferday > 14:
            return -2
        else:
            subindex = self.subnumlist.index(subnum)
            deadline = self.recordlist[subindex][1]
            year = int(deadline[:4])
            month = int(deadline[4:6])
            day = int(deadline[6:])
            day += deferday
            if day > 31:
                month += 1
                day = day % 31
                if month > 12:
                    month = month % 12
                    year += 1
            if day < 10:
                day = '0' + str(day)
            if month < 10 :
                month = '0' + str(month)
            result = str(year) + str(month) + str(day)
            self.recordlist[subindex][1] = result
            return self.recordlist[subindex]






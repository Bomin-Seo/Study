from MySelfClass import *

if __name__ == '__main__':
    obj = MySelfClass()
    print(obj.getStudentID())
    print(obj.getBirthday())
    print(obj.getBirthdayByIntegerSum())
    print(obj.getMaxInteger())
    print(obj.getAverageInteger())
    print(obj.getBirthdayByMonth())

    record = MyRecordClass()
    record.makeRecord("9900000029","20210718","A001",1)
    print(record.recordlist)
    record.makeRecord("9900000030", "20211230", "A002", 2)
    print(record.recordlist)
    print(record.checkDelay("A001", "20210718"))
    print(record.deferDeadline("A002", 13))

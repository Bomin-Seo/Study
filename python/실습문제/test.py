from todolist import *

work1 = ["kim", 20211201, "A001", 2]
work2 = ["seo", 20211202, "A003", 3]
work3 = ["lee", 20211201, "A004", 1]
work4 = ["kim", 20211204, "A002", 2]
work5 = ["lee", 20211225, "A006", 1]

if __name__ == "__main__":
    todolist = ToDoList()
    todolist.addItem(work1)
    todolist.addItem(work2)
    todolist.addItem(work3)
    todolist.addItem(work4)
    todolist.addItem(work5)
    earliesitem = todolist.getEarliestItem()
    print(earliesitem)
    getname = todolist.getItemByName("jeong")
    print(getname)
    getname = todolist.getItemByName("lee")
    print(getname)
    getedf = todolist.getItemsByEDF(True)
    print(getedf)
    getedf = todolist.getItemsByEDF(False)
    print(getedf)
    getdeadline = todolist.getItemDeadline("A006")
    print(getdeadline)
    deferdeadline = todolist.deferDeadline("A006", 13)
    print(deferdeadline)
    todolist.writeFile()
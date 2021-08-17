
from _datetime import datetime

from services.classtask import task
from services.classuser import user
from userdef import insertuser
from userdef import inserttask
from userdef import *


ask = input( """a.insert user
b.insert task 
c.update priority 
d.update notes
e.update bookmark
f.update status
g.all tasks
h.all tasks users
i.tasks based on status
j:assign task: """)


if ask == "a":
    userid = input("enter userid :")
    username = input("enter username:")
    contactno = input("contact number:")
    role = input("role:")
    mailid = input("mailid:")
    dob = input("enter dob:")
    createdon = input("created on:")
    modifiedon = input("modified on :")
    u = user(userid, username, contactno, role, mailid, dob, createdon, modifiedon)
    insertuser(u)

elif ask == "b":
    taskid = input("enter taskid:")
    name = input("enter name:")
    description = input("description:")
    status = input("status:")
    priority = input("priority:")
    notes = input("notes:")
    bookmark = input("bookmark:")
    ownerid = input("enter ownerid:")
    creatorid = input("enter creatorid:")
    createon = input("createdon:")
    modifyon = input("modifiedon:")
    t = task(taskid, name, description, status, priority, notes, bookmark, ownerid, creatorid, createon, modifyon)
    inserttask(t)


elif ask == "c":
    taskid = input("enter taskid: ")
    priority = input("enter priority:")
    updatepriority(taskid, priority)

elif ask == "d":
    taskid = input("enter taskid:")
    notes = input("enter the notes:")
    updatenotes(taskid, notes)

elif ask == "e":
    taskid = input("enter taskid:")
    bookmark = input("enter bookmark:")
    updatebookmark(taskid, bookmark)

elif ask == "f":
    taskid = input("enter taskid:")
    status = input("enter status:")
    updatenotes(taskid, status)

elif ask == "g":
    alltasks()

elif ask == "h":
    userid = input("Enter userid: ")
    print(alltaskuser(userid))


elif ask == "i":
    status = input("status:")
    print(tasksbasedonstatus(status))



elif ask == "j":
    userid = input("enter userid:")
    taskid = input("enter taskid:")
    assigntask(userid, taskid)

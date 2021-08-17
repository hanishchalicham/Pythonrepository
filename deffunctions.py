
from _datetime import datetime

import mysql.connector

from classuser import user
from classtask import task
import smtplib
import getpass



def connectToDB():
    mydb = mysql.connector.connect(host="localhost", user="root", password="sctshanish1999", database="jobtracking")
    return mydb


def createuser():
    mydb = connectToDB()
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE user (userid INT, username VARCHAR(25), contactno VARCHAR(25), role VARCHAR(45), mailid VARCHAR(45), dob VARCHAR(45), createdon  VARCHAR(45), modifiedon VARCHAR(45))")
    mydb.commit()


def createtask():
    mydb = connectToDB()
    mycursor = mydb.cursor()
    mycursor.execute(
        "CREATE TABLE task (taskid INT, name VARCHAR(25), description VARCHAR(25), status VARCHAR(20), priority INT, "
        "notes VARCHAR(25), bookmark VARCHAR(25), ownerid INT, creatorid INT, createon VARCHAR(25), "
        "modifyon VARCHAR(25))")
    mydb.commit()



def inserttask(task):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "insert into task (taskid,name,description,status,priority,notes,bookmark,ownerid,creatorid,createon,modifyon) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (task.taskid, task.name, task.description, task.status, task.priority, task.notes, task.bookmark, task.ownerid, task.creatorid, task.createon, task.modifyon)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()


#t = task(4, "Harry", "sonatasoftware", "single", 3, "hello", "right", 22, 33, datetime.now(), datetime.now())
#inserttask(t)


def insertuser(user):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "insert into user (userid,username,contactno,role,mailid,dob,createdon,modifiedon) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (user.userid, user.username, user.contactno, user.role, user.mailid, user.dob, user.createdon, user.modifiedon)
    # val = ("Ganesh", "ganesh@sonata.com", "999999999")
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()


#u = user(4, "Hanish", "999999999", "TTS", datetime.now(), datetime.now(), datetime.now())
#insertuser(u)

def updatepriority(taskid, priority):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task SET priority=%s WHERE taskid = %s"
    val = (priority, taskid)
    mycursor.execute(sql, val)
    mydb.commit()


#updatepriority(16,2)


def updatenotes(taskid, notes):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task SET notes=%s WHERE taskid = %s"
    val = (notes, taskid)
    mycursor.execute(sql, val)
    mydb.commit()


updatenotes(16,"hello")


def updatebookmark(taskid, bookmark):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task SET bookmark=%s WHERE taskid = %s"
    val = (bookmark, taskid)
    mycursor.execute(sql, val)
    mydb.commit()


#updatebookmark(16,"hello")


def updatestatus(taskid, status):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task SET status=%s WHERE taskid = %s"
    val = (status, taskid)
    mycursor.execute(sql, val)
    mydb.commit()


#updatestatus(16,"normal")


def alltasks():
    mydb = connectToDB()
    cursor = mydb.cursor()
    sql = 'SELECT name, taskid FROM task'
    cursor.execute(sql)
    all = cursor.fetchall()
    print(all)


def alltaskuser(userid):
    db = connectToDB()
    cursor = db.cursor()
    sql = "SELECT user.username as user, task.name as taskname FROM user INNER JOIN task ON user.userid = task.ownerid WHERE userid = %s"
    val = (userid, )
    cursor.execute(sql, val)
    all = cursor.fetchall()
    for i in all:
        return all


def tasksbasedonstatus(status):
    db = connectToDB()
    cursor = db.cursor()
    sql = "SELECT name FROM task WHERE status =%s"
    val = (status, )
    cursor.execute(sql, val)
    all = cursor.fetchall()
    for x in all:
        return all


def assigntask(userid, taskid):
    mydb = connectToDB()
    mycursor = mydb.cursor()
    sql = "UPDATE task SET ownerid=%s WHERE taskid = %s"
    val = (userid, taskid)
    mycursor.execute(sql, val)
    mydb.commit()
    sendermail = input("From: ")
    mailpassword = input("Password:")
    recmail = input("To: ")
    message = input("Message to be sent: ")
    sent = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    sent.login(sendermail, mailpassword)
    sent.sendmail(sendermail, recmail, message)
    sent.quit()

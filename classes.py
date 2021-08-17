class task:
    def __init__(self,taskid,name,description,status,priority,notes,bookmark,ownerid,creatorid,createon,modifyon):
        self.taskid = taskid
        self.name = name
        self.description = description
        self.status = status
        self.priority = priority
        self.notes = notes
        self.bookmark = bookmark
        self.ownerid = ownerid
        self.creatorid = creatorid
        self.createon = createon
        self.modifyon = modifyon
        
        
        
 class user:
    def __init__(self , userid, username, contactno, role, mailid, dob, createdon, modifiedon):
        self.userid = userid
        self.username = username
        self.contactno = contactno
        self.role = role
        self.mailid = mailid
        self.dob = dob
        self.createdon = createdon
        self.modifiedon = modifiedon
        
        

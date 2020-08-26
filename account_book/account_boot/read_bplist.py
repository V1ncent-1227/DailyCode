from bpylist import archiver

class TallySynModel:
    def __init__(self, week, time, typeID, amount, typeName,month,userID,expAmount,iconURL,year,type,date,sortName,iconName,inAmount,positiveAmount,dbStatus,serverID,remark):
        self.week = week
        self.time = time
        self.typeID = typeID
        self.amount = amount
        self.typeName = typeName
        self.month = month
        self.userID = userID
        self.expAmount = expAmount
        self.iconURL = iconURL
        self.year = year
        self.type = type
        self.date = date
        self.sortName = sortName
        self.iconName = iconName
        self.inAmount = inAmount
        self.positiveAmount = positiveAmount
        self.dbStatus = dbStatus
        self.serverID = serverID
        self.remark = remark


    @staticmethod
    def encode_archive(obj, archive):
        archive.encode('week', obj.week)
        archive.encode('time', obj.time)
        archive.encode('typeID', obj.typeID)
        archive.encode('amount', obj.amount)
        archive.encode('typeName', obj.typeName)
        archive.encode('month', obj.month)
        archive.encode('userID', obj.userID)
        archive.encode('expAmount', obj.expAmount)
        archive.encode('iconURL', obj.iconURL)
        archive.encode('year', obj.year)
        archive.encode('type', obj.type)
        archive.encode('date', obj.date)
        archive.encode('sortName', obj.sortName)
        archive.encode('iconName', obj.iconName)
        archive.encode('inAmount', obj.inAmount)
        archive.encode('positiveAmount', obj.positiveAmount)
        archive.encode('dbStatus', obj.dbStatus)
        archive.encode('serverID', obj.serverID)
        archive.encode('remark', obj.remark)


    @staticmethod
    def decode_archive(archive):
        week = archive.decode('week')
        time = archive.decode('time')
        typeID = archive.decode('typeID')
        amount = archive.decode('amount')
        typeName = archive.decode('typeName')
        month = archive.decode('month')
        userID = archive.decode('userID')
        expAmount = archive.decode('expAmount')
        iconURL = archive.decode('iconURL')
        year = archive.decode('year')
        type = archive.decode('type')
        date = archive.decode('date')
        sortName = archive.decode('sortName')
        iconName = archive.decode('iconName')
        inAmount = archive.decode('inAmount')
        positiveAmount = archive.decode('positiveAmount')
        dbStatus = archive.decode('dbStatus')
        serverID = archive.decode('serverID')
        remark = archive.decode('remark')
        return TallySynModel(week, time, typeID, amount, typeName,month,userID,expAmount,iconURL,year,type,date,sortName,iconName,inAmount,positiveAmount,dbStatus,serverID,remark)

archiver.update_class_map({'TallySynModel': TallySynModel})


objects = archiver.unarchive_file('2020_08_06.plist')
for obj in objects:
    print(obj.week,obj.time,obj.typeID,obj.amount,obj.typeName,obj.month,obj.userID,obj.expAmount,obj.iconURL,obj.year,obj.type,obj.date,obj.sortName,obj.iconName,obj.inAmount,obj.positiveAmount,obj.dbStatus,obj.serverID,obj.remark)
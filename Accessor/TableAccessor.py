from DatabaseLoader import DataBaseUtils
from Utils import FileUtils
from Entities.Column import Column
from Entities.Row import Row

class TableAccessor():
    def __init__(self,tablename):
        self.tablename = tablename
        self.tableObject = DataBaseUtils.getTable(tablename)

    def insertKey(self,key,columns):
        keyDict  = self.tableObject.getDictionaryFromKey(key)
        for column in columns:
            #using function since lower data structure can change
            keyDict.update({FileUtils.keyMaker(key, column.columnName):column.columnValue})

    def getValuedFromKey(self,key,columns):
        keyDict = self.tableObject.getDictionaryFromKey(key)
        row = Row(key)
        for column in columns:
            row.addcolumn(Column(column.columnName,keyDict.get(FileUtils.keyMaker(key,column.columnName),None)))
        return row

    #scan functionality which will scan an sorted array
    #need to maintain an sorted array which will help in getting start key and end key
    def scan(self, startkey, endkey,columns):
        pass






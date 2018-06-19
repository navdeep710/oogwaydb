from FileLoader import TableLoader
import Contants
import os

tables = set()
tablesDict = {}

def loadTableNames(self):
    tablesname = os.listdir(Contants.TABLE_LOCATION)
    #though this will be a set since filesystem is a set :)
    for name in tablesname:
        tables.add(name)

def createTable(tablename):
    if(tablename not in tables):
        tables.add(tablename)
        tablesDict[tablename] = TableLoader(tablename)
    else:
        print "table " + tablename + " already exists"

def getTable(tablename):
    if(tablename in tables):
        if(tablename not in tablesDict):
            tablesDict[tablename] = TableLoader(tablename)
        return tablesDict[tablename]
    else:
        print "table not present in self table , you need to create it first"

def saveTable(tablename):
    if(tablename in tablesDict):
        tableObject = tablesDict[tablename]
        tableObject.saveFiles()







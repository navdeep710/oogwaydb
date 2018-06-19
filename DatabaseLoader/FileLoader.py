#this class will load files from a given path
#currently i am keeping this location as static as table name
from collections import defaultdict
import os

from Utils import FileUtils
import KeyUtils
import Contants


#this is table loader which can have different functionality , but it must implement these operations
#self.tableDictionary must support get and update functions
class TableLoader:
    def __init__(self,tablename):
        self.tablename = tablename
        self.tablePath = Contants.TABLE_LOCATION + os.sep + tablename
        self.tableDictionary = defaultdict(dict)
        self.loadDirectory()


    def loadDirectory(self):
        if(os.path.exists(self.tablePath)):
            fileList = os.listdir(self.tablePath)
            for file in fileList:
                self.loadFile(file)
        else:
            os.mkdir(self.tablePath)


    def loadFile(self,filepath):
        filelines = open(self.tablePath + os.sep + filepath,'r').readlines()
        singleDict = {}
        for line in filelines:
            #column type can also be incorporated here
            line = line.rstrip()
            if(len(line) > 0):
                key,columnname,value = FileUtils.keyValuegetter(line)
                singleDict[FileUtils.keyMaker(key,columnname)] = value
        self.tableDictionary[filepath] = singleDict

    def saveFiles(self):
        for filename in self.tableDictionary.keys():
            dictFile = open(self.tablePath + os.sep + filename,"w")
            for key in self.tableDictionary[filename].keys():
                mkey,columnname = FileUtils.keyValuegetter(key)
                dictFile.write(FileUtils.keyValueMaker(mkey,columnname,self.tableDictionary[filename][key]))
                dictFile.write("\n")
            dictFile.close()

    #this function implementation can change depending upon the data structure
    def getDictionaryFromKey(self,key):
        return self.tableDictionary[KeyUtils.findKeyInarray(key)]










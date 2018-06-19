def getKeyValueSeparator():
    return ","

def keyValueMaker(key,columnname,value):
    return key + getKeyValueSeparator() + columnname + getKeyValueSeparator() + str(value)

def keyMaker(key,columnName):
    return key + getKeyValueSeparator() + columnName

def keyValuegetter(keyValueStr):
    return keyValueStr.split(getKeyValueSeparator())
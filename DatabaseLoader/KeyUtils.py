def getPresplitFiles():
    return ["1_1000",'1001_2000',"2001_3000","3001_4000","4001_5000"]

def findKeyInarray(key):
    for index,each in enumerate(getPresplitFiles()):
        mrange = each.split('_')
        if(int(key) >= int(mrange[0]) and int(key) <= int(mrange[1])):
            return each

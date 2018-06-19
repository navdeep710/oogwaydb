from Column import Column
class Row:
    def __init__(self,key):
        self.key = key
        self.columns = []

    def addcolumn(self,column):
        if(isinstance(column,Column)):
            self.columns.append(column)

    def __str__(self):
        return "key::" + self.key + " " + ",".join([str(x) for x in  self.columns])

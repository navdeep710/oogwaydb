class Column:
    def __init__(self,columnName,columnValue=None):
        self.columnName = columnName
        self.columnValue = columnValue

    def __str__(self):
        return "columnName::" + str(self.columnName) + " " + "columnValue::" +  str(self.columnValue)
from Accessor.TableAccessor import TableAccessor
from Entities.Column import Column
from DatabaseLoader import DataBaseUtils

DataBaseUtils.createTable("oogway")

tableObj = TableAccessor("oogway")

print tableObj.insertKey("2",[Column("name","nav"),Column("age",34)])
#print tableObj.getValuedFromKey("2",[Column("name",None),Column("age",None)])



# tableObj = TableAccessor("oogway")
# tableObj.insertKey("2002",[Column("name","anu"),Column("age",45)])


#DataBaseUtils.saveTable("oogway")


print tableObj.getValuedFromKey("2002",[Column("name",None),Column("age",None)])
print tableObj.getValuedFromKey("2",[Column("name",None),Column("age",None)])


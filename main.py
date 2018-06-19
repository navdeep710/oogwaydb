import atexit

from Accessor.TableAccessor import TableAccessor
from DatabaseLoader import DataBaseUtils
from Entities.Column import Column
from FileSync import SyncTable

tableObj = None

def main():
    print "hello !! welcome to the present"
    while(True):
        operation_num = raw_input("\x1b[1;%dm" % (31)  + ''' You will be entring your values to default db
                     \n you should first tell me what to you want to do
                     press 1 for insert
                     press 2 for get
                     else you want to beak free
                       \n''' +  "\x1b[0m")
        if(operation_num == "1"):
            insert_line = raw_input("\x1b[1;%dm" % (31) +  '''please insert in following manner:
                         row key for now primarly should be integer
                         key,column name , column value (comman separated)
                         eg  --> 1,age,32 \n''' +   "\x1b[0m")
            row_key,column_name,value = insert_line.rstrip().split(",")
            if(str(row_key).isdigit()):
                tableObj.insertKey(row_key,[Column(column_name,value)])
        elif(operation_num == "2"):
            get_line = raw_input("\x1b[1;%dm" % (31) + ''' please enter the key you want to access
                                     with column names in following format
                                     key, column1,column2 \n''' +  "\x1b[0m")
            line_values = get_line.split(",")
            key = line_values[0]
            str_columns = line_values[1:]
            columns = [Column(col,None) for col in str_columns]
            print tableObj.getValuedFromKey(key,columns)
        else:
            "you didt liked it , coming out of closet"
            break;



@atexit.register
def goodbye():
    DataBaseUtils.saveTable("oogway")



if __name__ == "__main__":
    DataBaseUtils.createTable("oogway")
    tableObj = TableAccessor("oogway")
    SyncTable.start("oogway")
    main()


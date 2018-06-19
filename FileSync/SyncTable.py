import threading
from DatabaseLoader import DataBaseUtils

def syncTableToDisk(tablename):
    DataBaseUtils.saveTable(tablename)
    print tablename + " synced"

def start(tablename,synctime=30):
    t = threading.Timer(synctime,syncTableToDisk,[tablename])
    t.start()

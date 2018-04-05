import os, os.path, time
from datetime import datetime

def deletefile(path):
    print(type(path))
    print("deleting the file")

# Get all files and folder from the given path
allfiles = os.walk(r"e:\classroom\python")

for (dirname, directories, files) in allfiles:
    if dirname.find(".git") >= 0:
        continue
    #print directory name
    print("Directory:", dirname)
    print("==========" + "=" * len(dirname))
    #print files in that directory
    for file in files:
        print(file)
        t = datetime.fromtimestamp(os.path.getmtime(dirname+'\\'+file))
        #print("%s" % time.ctime(os.path.getmtime(dirname+'\\'+file)))
        print("%s" % t)
        print("%s" % (datetime.now() - t))
        #print("%d" % (datetime.now() - t))
        delta = datetime.now() - t
        print(delta.days)
        deletefile(file)


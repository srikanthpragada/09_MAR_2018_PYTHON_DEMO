import os

allfiles = os.walk(r"e:\classroom\python\mar9\demo")

for (dirname, directories, files) in allfiles:
    # print directory name
    if dirname.find(".git") >= 0:
        continue
    print("Directory : ", dirname)
    print("=============" + "=" * len(dirname))
    # print files in that directory
    for file in files:
        print(file)

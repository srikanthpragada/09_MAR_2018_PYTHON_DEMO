# open file for writing in text mode
with open(r"e:\classroom\python\mar9\names.txt", "rt") as f:
    for lineno, name in enumerate(f.readlines()):
        print("{:03} {}".format(lineno + 1, name), end='')

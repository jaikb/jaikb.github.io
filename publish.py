import os

if len(os.sys.argv) > 1: 
    args = os.sys.argv
    file = args[1]
    comment = args[2]
    # push = args[3]
    os.system("git add %s" %file)
    os.system("git commit -m %s" %comment)
    if os.sys.argv[1] == "-c":
        os.system("git push")
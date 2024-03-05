import os
def chck(path):
    exists = os.path.exists(path)

    if exists:
        dirname, filename = os.path.split(path)
        print(dirname)
        print(filename)
    else:
        print("does not exist")


a = 'path'
chck(a)
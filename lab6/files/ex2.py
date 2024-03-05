import os
def chck(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)

    print(exists)
    print(readable)
    print(writable)
    print(executable)

a = 'path'
chck(a)
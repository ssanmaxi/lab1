import os
def ls(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    print(dirs)
    print(files)
    print(os.listdir(path))


a = 'path'
ls(a)
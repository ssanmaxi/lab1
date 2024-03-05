def cnt(file_path):
    with open(file_path, 'r') as file:
        lcnt = sum(1 for line in file)
        print(lcnt)

a = 'path'
cnt(a)
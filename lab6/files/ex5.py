def wr(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')

lst = [1, 2, 3, 4, 5]
out = 'path'
wr(out, lst)
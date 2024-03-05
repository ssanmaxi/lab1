import string

def gen():
    for c in string.ascii_uppercase:
        file_path = c + ".txt"
        with open(file_path, 'w') as file:
            file.write("This is file {}.".format(c))

gen()
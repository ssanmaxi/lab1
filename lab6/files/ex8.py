import os

def delet(path):
    exists = os.path.exists(path)
    if exists and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted successfully.")
    elif exists:
        print("No write access to the file.")
    else:
        print("File does not exist.")

# Example usage:
a = 'path'
delet(a)
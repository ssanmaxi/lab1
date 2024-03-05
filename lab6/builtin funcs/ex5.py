def true(tuple):
    return all(tuple)

tuple = (True, True, False, True)

if true(tuple):
    print("true")
else:
    print("not all true")
thisset = {"apple", "banana", "cherry"}
print(thisset) #{'cherry', 'apple', 'banana'}


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) #{'banana', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) #{True, 2, 'banana', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset) #{False, True, 'cherry', 'apple', 'banana'}


thisset = {"apple", "banana", "cherry"}

print(len(thisset)) #3


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"}  #{True, 34, 40, 'male', 'abc'}


myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #{'apple', 'banana', 'cherry'}



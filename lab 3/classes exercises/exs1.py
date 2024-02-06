class User:
    def getString(self , a):
        return str(a)

    def printString(self , a):
        print(a.upper())



user = User()

str1 = user.getString('Apple')

user.printString("apple")

#Define a class which has at least two methods getString: to get a string from console input printString: to print the string in upper case.Also please include simple test function to test the class methods.

class Assignment:

    def __init__(self):
        self.string=input("enter a string")

    def getstring(self):

        return self


    def printstring(self):
       print(self.string.upper())

def test():
    result=Assignment()

    result.getstring()
    result.printstring()



test()
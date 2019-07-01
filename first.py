def changename(mylist):
    mylist.append([12,13,14])
    print("inside function",mylist)
    return

mylist=[10,20,30]
changename(mylist)
print("after function",mylist)
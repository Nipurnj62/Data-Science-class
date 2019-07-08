string=input("enter a string")
print(string)

lower_count=upper_count=0
for i in string:
    if i.islower():
        lower_count+=1
    elif i.isupper():
        upper_count+=1



print("total lowercse letter ",lower_count)
print("total uppercase letter",upper_count)
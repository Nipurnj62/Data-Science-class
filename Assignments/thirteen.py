string=input("enter a string")

chr_count=digi_count=0
for i in string:
    if i.isdigit():
        digi_count+=1
    elif i.isalpha():
        chr_count+=1



print("total count of characters ",chr_count)
print("total count of digit ",digi_count)





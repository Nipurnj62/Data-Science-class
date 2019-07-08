new_list=[]
values=input("enter some numbers").split(",")


for i in values:
    binary_conversion=int(i,2)
    if binary_conversion%5==0:
        new_list.append(i)

    else:
        continue

print(','.join(new_list))
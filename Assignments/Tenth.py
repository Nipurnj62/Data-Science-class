str=input("enter a string")
split_string=str.split()

empty_list=[]
for i in split_string:
    if i  not in empty_list:
        empty_list.append(i)
    else:
         continue


empty_list.sort()
print(' '.join(empty_list))




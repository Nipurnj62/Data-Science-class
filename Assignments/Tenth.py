#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
str=input("enter a string")
split_string=str.split()

empty_list=[]
for i in split_string:
    if i  not in empty_list:
        empty_list.append(i)
    else:
         continue


empty_list.sort()
print((' ').join(empty_list))




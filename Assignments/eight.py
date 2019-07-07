#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
unsorted_string= input("enter a string")

split_string=unsorted_string.split()


newlist=[]
for i in split_string:
        newlist.append(i)

newlist.sort()
print(','.join(newlist))
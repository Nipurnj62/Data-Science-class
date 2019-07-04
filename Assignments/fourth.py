#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:


values=input("enter some numbers")

new_list=list(values.split())
new_tuple=tuple(values.split())
print(new_list)
print(new_tuple)

